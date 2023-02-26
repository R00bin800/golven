import streamlit as st

st.set_page_config(page_title="Welcome to wave site")
st.title("Welcome to wave site")
#st.subheader("Feed me your XLSX file")
st.markdown(
"Welcome to this website created by Robin van Marle.  \n"
"Using the sidebar you can generate some wave data and then analyze the data."
)
st.sidebar.markdown("# Home page")