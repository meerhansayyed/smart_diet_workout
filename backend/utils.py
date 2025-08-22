import pandas as pd
from projects_paths import FOOD_DATASET

def load_food_dataset():
    return pd.read_csv(FOOD_DATASET)

def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        return 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        return 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

def daily_calorie_needs(bmr, activity_level):
    factors = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Extra Active": 1.9,
    }
    return bmr * factors[activity_level]
