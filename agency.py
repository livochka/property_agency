# Module created to represent property agency
# Here you can call to agent, add and delete property
# We can show you all available properties
# Also we can advice you properties in order to your wished price
last_id = 0


def get_valid_input(input_string, valid_options):
    """
    (str, tuple) -> str
    Created to get valid input from user
    input_string: intro string with details of input
    valid_options: tuple with valid answer option
    return: user answer
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    """
    Created to represent properties
    """

    def __init__(self, square_feet='', beds='', baths=''):
        global last_id
        self.id = last_id + 1
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Created to display information about property on screen
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        Allows to create object Property with user arguments for this class
        return: dictionary with keys 'square_feet', 'beds' and 'bath' and
        input values
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    Class for representation Apartments
    """

    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Created to display information about Apartment
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)
        print()

    def prompt_init():
        """
        Allows to create object Apartment with user arguments for this class
        return: dictionary with keys 'square_feet', 'beds', 'bath',
        'laundry', 'balcony' and input values
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input('What laundries facilities does the'
                                  'property have?', Apartment.valid_laundries)

        balcony = get_valid_input("Does the property have a balcony? ",
                                  Apartment.valid_balconies)
        parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    Class for representing House
    """

    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Created to display information about Houses on screen
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))
        print()

    def prompt_init():
        """
        Allows to create object House with user arguments for this class
        return: dictionary with keys 'square_feet', 'beds', 'bath',
        'num_stories', 'garage', 'fenced' and input values
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({"fenced": fenced, "garage": garage,
                            "num_stories": num_stories})
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Class for representing rental operations
    """

    def __init__(self, furnished='', utilities='', rent=''):
        self.furnished = furnished
        self.rent = float(rent)
        self.utilities = utilities

    def display(self):
        """
        Created to display details of property purchase
        """

        print("RENTAL DETAILS")
        print("rent: {}".format(str(self.rent)))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))
        print()

    def prompt_init():
        """
        Allows to create Purchase object with values by user
        return: dictionary with keys 'rent', 'utilities', 'furnished'
        and values were input by user
        """

        return dict(rent=input("What is the monthly rent? (please, enter a "
                               "number) "),
                    utilities=input("What are the estimated utilities? "),
                    furnished=get_valid_input("Is the property furnished? ",
                                              ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    Class for representing purchase operations
    """

    def __init__(self, price='', taxes=''):
        self.price = float(price)
        self.taxes = float(taxes)

    def display(self):
        """
        Created to display details of property purchase
        """

        print("PURCHASE DETAILS")
        print("selling price: {}".format(str(self.price)))
        print("estimated taxes: {}".format(str(self.taxes)))
        print()

    def prompt_init():
        """
        Allows to create Purchase object with values by user
        return: dictionary with keys 'price', 'taxes' and values were input
        by user
        """

        return dict(price=input("What is the selling price? (please, enter a "
                                "number) "),
                    taxes=input("What are the estimated taxes? (please, "
                                "enter a number) "))

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Apartment):
    """
    Class for representing apartment, which you can rent, and their details
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rental_info = Rental.prompt_init()
        self.pay = Rental(rent=rental_info['rent'],
                          furnished=rental_info['furnished'],
                          utilities=rental_info['utilities'])

    def display(self):
        """
        Created to display information about HouseRental object on screen
        """
        super().display()
        self.pay.display()


class ApartmentPurchase(Apartment):
    """
    Class for representing apartment, which you can buy, and their details
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        purchase_info = Purchase.prompt_init()
        self.pay = Purchase(price=purchase_info['price'],
                            taxes=purchase_info['taxes'])

    def display(self):
        """
        Created to display information about HouseRental object on screen
        """
        super().display()
        self.pay.display()


class HousePurchase(House):
    """
    Class for representing house, which you can buy, and their details
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        purchase_info = Purchase.prompt_init()
        self.pay = Purchase(price=purchase_info['price'],
                            taxes=purchase_info['taxes'])

    def display(self):
        """
        Created to display information about HouseRental object on screen
        """
        super().display()
        self.pay.display()


class HouseRental(House):
    """
    Class for representing house, which you can rent, and their details
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        renta_info = Rental.prompt_init()
        self.pay = Rental(rent=renta_info['rent'],
                          furnished=renta_info['furnished'],
                          utilities=renta_info['utilities'])

    def display(self):
        """
        Created to display information about HouseRental object on screen
        """
        super().display()
        self.pay.display()


class Agent:
    """
    Class for representing property agent
    """

    type_map = {("house", "rental"): HouseRental,
                ("house", "purchase"): HousePurchase,
                ("apartment", "rental"): ApartmentRental,
                ("apartment", "purchase"): ApartmentPurchase,
                "house": House,
                'apartment': Apartment,
                'renting': Rental,
                'purchasing': Purchase}

    def __init__(self):
        self.property_list = []

    def _find_property_for_advising(self, pay_type, price):
        """
        (class, number) -> list
        Created to find property that suit for you in price
        pay_type: payment type - rent or purchase
        price: maximum price you could pay
        return: list with properties that suits to you
        """
        best = []
        for prop in self.property_list:
            if isinstance(prop.pay, Rental) and Rental == pay_type \
                    and price >= prop.pay.rent:
                best.append(prop)
            if isinstance(prop.pay, Purchase) and Purchase == pay_type \
                    and price >= prop.pay.price + 0.01 * prop.pay.taxes * \
                            prop.pay.price:
                best.append(prop)
        return best

    def _get_price():
        """
        Created to get user maximum price for current operation
        """
        question = "What is the maximum price you could pay? "
        while True:
            try:
                return float(input(question))
            except ValueError:
                continue

    _get_price = staticmethod(_get_price)

    def _print_advice(advice):
        """
        list -> none
        Created to print info about property agent advice to you
        advice: list with properties agent advice to you
        """
        if advice:
            print("\nWe have found a property for you!!!\n")
            for i in advice:
                i.display()
        else:
            print("Sorry, nothing found :(")

    _print_advice = staticmethod(_print_advice)

    def advice_property(self):
        """
        Created to advice you property from agent property list
        """
        pay_type = get_valid_input('Renting or purchasing?',
                                   ('renting', 'purchasing'))
        price = self._get_price()
        payment = self.type_map[pay_type]
        advice = self._find_property_for_advising(payment, price)
        self._print_advice(advice)

    def display_properties(self):
        """
        Created to display information about available properties
        in property list
        """
        for prop in self.property_list:
            prop.display()

    def add_property(self):
        """
        Created to add properties with parameters from user
        """
        property_type = get_valid_input("What type of property? ",
                                        ("house", "apartment")).lower()

        payment_type = get_valid_input("What payment type? ",
                                       ("purchase", "rental")).lower()
        PropertyClass = self.type_map[property_type]
        PropertySubclass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertySubclass(**init_args))
