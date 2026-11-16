import streamlit as st

st.title("This is title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.title("Dashboard", icon=":material/dashboard:")

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.write("Streamlit is an open-source app framework that is a breeze to get started with. Just install it like any other Python library")

agree = st.checkbox("I agree with kashish")

if agree:
    st.write("Great!")


#radio

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)

st.write("You selected:", genre)

num1=st.number_input("Enter a number")
num2=st.number_input("Enter another number")

print("Then sum of two numbers is: ", num1+num2)

if st.button("Add"):
    st.write("Then sum of two numbers is: ", num1+num2)