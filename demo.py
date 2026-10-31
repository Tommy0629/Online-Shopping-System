from user import User, RegularUser, PremiumUser
from product import Product, Clothing, Electronics

# Polymorphic function: accepts any Product and calls its get_description()
def describe_product(product: Product):
    print(product.get_description())

# Create multiple instances of each subclass
user1 = RegularUser("Alice", "alice@example.com", 250)
user2 = PremiumUser("Bob", "bob@example.com", "platinum")
user3 = RegularUser("Charlie", "charlie@example.com", 50)
user4 = PremiumUser("Diana", "diana@example.com", "gold")

product1 = Clothing("Cotton T-Shirt", 19.99, "M")
product2 = Clothing("Denim Jeans", 49.99, "L")
product3 = Electronics("Wireless Headphones", 129.99, 12)
product4 = Electronics("Mechanical Keyboard", 79.99, 36)

# Demonstrate composition: add products to user carts
user1.shopping_cart.add_product(product1)
user1.shopping_cart.add_product(product3)
user2.shopping_cart.add_product(product2)

print("Alice's cart:")
user1.shopping_cart.list_products()

print("Bob's cart:")
user2.shopping_cart.list_products()

# Call the polymorphic function on different subclasses
describe_product(product1)
describe_product(product3)

# Show class attributes via class methods
print("Total products created:", Product.get_product_count())
print("Total users created:", User.get_user_count())

# Demonstrate remove from cart
user1.shopping_cart.remove_product(product1)

print("Alice's cart after removal:")
user1.shopping_cart.list_products()

# Show polymorphic get_discount_rate() across different User subclasses
print("Discount rate for Alice:", user1.get_discount_rate() * 100, "%")
print("Discount rate for Bob:", user2.get_discount_rate() * 100, "%")
print("Discount rate for Charlie:", user3.get_discount_rate() * 100, "%")
print("Discount rate for Diana:", user4.get_discount_rate() * 100, "%")

# Extension: user input to create your own account
try:
    choice = input("New account -> [R]egular or [P]remium? ").strip().upper()
    name = input("Name: ")

    # Create object first so set_name() validates immediately on input
    if choice == "P":
        shopper = PremiumUser(name, "@")
    else:
        shopper = RegularUser(name, "@", 0)

    email = input("Email: ")
    shopper.set_email(email)

    if choice == "P":
        tier = input("Tier (gold/platinum): ")
        shopper.set_membership_tier(tier)
    else:
        points = input("Starting loyalty points: ")
        shopper.set_loyalty_points(points)

    # First product (no y/n prompt)
    kind = input("Product type -> [C]lothing or [E]lectronics? ").strip().upper()
    pname = input("Product name: ")

    if kind == "C":
        new_product = Clothing(pname, 1.0, "M")
    else:
        new_product = Electronics(pname, 1.0, 0)

    price = input("Price: ")
    new_product.set_price(price)

    if kind == "C":
        size = input("Size (XS/S/M/L/XL): ")
        new_product.set_size(size)
    else:
        months = input("Warranty months: ")
        new_product.set_warranty_months(months)

    shopper.shopping_cart.add_product(new_product)
    describe_product(new_product)

    # Loop: ask after each additional product
    while True:
        more = input("\nAdd another product? [y/n]: ").strip().lower()
        if more == "n":
            break

        kind = input("Product type -> [C]lothing or [E]lectronics? ").strip().upper()
        pname = input("Product name: ")

        if kind == "C":
            new_product = Clothing(pname, 1.0, "M")
        else:
            new_product = Electronics(pname, 1.0, 0)

        price = input("Price: ")
        new_product.set_price(price)

        if kind == "C":
            size = input("Size (XS/S/M/L/XL): ")
            new_product.set_size(size)
        else:
            months = input("Warranty months: ")
            new_product.set_warranty_months(months)

        shopper.shopping_cart.add_product(new_product)
        describe_product(new_product)

    print("\nYour final cart:")
    shopper.shopping_cart.list_products()

    subtotal = shopper.shopping_cart.get_subtotal()
    discount = shopper.get_discount_rate()
    final = subtotal * (1 - discount)

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Your discount rate: {discount * 100:.1f}%")
    print(f"Final price after discount: ${final:.2f}")
except ValueError as e:
    print(f"Invalid input, skipping extension. ({e})")

print("Total products created:", Product.get_product_count())
print("Total users created:", User.get_user_count())