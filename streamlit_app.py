import streamlit as st
import random

st.set_page_config(page_title="🎁 Your Discount", page_icon="💸", layout="centered")

# Generate a random discount
discount = random.randint(1, 5)

# Display result
st.title("🎉 Congratulations!")
st.header(f"🔥 You've won a {discount}% discount!")

st.markdown("Use this discount at checkout. Valid only once!")
