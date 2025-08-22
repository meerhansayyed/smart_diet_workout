import pandas as pd

def recommend_diet(goal, calorie_needs, budget, food_data, days=1):
    if goal == "Weight Loss":
        calorie_needs -= 500
    elif goal == "Muscle Gain":
        calorie_needs += 300
    
    df = food_data.sample(frac=1).reset_index(drop=True)
    selected_meals = []
    total_calories, total_cost = 0, 0

    for _, row in df.iterrows():
        if total_calories + row['Calories'] <= calorie_needs and total_cost + row['Cost(₹)'] <= budget:
            selected_meals.append(row)
            total_calories += row['Calories']
            total_cost += row['Cost(₹)']
        
        if total_calories >= (0.9 * calorie_needs):
            break

    meals_df = pd.DataFrame(selected_meals)

    if days == 1:  # daily plan
        return meals_df, round(total_calories, 2), round(total_cost, 2)
    else:  # weekly plan
        weekly_plan = {}
        for day in range(1, days+1):
            df = food_data.sample(frac=1).reset_index(drop=True)
            selected_meals, total_calories, total_cost = [], 0, 0
            for _, row in df.iterrows():
                if total_calories + row['Calories'] <= calorie_needs and total_cost + row['Cost(₹)'] <= budget:
                    selected_meals.append(row)
                    total_calories += row['Calories']
                    total_cost += row['Cost(₹)']
                if total_calories >= (0.9 * calorie_needs):
                    break
            weekly_plan[f"Day {day}"] = {
                "meals": pd.DataFrame(selected_meals),
                "calories": round(total_calories, 2),
                "cost": round(total_cost, 2)
            }
        return weekly_plan
