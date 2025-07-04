import streamlit as st
import json
import random

st.set_page_config(page_title="HalalGPT", layout="wide")

# Load data
with open("islamic_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Split screen layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("<h1 class='glow'>HalalGPT</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='tagline'>“O mankind, eat from whatever is on earth [that is] lawful and pure.” — Quran 2:168</p>",
        unsafe_allow_html=True)
    st.markdown(
        "<p class='slogan'>Your AI Guide to Halal & Haram Ingredients</p>",
        unsafe_allow_html=True)

    if st.button("🔍 Enter HalalGPT"):
        st.session_state.entered = True

    st.markdown("---")
    st.markdown(
        "<p class='credit'>Made with 💚 by <strong>ZAYAN ALI ADIL</strong></p>",
        unsafe_allow_html=True)

with col2:
    st.image("https://i.imgur.com/EVQfhVi.png", use_column_width=True)

# Show search page if button clicked
if st.session_state.get("entered"):
    st.markdown("## 🧪 Ingredient Check")
    user_input = st.text_input(
        "Enter an ingredient, brand, or product name (e.g. Gelatin, Pepsi, etc.)"
    )

    if user_input:
        result = next((item for item in data
                       if item["ingredient"].lower() == user_input.lower()),
                      None)
        if result:
            st.success(f"**Status:** {result['status']}")
            st.markdown(f"**Explanation:** {result['explanation']}")
            st.markdown(f"**Category:** {result['category']}")
            st.markdown(f"**Reference:** {result['reference']}")
        else:
            st.error("Ingredient not found in the database.")

    st.markdown("---")
    st.markdown("### 📩 Submit a New Ingredient")
    new_ingredient = st.text_input("Suggest a new ingredient we should add:")
    if st.button("Submit"):
        st.success("JazakAllah! We'll review and add it soon, In Sha Allah.")

    st.markdown("---")
    st.markdown(f"### 🕋 Fatwa of the Day")
    random_fatwa = random.choice([
        "Consuming gelatin derived from non-Zabiha animals is considered haram. — Darul Ifta",
        "Alcohol-based flavorings in small amounts are not permissible in food. — Dr. Zakir Naik",
        "Always verify the source of enzymes and emulsifiers in processed foods. — Mufti Menk"
    ])
    st.info(random_fatwa)
