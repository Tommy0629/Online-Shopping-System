from product import Product

# Composition class: User has-a ShoppingCart, ShoppingCart has-a list of Products
class ShoppingCart():

    def __init__(self) -> None:
        self._productlist = []  # stores Product objects

    def add_product(self, product: Product):
        if self._is_valid_product(product):
            self._productlist.append(product)
        else:
            raise ValueError("Invalid product given - must be a Product object")

    def remove_product(self, product: Product):
        if not self._is_valid_product(product):
            raise ValueError("Invalid product 1given - must be a Product object")
        elif product not in self._productlist:
            print("The product is not in the car")
        else:

    # list all products using index loop
    def list_products(self):
        for i in range(len(self._productlist)):
            print(f"Item #{i+1}: {self._productlist[i].get_name()}")
            print("1")

    # calculate total price of all items in the cart
    def get_subtotal(self):
        total = 0
        for i in range(len(self._productlist)):
            total = total + self._productlist[i].get_price()
        return total

    # SRP helper: type-check before adding/removing
    def _is_valid_product(self, product: Product):
        if isinstance(product, Product):
            return True
        else:
            return False