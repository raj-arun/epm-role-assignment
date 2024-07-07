import streamlit as st

st.title("🎈 EPM Role Assignment Report")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.divider()

role = st.radio(
    "Do you have Service Adminstrator Role?",
    ["Yes", "No"],)

if role == "Yes":
    st.write("You can use this service.")
    disableinput = False
else:
    st.write("You cannot user this serivice.")
    disableinput = True

st.divider()
st.text_input("EPM URL: ",disabled=disableinput)
st.text_input("EPM Username: ",disabled=disableinput)
st.text_input("EPM Password: ",disabled=disableinput)

st.divider()
st.subheader("Raw Data")
