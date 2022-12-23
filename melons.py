"""Classes for melon orders."""

class AbstractMelonOrder:
    #made the base_price parameter as default paramter and set to 5 here in parent class. So, that we can use in all child classes
    def __init__(self, species, qty, base_price = 5):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = base_price

    def get_total(self):
        """Calculate price, including tax."""

    
        if self.species == "christmas melon":
            self.base_price = 1.5 * (self.base_price)

        total = (1 + self.tax) * self.qty * self.base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)

        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17
   
    def get_total(self):
        """Calculate price, including tax."""
        total = super().get_total()

        if self.qty < 10:
            total = total + 3

        return total
         
    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.passed_inspection = False

    def get_total(self):
            """Calculate price, including tax."""
            #used the base_price attribute from the parent class and put it in a new variable
            base_price = self.base_price
            #instead of using a new variable to take the base_price we can simply use self.base_price
            total =  self.qty * base_price
            return total

    def mark_inspection(self, passed):
        self.passed_inspection = passed
        

# order0 = AbstractMelonOrder()
# international = InternationalMelonOrder("watermelon", 6, "AUS")
# total = international.get_total()
# domestic = DomesticMelonOrder("watermelon", 6)
# total1 = domestic.get_total()
# print(total)
# print(total1)