import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewing streamlit")
st.text(" back to text")
st.write("hekoo")

chai=st.selectbox("Your fav chai",['tea','redlab0le','taaza','brook'])
st.write("your fav chai {chai} , excellent choice")
st.success("Select wisely")

