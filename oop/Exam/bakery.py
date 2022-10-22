from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type == 'Bread' or food_type == 'Cake':
            food = [foods for foods in self.food_menu if foods.name == name]
            if food:
                raise Exception(f"{food_type} {name} is already in the menu!")
            if food_type == 'Bread':
                self.food_menu.append(Bread(name, price))
            elif food_type == 'Cake':
                self.food_menu.append(Cake(name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if drink_type == 'Tea' or drink_type == 'Water':
            drink = [drinks for drinks in self.drinks_menu if drinks.name == name]
            if drink:
                raise Exception(f"{drink_type} {name} is already in the menu!")
            if drink_type == 'Tea':
                self.drinks_menu.append(Tea(name, portion, brand))
            elif drink_type == 'Water':
                self.drinks_menu.append(Water(name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type == 'OutsideTable' or table_type == 'InsideTable':
            table = [table for table in self.tables_repository if table_number == table.table_number]
            if table:
                raise Exception(f"Table {table_number} is already in the bakery!")
            if table_type == 'InsideTable':
                self.tables_repository.append(InsideTable(table_number, capacity))
            elif table_type == 'OutsideTable':
                self.tables_repository.append(OutsideTable(table_number, capacity))
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved:
                if table.capacity >= number_of_people:
                    table.number_of_people = number_of_people
                    table.is_reserved = True
                    return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_name):
        messages = []
        n = '\n'
        food_list = list(food_name)
        for table in self.tables_repository:
            if table.table_number == table_number:
                messages.append(f"Table {table_number} ordered:")
                for food in food_list:
                    for food_ in self.food_menu:
                        if food == food_.name:
                            table.order_food(food_)
                            messages.append(f' - {food_.name}: {food_.portion:.2f}g - {food_.price:.2f}lv')
                            food_list.remove(food)
                if food_list:
                    messages.append(f'{self.name} does not have in the menu:')
                    for food in food_list:
                        messages.append(f'{food}')
                return n.join(messages)
        return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *drinks_name):
        messages = []
        n = '\n'
        drink_list = list(drinks_name)
        for table in self.tables_repository:
            if table.table_number == table_number:
                messages.append(f"Table {table_number} ordered:")
                for drink in drink_list:
                    for drink_ in self.drinks_menu:
                        if drink == drink_.name:
                            table.order_drink(drink_)
                            messages.append(
                                f' - {drink_.name} {drink_.brand} - {drink_.portion:.2f}ml - {drink_.price:.2f}lv')
                            drink_list.remove(drink)
                if drink_list:
                    messages.append(f'{self.name} does not have in the menu:')
                    for drink in drink_list:
                        messages.append(f'{drink}')
                    return n.join(messages)
        return f"Could not find table {table_number}"

    def leave_table(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                bill = table.get_bill()
                self.total_income += bill
                table.clear()
                return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        messages = []
        n = '\n'
        for table in self.tables_repository:
            if not table.is_reserved:
                messages.append(table.free_table_info())
        return n.join(messages)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
