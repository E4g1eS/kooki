from __future__ import annotations
import json
import tkinter as tk
import os

DATA_PATH = "data.json"

class Ingredient:
    _name : str

    def __str__(self):
        return f"{self._name}"

class Amount:
    _value : float
    _unit : str

    def __str__(self):
        return f"{self._value} {self._unit}"

class Recipe:
    _ingredients: list[tuple(Ingredient, Amount)]
    _steps: list[str]
    _notes: list[str]

    def __str__(self):
        result = ""
        for ingredient in self._ingredients:
            result += f"{ingredient[0]} -- {ingredient[1]}\n"

        for index, step in self._steps:
            result += f"{index}.) {step}\n"

        for note in self._notes:
            result += f"-- {note}\n"

class Cookbook:
    _recipes: list[Recipe]

class App(tk.Tk):
    _cookbook : Cookbook
    
    def _read_data(self):

        if not os.path.isfile(DATA_PATH):
            with open(DATA_PATH, "x", encoding="utf-8") as data_file:
                data_file.write("{}")

        data = None
        with open(DATA_PATH, "r", encoding="utf-8") as data_file:
            data = data_file.read()

        json_data = json.loads(data)
        print(json_data)

    def load(self):
        self._read_data()



if __name__ == "__main__":
    app = App()
    app.load()
    app.mainloop()