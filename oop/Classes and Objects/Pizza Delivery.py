class PizzaDelivery:
    def __init__(self, name, price, ingredient):
        self.name = name
        self.price = price
        self.ingredients = dict(ingredient)
        self.ordered = False

    def add_extra(self, ingredient, quantity, ingredient_price):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += ingredient_price * quantity
        else:
            self.ingredients[ingredient] = quantity
            self.price += quantity * ingredient_price

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif ingredient in self.ingredients:
            value = self.ingredients[ingredient]
            if value < quantity:
                return f"Please check again the desired quantity of {ingredient}!"
            self.ingredients[ingredient] = value - quantity
            self.price -= quantity * ingredient_price

    def make_order(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join((': '.join((str(i), str(q)))) for i, q in self.ingredients.items())} and the price will be {self.price}lv."
