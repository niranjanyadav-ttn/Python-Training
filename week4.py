# Q1. Object Modeling & Core OOP
# Design a multi-role User Management System where:
# A base class defines common identity attributes.
# Multiple specialized user types inherit from the base class.
# Each subclass overrides at least one behavior from the parent class.
# A class-level attribute tracks the total number of active users across all subclasses.

class User:

    total_active_users = 0
    
    def __init__(self, user_id, name, email, is_active=True):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.is_active = is_active
        
        if self.is_active:
            User.total_active_users += 1
    
    def get_details(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email}"
    
    def get_permissions(self):
        return ["read"]
    
    def deactivate(self):
        if self.is_active:
            self.is_active = False
            User.total_active_users -= 1
            print(f"User {self.name} has been deactivated")
    
    def activate(self):
        if not self.is_active:
            self.is_active = True
            User.total_active_users += 1
            print(f"User {self.name} has been activated")
    
    @classmethod
    def get_total_active_users(cls):
        return cls.total_active_users


class Admin(User):
    
    def __init__(self, user_id, name, email, department, is_active=True):
        
        super().__init__(user_id, name, email, is_active)
        self.department = department
        self.role = "Admin"
    
    def get_permissions(self):
        return ["read", "write", "delete", "manage_users", "system_config"]
    
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Role: {self.role}, Department: {self.department}"
    
    def manage_user(self, user, action):
        return f"Admin {self.name} performed '{action}' on user {user.name}"


class Customer(User):
    
    def __init__(self, user_id, name, email, membership_tier="Basic", is_active=True):
     
        super().__init__(user_id, name, email, is_active)
        self.membership_tier = membership_tier
        self.role = "Customer"
        self.purchase_history = []
    
    def get_permissions(self):
        return ["read", "write_reviews", "make_purchases", "view_orders"]
    
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Role: {self.role}, Membership: {self.membership_tier}"
    
    def add_purchase(self, item):
        self.purchase_history.append(item)
        return f"Customer {self.name} purchased: {item}"

if __name__ == "__main__":
    print("=== User Management System Demo ===\n")
    
    admin1 = Admin(101, "Alice Johnson", "alice@company.com", "IT Security")
    customer1 = Customer(201, "Bob Smith", "bob@email.com", "Gold")
    customer2 = Customer(202, "Charlie Brown", "charlie@email.com", "Silver")
    print(f"Total Active Users: {User.get_total_active_users()}\n")
    
    print("--- User Details ---")
    print(admin1.get_details())
    print(customer1.get_details())
    print(customer2.get_details())
    print()
    
    print("--- User Permissions ---")
    print(f"Admin permissions: {admin1.get_permissions()}")
    print(f"Customer permissions: {customer1.get_permissions()}")
    print()
    
    print("--- Specific User Actions ---")
    print(admin1.manage_user(customer1, "reset_password"))
    print(customer1.add_purchase("Laptop"))
    print()
    
    print("--- User Activation Management ---")
    customer2.deactivate()
    print(f"Total Active Users: {User.get_total_active_users()}")
    
    customer2.activate()
    print(f"Total Active Users: {User.get_total_active_users()}")
    print()

# Q2. Advanced Class Construction
# Implement:
# A @classmethod that creates an object from a single serialized string.
# A @staticmethod that performs validation logic independent of class state.
# Demonstrate the difference in responsibility between the two methods through usage.
class Product:
    
    tax_rate = 0.18 
    
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, ₹{self.price})"
    
    @classmethod
    def from_string(cls, product_string):
        product_id, name, price = product_string.split(',')
        return cls(int(product_id), name.strip(), float(price))
    
    @staticmethod
    def is_valid_price(price):
        try:
            price_value = float(price)
            return price_value > 0
        except ValueError:
            return False
    
    @staticmethod
    def calculate_tax(price):
        return price * Product.tax_rate


if __name__ == "__main__":
    print("=== CLASSMETHOD vs STATICMETHOD Demo ===\n")
    
    print("1. Normal Constructor:")
    p1 = Product(101, "Laptop", 50000)
    print(f"   {p1}\n")
    
    print("2. CLASSMETHOD:")
    product_string = "102, Mobile Phone, 25000"
    p2 = Product.from_string(product_string)
    print(f"   Input: '{product_string}'")
    print(f"   Output: {p2}\n")
    
    print("3. STATICMETHOD (Validation):")
    print(f"   Is 5000 valid price? {Product.is_valid_price(5000)}")
    print(f"   Is -100 valid price? {Product.is_valid_price(-100)}")
    print(f"   Is 'abc' valid price? {Product.is_valid_price('abc')}\n")
    
    print("4. STATICMETHOD (Utility Calculation):")
    price = 10000
    tax = Product.calculate_tax(price)
    print(f"   Price: ₹{price}")
    print(f"   Tax (18%): ₹{tax}")
    print(f"   Total: ₹{price + tax}")
    print()

# Q3. Deep Usage of Special Methods
# Enhance one core entity by implementing:
# __str__ for human-readable output
# __repr__ for developer-friendly debugging
# __len__ to represent a business-meaningful metric
# __eq__ and __lt__ for object comparison
# __call__ to make the object behave like a function
class ShoppingCart:
    
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.items = []
    
    def add_item(self, product_name, price, quantity=1):
        self.items.append((product_name, price, quantity))
    
    def get_total(self):
        return sum(price * quantity for _, price, quantity in self.items)
    
    def __str__(self):
        total = self.get_total()
        return f"Cart[{self.customer_name}]: {len(self.items)} items | ₹{total:.2f}"
    
    def __repr__(self):
        return f"ShoppingCart('{self.customer_name}', {self.cart_id}, items={len(self.items)})"
    
    def __len__(self):
        return sum(quantity for _, _, quantity in self.items)
    
    def __eq__(self, other):
        if not isinstance(other, ShoppingCart):
            return False
        return self.get_total() == other.get_total()
    
    def __lt__(self, other):
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        return self.get_total() < other.get_total()
    
    def __call__(self, discount_percentage=0):
        total = self.get_total()
        final = total * (1 - discount_percentage / 100)
        return final

if __name__ == "__main__":
    print("=== Special Methods Demo ===\n")
    
    cart1 = ShoppingCart("Alice", 1001)
    cart1.add_item("Laptop", 50000, 1)
    cart1.add_item("Mouse", 500, 2)
    
    cart2 = ShoppingCart("Bob", 1002)
    cart2.add_item("Mobile", 25000, 2)
    
    print("1. __str__ vs __repr__:")
    print(f"   print(): {cart1}")
    print(f"   repr():  {repr(cart1)}\n")
    
    print(f"2. __len__: cart1 has {len(cart1)} total items\n")
    
    print(f"3. __eq__: cart1 == cart2? {cart1 == cart2}")
    print(f"   (₹{cart1.get_total()} vs ₹{cart2.get_total()})\n")
    
    print("4. __lt__: Sorting carts by value")
    carts = [cart1, cart2]
    sorted_carts = sorted(carts)
    for c in sorted_carts:
        print(f"   {c.customer_name}: ₹{c.get_total()}\n")
    
    print("5. __call__: cart1(15) applies 15% discount")
    print(f"   Original: ₹{cart1.get_total()}")
    print(f"   After discount: ₹{cart1(15)}")
    print()

# Q4. Decorator-Driven Behavior Control
# Create:
# A decorator that logs function execution metadata.
# A parameterized decorator that conditionally enables or disables logging.
# Apply decorators across multiple class methods without changing their internal logic.
