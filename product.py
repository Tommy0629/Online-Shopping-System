from abc import ABC, abstractmethod

# Base class #2: Product (abstract), extended by Clothing and Electronics
class Product(ABC):
    _product_count = 0  # class attribute: tracks total products created

    def __init__(self, name: str, price: float):
        self.set_name(name)
        self.set_price(price)
        Product._product_count += 1

    # abstract method: subclasses must provide their own description
    @abstractmethod
    def get_description(self):
        raise NotImplementedError

    # class method: read the class attribute without an instance
    @classmethod
    def get_product_count(cls) -> int:
        return cls._product_count

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        if self._is_valid_name(name):
            self._name = name
        else:
            raise ValueError("Invalid value given for name")

    # SRP helper: reject empty strings and pure-digit names
    def _is_valid_name(self, value) -> bool:
        if not isinstance(value, str) or value.strip() == "":
            return False
        if value.strip().isdigit():
            return False
        return True

    def get_price(self):
        return self._price

    def set_price(self, price):
        if self._is_valid_price(price):
            self._price = float(price)
        else:
            raise ValueError("Invalid value given for price")

    # SRP helper: price must convert to float and be greater than zero
    def _is_valid_price(self, value) -> bool:
        try:
            return float(value) > 0
        except (ValueError, TypeError):
            return False


# Subclass 1 of Product: clothing item has a size
class Clothing(Product):
    def __init__(self, name: str, price: float, size: str):
        super().__init__(name, price)
        self.set_size(size)

    def get_size(self):
        return self._size

    def set_size(self, size: str):
        valid = {"XS", "S", "M", "L", "XL"}
        if isinstance(size, str) and size.upper() in valid:
            self._size = size.upper()
        else:
            raise ValueError("Invalid value given for size")

    # override abstract method: clothing-specific description
    def get_description(self):
        return f"[Clothing] {self._name} - size {self._size}, ${self._price:.2f}"

    def __str__(self):
        return f"Clothing: {self._name} | size={self._size} | ${self._price:.2f}"


# Subclass 2 of Product: electronics item has a warranty length
class Electronics(Product):
    def __init__(self, name: str, price: float, warranty_months: int):
        super().__init__(name, price)
        self.set_warranty_months(warranty_months)

    def get_warranty_months(self):
        return self._warranty_months

    def set_warranty_months(self, warranty_months):
        if self._is_valid_months(warranty_months):
            self._warranty_months = int(warranty_months)
        else:
            raise ValueError("Invalid value given for warranty_months")

    # SRP helper: warranty months must be a non-negative number
    def _is_valid_months(self, value) -> bool:
        try:
            return int(value) >= 0
        except (ValueError, TypeError):
            return False

    # override abstract method: electronics-specific description
    def get_description(self):
        return f"[Electronics] {self._name} - {self._warranty_months}-month warranty, ${self._price:.2f}"

    def __str__(self):
        return f"Electronics: {self._name} | warranty={self._warranty_months}mo | ${self._price:.2f}"