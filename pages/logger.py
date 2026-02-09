import streamlit as st
from models.food import Food
from database.db_manager import init_database

init_database()

st.title("🍎 Ajouter un aliment")

# app.py ou pages/1_📝_Logger.py
import streamlit as st
from models.food import Food
from database.db_manager import init_database

# Init DB au démarrage
init_database()

st.title("🍎 Ajouter un aliment")

with st.form("add_food_form"):
    name = st.text_input("Nom de l'aliment")
    col1, col2 = st.columns(2)
    
    with col1:
        calories = st.number_input("Calories (pour 100g)", min_value=0)
        protein = st.number_input("Protéines (g)", min_value=0.0, step=0.1)
    
    with col2:
        carbs = st.number_input("Glucides (g)", min_value=0.0, step=0.1)
        fat = st.number_input("Lipides (g)", min_value=0.0, step=0.1)
    
    submitted = st.form_submit_button("Ajouter")
    
    if submitted and name:
        food = Food(name, calories, protein, carbs, fat)
        food.save()
        st.success(f"✅ {name} ajouté !")

# Afficher les aliments existants
st.subheader("Aliments dans la base")
foods_df = Food.get_all()
st.dataframe(foods_df)