class Nutrition:
   total_calories = ""
   consumed_calories = ""
   calories_remaining = ""

def add_meals(self,calories,meal_name):
    self.consumed_calories += calories
    self.calories_remaining -= calories
    print(f"{meal_name} - {calories} calories was added to the nutrition")

def get_consumed_calories(self):
    return self.consumed_calories

def get_remaining_calories(self):
    return self.calories_remaining

