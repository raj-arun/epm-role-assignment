import streamlit as st

st.title("🎈 EPM Role Assignment Report")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

role = st.radio(
    "Do you have Service Adminstrator Role?",
    ["Yes", "No"],)

if role == "Yes":
    st.write("You can use this service".)
else:
    st.write("You cannot user this serivice.")

st.text_input("EPM URL: ")
st.text_input("EPM Username: ")
st.text_input("EPM Password: ")

st.subheader("Raw Data")
