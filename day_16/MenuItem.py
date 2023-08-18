#!/usr/bin/python3

# Day 16 for 100 Days of code challenge - Coffee machine version 2.0
import turtle


class MenuItem:

    """
        MenuItems class for the coffee machiune

        Attributes:
            name (str): The name of the drink
            cost (float): The cost of the drink
            ingredients (dict): The ingredients and amounts required
                to make the drink

    """
    def __init__(self, name="", cost=0, ingredients=None):
        """ Initialises the MenuItem objects."""
        if ingredients is None:
            ingredients = {}
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


    def get_items(self):
        names = self.name
        return names