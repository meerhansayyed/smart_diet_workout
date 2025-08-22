import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import os

# ----------------- Sample Weekly Meal Data -----------------
meals = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Breakfast": ["Oats + Milk", "Egg Whites + Toast", "Poha", "Upma", "Smoothie", "Idli + Sambar", "Paratha"],
    "Lunch": ["Chicken + Rice", "Paneer + Roti", "Fish + Rice", "Dal + Roti", "Rajma + Rice", "Chole + Roti", "Veg Pulao"],
    "Snack": ["Nuts", "Fruit", "Protein Bar", "Buttermilk", "Boiled Egg", "Sprouts", "Yogurt"],
    "Dinner": ["Soup + Roti", "Paneer Curry", "Grilled Fish", "Dal Khichdi", "Vegetable Curry", "Chicken Soup", "Salad"],
    "Calories": [1800, 1750, 1600, 1700, 1650, 1850, 1500],
    "Protein": [120, 110, 100, 105, 95, 125, 90],
    "Carbs": [220, 210, 200, 205, 190, 230, 180],
    "Fat": [50, 55, 45, 48, 52, 60, 40],
    "Cost": [200, 180, 150, 160, 170, 220, 140]
}

df = pd.DataFrame(meals)

# ----------------- Show Weekly Summary -----------------
avg_calories = df["Calories"].mean()
total_cost = df["Cost"].sum()

print("Average Calories per Day:", avg_calories)
print("Total Weekly Cost:", total_cost)

# ----------------- Plot Pie Chart for Each Day -----------------
for i in range(len(df)):
    macros = [df.loc[i, "Protein"], df.loc[i, "Carbs"], df.loc[i, "Fat"]]
    labels = ["Protein", "Carbs", "Fat"]

    plt.figure(figsize=(5,5))
    plt.pie(macros, labels=labels, autopct='%1.1f%%')
    plt.title(f"{df.loc[i, 'Day']} Macros")
    plt.savefig(f"day_{i+1}_macros.png")  # Save chart for PDF
    plt.close()

# ----------------- Export as PDF -----------------
pdf = SimpleDocTemplate("Weekly_Diet_Plan.pdf", pagesize=A4)
styles = getSampleStyleSheet()
content = []

content.append(Paragraph("Weekly Diet Plan", styles['Title']))
content.append(Spacer(1, 12))

for i in range(len(df)):
    content.append(Paragraph(f"<b>{df.loc[i, 'Day']}</b>", styles['Heading2']))
    table_data = [
        ["Breakfast", df.loc[i, "Breakfast"]],
        ["Lunch", df.loc[i, "Lunch"]],
        ["Snack", df.loc[i, "Snack"]],
        ["Dinner", df.loc[i, "Dinner"]],
        ["Calories", df.loc[i, "Calories"]],
        ["Protein", df.loc[i, "Protein"]],
        ["Carbs", df.loc[i, "Carbs"]],
        ["Fat", df.loc[i, "Fat"]],
        ["Cost (₹)", df.loc[i, "Cost"]],
    ]
    table = Table(table_data)
    content.append(table)
    content.append(Spacer(1, 12))

content.append(Paragraph(f"<b>Weekly Summary</b>", styles['Heading2']))
content.append(Paragraph(f"Average Calories per Day: {avg_calories:.2f}", styles['Normal']))
content.append(Paragraph(f"Total Weekly Cost: ₹{total_cost}", styles['Normal']))

pdf.build(content)

print("✅ Weekly Diet Plan PDF generated successfully!")
