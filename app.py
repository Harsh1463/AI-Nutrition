import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="AI Powered Nutrition Agent",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 AI Powered Nutrition Agent")

# Food Database
food_data = {
    "Food": ["Apple", "Banana", "Oats", "Rice", "Egg", "Milk", "Paneer", "Chicken Breast"],
    "Calories": [95, 105, 150, 206, 78, 122, 265, 165],
    "Protein": [0.5, 1.3, 5, 4.3, 6, 8, 18, 31],
    "Carbs": [25, 27, 27, 45, 0.6, 12, 6, 0],
    "Fat": [0.3, 0.4, 3, 0.4, 5, 5, 20, 3.6]
}

df = pd.DataFrame(food_data)

# Sidebar
st.sidebar.header("User Profile")

name = st.sidebar.text_input("Name")
age = st.sidebar.number_input("Age", 1, 100, 20)
weight = st.sidebar.number_input("Weight (kg)", 20, 200, 60)
height = st.sidebar.number_input("Height (cm)", 100, 250, 170)

goal = st.sidebar.selectbox(
    "Fitness Goal",
    ["Weight Loss", "Weight Gain", "Maintenance"]
)

condition = st.sidebar.selectbox(
    "Health Condition",
    ["None", "Diabetes", "Heart Disease", "Obesity"]
)

# BMI Section
st.header("📏 BMI Analysis")

if st.button("Calculate BMI"):
    bmi = weight / ((height / 100) ** 2)

    st.metric("BMI", f"{bmi:.2f}")

    if bmi < 18.5:
        st.warning("Underweight")
    elif bmi < 25:
        st.success("Normal Weight")
    elif bmi < 30:
        st.warning("Overweight")
    else:
        st.error("Obese")

# Diet Plan
st.header("🍽 Personalized Diet Plan")

if st.button("Generate Diet Plan"):

    st.success(f"Hello {name}")

    if goal == "Weight Loss":
        st.write("🍎 Breakfast: Oats + Fruits")
        st.write("🥗 Lunch: Salad + Vegetables")
        st.write("🍲 Dinner: Soup + Vegetables")

    elif goal == "Weight Gain":
        st.write("🥛 Breakfast: Milk + Banana")
        st.write("🍚 Lunch: Rice + Paneer")
        st.write("🍗 Dinner: Protein Rich Meal")

    else:
        st.write("🥗 Balanced Diet Plan")

    st.subheader("Health Advice")

    advice = {
        "None": "Maintain a balanced diet.",
        "Diabetes": "Avoid sugary foods and increase fiber intake.",
        "Heart Disease": "Reduce saturated fats and consume vegetables.",
        "Obesity": "Maintain calorie deficit and regular exercise."
    }

    st.info(advice[condition])

# Food Search
st.header("🔍 Nutrition Information Search")

food_name = st.text_input("Enter Food Name")

if st.button("Search Food"):

    result = df[df["Food"].str.lower() == food_name.lower()]

    if not result.empty:
        st.dataframe(result)
    else:
        st.error("Food not found")

# Meal Logger
st.header("📝 Meal Logger")

selected_foods = st.multiselect(
    "Select Foods Consumed Today",
    df["Food"].tolist()
)

if st.button("Analyze Meals"):

    meals = df[df["Food"].isin(selected_foods)]

    if not meals.empty:

        calories = meals["Calories"].sum()
        protein = meals["Protein"].sum()
        carbs = meals["Carbs"].sum()
        fat = meals["Fat"].sum()

        st.success("Meal Analysis Complete")

        st.write(f"Calories: {calories}")
        st.write(f"Protein: {protein} g")
        st.write(f"Carbs: {carbs} g")
        st.write(f"Fat: {fat} g")

        chart_data = pd.DataFrame({
            "Nutrient": ["Protein", "Carbs", "Fat"],
            "Value": [protein, carbs, fat]
        })

        fig, ax = plt.subplots()
        ax.bar(chart_data["Nutrient"], chart_data["Value"])
        ax.set_title("Nutrition Intake")

        st.pyplot(fig)

# Nutrition Database
st.header("📊 Nutrition Database")

st.dataframe(df)

st.markdown("---")
st.markdown("AI Powered Nutrition Agent | Streamlit Project")