import streamlit as st
import requests
import json
from requests.auth import HTTPBasicAuth
import pandas as pd

roleData = ""

def getuserRoles(epmurl, epmuname, epmpwd, apiheaders):
    st.write("Invoking the REST API....")
    st.write("User name is : ", epmuname)
    st.write("Password is : ", epmpwd)
    reqResponse = requests.get(epmurl, auth=HTTPBasicAuth(epmuname, epmpwd), headers=apiheaders)
    if reqResponse.status_code == 200:
        roleData = json.loads(reqResponse.text)
        st.write("REST API call successful")
        # prompt: print the dataSlice
        st.write(json.dumps(roleData, indent=4, sort_keys=True))
    else:
        st.write(reqResponse.status_code)
    
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
epmURL = st.text_input("EPM URL: ",disabled=disableinput)
uName = st.text_input("EPM Username: ",disabled=disableinput)
uPwd = st.text_input("EPM Password: ",disabled=disableinput,type="password")

# variables to pass login information while invoking the REST API

st.write("User name is : ", uName)
st.write("Password is : ", uPwd)
st.write("URL is : ", epmURL)

#uName = ""  #provide user name
#uPwd = "" #provide password
#roleData = ""

requestURL = epmURL + "/interop/rest/security/v2/report/roleassignmentreport/user" #provide correct url
st.write("REST End Point is : ", requestURL)
reqHeaders = {}
reqHeaders['Content-Type'] = 'application/json'

st.button("Get Data", type="primary", on_click=getuserRoles(epmurl=requestURL, epmuname=uName, epmpwd=uPwd, apiheaders=reqHeaders))

st.divider()
st.subheader("Raw Data")
