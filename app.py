import streamlit as st
import json
import random

# Load style.css
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="HalalGPT", page_icon="🕌", layout="wide")

# Load ingredient data from islamic_data.json
try:
    with open("islamic_data.json", "r", encoding="utf-8") as f:
        ingredients_data = json.load(f)
except FileNotFoundError:
    st.error("❌ File 'islamic_data.json' not found.")
    st.stop()

# Random Fatwa of the Day
fatwas = [
    "Avoid doubtful matters, for whoever avoids doubtful matters clears himself in regard to his religion. — Prophet Muhammad ﷺ",
    "That which is Halal is clear and that which is Haram is clear. — Sahih Bukhari",
    "Allah has permitted the pure and prohibited the impure. — Qur’an 7:157",
    "The lawful is clear and the unlawful is clear, and between them are doubtful matters. — Sahih Muslim"
]
random_fatwa = random.choice(fatwas)

# INTRO PAGE
st.markdown(f"""
<div class="hero" id="intro">
    <h1>HalalGPT</h1>
    <blockquote>
        “Verily, Allah has permitted the pure and prohibited the impure.”<br>
        <span>— Qur’an 7:157</span>
    </blockquote>
    <p class="intro">HalalGPT is your AI-powered assistant to instantly verify ingredients and products using verified Islamic sources.</p>
    <div class="fatwa-box">
        <em>📘 Fatwa of the Day:</em><br>
        <strong>"{random_fatwa}"</strong>
    </div>
    <a href="#app" class="scroll-button">🔽 Enter HalalGPT</a>
</div>
""", unsafe_allow_html=True)

# Scroll anchor
st.markdown("<div id='app'></div>", unsafe_allow_html=True)

# SECTION TITLE
st.markdown("<h2 class='section-title'>Ingredient Checker</h2>", unsafe_allow_html=True)

# CATEGORY DROPDOWN
def get_categories():
    cats = sorted(set(item.get("category", "Uncategorized") for item in ingredients_data))
    cats.insert(0, "All Categories")
    return cats

col1, col2 = st.columns([3, 2])

with col1:
    user_input = st.text_input("🔍 Search Ingredient (e.g., Oreo, Gelatin):")

with col2:
    selected_category = st.selectbox("📂 Category Filter", get_categories())

# FILTER RESULTS
def filter_results(query, category):
    results = []
    for item in ingredients_data:
        name_match = query.lower() in item["ingredient"].lower() if query else False
        category_match = category == "All Categories" or item["category"] == category
        if name_match and category_match:
            results.append(item)
    return results

results = filter_results(user_input, selected_category)

# DISPLAY RESULTS
if user_input:
    if results:
        for result in results:
            status = result["status"].lower()
            badge_class = f"status-{status}"

            st.markdown(f"""
            <div class='result-page'>
                <div class='result-header'>
                    <h2>{result["ingredient"]}</h2>
                    <span class='{badge_class}'>{result["status"].upper()}</span>
                </div>
                <div class='result-body'>
                    <p><strong>Explanation:</strong><br>{result["explanation"]}</p>
                    <hr>
                    <p><strong>Category:</strong> {result["category"]}</p>
                    <p><strong>Reference:</strong> <a href="{result["reference"]}" target="_blank">{result["reference"]}</a></p>
                    <div class='feedback-box'>
                        <p>Was this helpful? 🙏</p>
                        <span class='feedback'>👍</span>
                        <span class='feedback'>👎</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No matching results found.")
else:
    st.markdown("""
    <div class='no-result-msg'>
        <p>🕋 Start by searching for an ingredient above.</p>
        <p style='color:gold'>“Eat of what is lawful and pure.” — Qur’an 2:168</p>
    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<footer>
    <p>Part of the <strong>ZAYNOVA</strong> mission — merging modern AI with timeless Islamic ethics.</p>
    <p class="author-credit">Built by <strong>ZAYAN ALI ADIL</strong> 💫</p>
</footer>
""", unsafe_allow_html=True)
