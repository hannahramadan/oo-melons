"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax 

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas melon":
            base_price = 5 * 1.5

        total = (1 + self.tax) * self.qty * base_price
        
        # __repr__("It's Christmas yayy!")
        # Q: how to do if statement for class?
        # if type(self) == InternationalMelonOrder:
        #     print('Domestic')

        return total

        # Now, Christmas melons will cost 1.5 times as much as the base price.
        # Also, a flat fee of $3 will be added to all international orders with less than 10 melons

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

###################

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "domestic", 0.08)

#########################

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code
    
    def get_total(self):
        """Calculate price, including tax."""
        int_total = super().get_total()
        if self.qty < 10:
            int_total += 3
        return int_total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
