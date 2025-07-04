import streamlit as st
import json

# Load data
with open("islamic_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Custom styling
st.set_page_config(page_title="HalalGPT", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Fatwa of the day
fatwa_of_day = {
    "question": "Is it permissible to consume food with doubtful ingredients?",
    "answer": "Avoiding doubtful (shubuhat) matters is better for one’s faith. The Prophet ﷺ said: 'Leave that which makes you doubt for that which does not make you doubt.' (Tirmidhi)"
}

# Sidebar
with st.sidebar:
    st.image("https://i.imgur.com/N7oN6fG.png", width=180)  # Replace with your logo
    st.markdown("## HalalGPT 🍃")
    st.markdown("**Search any ingredient or product to know if it's Halal or Haram.**")
    st.markdown("---")
    st.markdown("### Fatwa of the Day 📜")
    st.write(f"**Q:** {fatwa_of_day['question']}")
    st.write(f"**A:** {fatwa_of_day['answer']}")
    st.markdown("---")
    st.markdown("Made with ❤️ for the Ummah")

# Main
st.markdown("<h1 class='glow-text'>🔎 HalalGPT</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='tagline'>“Eat of what is lawful and pure on the earth...” — [Qur'an 2:168]</h3>", unsafe_allow_html=True)

query = st.text_input("Type any ingredient, food item, or product name:")

if query:
    result = next((item for item in data if query.lower() in item["ingredient"].lower()), None)
    if result:
        st.markdown(f"""
            <div class='result-box'>
                <h2>{result['ingredient']}</h2>
                <p><strong>Status:</strong> <span class='status-{result['status'].lower()}'>{result['status']}</span></p>
                <p><strong>Explanation:</strong> {result['explanation']}</p>
                <p><strong>Reference:</strong> {result['reference']}</p>
                <p><strong>Category:</strong> {result['category']}</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("❌ No matching ingredient found. Try another search.")

# Footer
st.markdown("<hr><center><span class='footer-text'>© 2025 HalalGPT | Built by <strong>ZAYAN ALI ADIL</strong></span></center>", unsafe_allow_html=True)
    
