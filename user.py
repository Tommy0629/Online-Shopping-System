from abc import ABC, abstractmethod
from shoppingcart import ShoppingCart

# Base class #1: User (abstract), has-a ShoppingCart (composition)
class User(ABC):
    _user_count = 0  # class attribute: tracks total users created

    def __init__(self, name: str, email: str):
        self.set_name(name)
        self.set_email(email)
        self.shopping_cart = ShoppingCart()  # composition: user has-a cart
        User._user_count += 1

    # abstract method: subclasses must override this
    @abstractmethod
    def get_discount_rate(self):
        raise NotImplementedError

    # class method: access the class attribute without an instance
    @classmethod
    def get_user_count(cls) -> int:
        return cls._user_count

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        if self._is_valid_string(name):
            self._name = name
        else:
            raise ValueError("Invalid value given for name")

    def get_email(self):
        return self._email

    def set_email(self, email: str):
        if self._is_valid_string(email) and "@" in email:
            self._email = email
        else:
            raise ValueError("Invalid value given for email")

    # SRP helper: reject empty strings and pure-digit names
    def _is_valid_string(self, value) -> bool:
        if not isinstance(value, str) or value.strip() == "":
            return False
        if value.strip().isdigit():
            return False
        return True

    def __str__(self):
        return f"Name: {self.get_name()}, Email: {self.get_email()}"


# Subclass 1 of User: regular customer earns loyalty points
class RegularUser(User):
    def __init__(self, name: str, email: str, loyalty_points: int):
        super().__init__(name, email)
        self.set_loyalty_points(loyalty_points)

    def get_loyalty_points(self):
        return self._loyalty_points

    def set_loyalty_points(self, loyalty_points):
        if self._is_valid_points(loyalty_points):
            self._loyalty_points = int(loyalty_points)
        else:
            raise ValueError("Invalid value given for loyalty_points")

    # SRP helper: points must be a non-negative number
    def _is_valid_points(self, value) -> bool:
        try:
            return int(value) >= 0
        except (ValueError, TypeError):
            return False

    # override abstract method: discount grows with points, capped at 5%
    def get_discount_rate(self):
        return min(self._loyalty_points / 100 * 0.01, 0.05)

    def __str__(self):
        return super().__str__() + f", Points: {self.get_loyalty_points()}"


# Subclass 2 of User: premium customer gets tier-based discount
class PremiumUser(User):
    _TIER_DISCOUNTS = {"gold": 0.10, "platinum": 0.15}  # class attribute

    def __init__(self, name: str, email: str, membership_tier: str = "gold"):
        super().__init__(name, email)
        self.set_membership_tier(membership_tier)

    def get_membership_tier(self):
        return self._membership_tier

    def set_membership_tier(self, membership_tier: str):
        if membership_tier.lower() in self._TIER_DISCOUNTS:
            self._membership_tier = membership_tier.lower()
        else:
            raise ValueError("Invalid value given for membership_tier")

    # override abstract method: look up discount by tier
    def get_discount_rate(self):
        return self._TIER_DISCOUNTS[self._membership_tier]

    def __str__(self):
        return super().__str__() + f", Tier: {self.get_membership_tier()}"