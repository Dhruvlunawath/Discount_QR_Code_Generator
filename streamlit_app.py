import streamlit as st
import random

# Page setup
st.set_page_config(page_title="🎁 Your Discount", page_icon="💸", layout="centered")

# Generate random discount
discount = random.randint(1, 5)

# Display content
st.title("🎉 Congratulations!")
st.header(f"🔥 You've won a {discount}% discount!")
st.markdown("Use this discount at checkout. Valid only once!")

# Terms & conditions
st.markdown("---")
st.markdown(
    """
    **Terms & Conditions Apply**  
    - Offer not valid on 92.50 Silver Articles  
    - Offer not valid on pure silver 
    - One-time use only  
    - Cannot be combined with other offers
    """,
    unsafe_allow_html=True
)
