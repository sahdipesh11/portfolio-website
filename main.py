import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Dipesh Sah")
    content = """
    This is going to be filled with contents related to me and my professional career. 
    My achievements, experiences, and whatever else I see fit to show in that section.
    The information provided here should be focused on selling myself as a prospective employee.
    """
    st.info(content)
