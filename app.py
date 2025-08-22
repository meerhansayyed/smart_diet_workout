import streamlit as st
import pandas as pd
import sys, os

# Ensure project root is in sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.utils import calculate_bmr, daily_calorie_needs
from backend.diet import recommend_diet
from backend.workout import recommend_workout
from projects_paths import FOOD_DATASET

# ✅ Load dataset safely
food_data = pd.read_csv(FOOD_DATASET)

# -------------------------
# Streamlit UI
# -------------------------
st.title("🏋️ Smart Diet & Workout Recommender")

st.sidebar.header("Enter Your Details")

age = st.sidebar.number_input("Age", 15, 80, 22)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
height = st.sidebar.number_input("Height (cm)", 100, 220, 172)
weight = st.sidebar.number_input("Weight (kg)", 30, 150, 79)
goal = st.sidebar.selectbox("Goal", ["Weight Loss", "Muscle Gain", "Maintain"])
activity = st.sidebar.selectbox(
    "Activity Level", 
    ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"]
)
budget = st.sidebar.slider("Daily Food Budget (₹)", 50, 500, 100)
level = st.sidebar.selectbox("Workout Level", ["Beginner", "Intermediate", "Advanced"])

# -------------------------
# Generate Plan
# -------------------------
if st.sidebar.button("Generate Plan"):
    bmr = calculate_bmr(weight, height, age, gender)
    calories = daily_calorie_needs(bmr, activity)

    # Daily plan
    meals, final_calories, total_cost = recommend_diet(goal, calories, budget, food_data)
    workout_plan = recommend_workout(level, goal)

    st.subheader("🍽️ Recommended Diet Plan (Daily)")
    st.write(meals[["Food", "Calories", "Protein(g)", "Carbs(g)", "Fat(g)", "Cost(₹)"]])
    st.write(f"**Total Calories:** {final_calories} kcal")
    st.write(f"**Total Cost:** ₹{total_cost} (within budget ₹{budget})")

    st.subheader("💪 Recommended Workout Plan")
    for w in workout_plan:
        st.write(f"- {w}")

    # Weekly plan
    weekly_plan = recommend_diet(goal, calories, budget, food_data, days=7)

    st.subheader("📅 Weekly Diet Plan (Mon–Sun)")
    for day, details in weekly_plan.items():
        st.markdown(f"### 📆 {day}")
        st.write(details["meals"][["Food", "Calories", "Protein(g)", "Carbs(g)", "Fat(g)", "Cost(₹)"]])
        st.write(f"**Total Calories:** {details['calories']} kcal")
        st.write(f"**Total Cost:** ₹{details['cost']} (within budget ₹{budget})")
        st.markdown("---")
