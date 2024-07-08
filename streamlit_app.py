import streamlit as st
import requests
import json
from requests.auth import HTTPBasicAuth
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer #display Pygwalker

roleData = ""

def getuserRoles(epmurl, epmuname, epmpwd, apiheaders):
    col1, col2, col3, col4 = st.columns(4)
    with st.container():
        #st.write("User name is : ", epmuname)
        st.write("Invoking the REST API....")
    
        reqResponse = requests.get(epmurl, auth=HTTPBasicAuth(epmuname, epmpwd), headers=apiheaders)
    
        if reqResponse.status_code == 200:
            roleData = json.loads(reqResponse.text)
            st.write("REST API call successful")
            rowList = []
            for index, value in enumerate(roleData["details"]):
                rowList.append([value["firstname"],value["lastname"],value["userlogin"],value["roles"][0]["rolename"]])
    
            df = pd.DataFrame(rowList, columns = ['First Name', 'Last Name','Login Name','Role'])
            st.subheader("Raw Data")
            st.write(df)
            st.subheader("Chart Area")
            df_count = df[['Role','First Name']].groupby("Role").count()
            st.write(df_count)
            #st.bar_chart(data=df_count, x="Role", y="First Name", x_label="Role", y_label="Count", color=None, horizontal=True, use_container_width=True)
            st.divider()
            st.bar_chart(data=df_count, color=None, x_label="Count", y_label="Role", horizontal=True, height=200)
            st.divider()
            
            pyg_app = StreamlitRenderer(df)
     
            pyg_app.explorer()
        else:
            st.write(reqResponse.status_code)
    
st.title("🎈 EPM Role Assignment Report")
st.write(
    "Enter the URL, User name and password. The app will generate the list of users along with their roles"
)

st.divider()

with st.container():
    st.write("This is inside the container")
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
    
    with st.form("epm form"):
        epmURL = st.text_input("EPM URL: ",disabled=disableinput)
        uName = st.text_input("EPM Username: ",disabled=disableinput)
        uPwd = st.text_input("EPM Password: ",disabled=disableinput,type="password")
        submitted = st.form_submit_button("Submit",)
        if submitted:
            st.write("URL is : ", epmURL)
            requestURL = epmURL + "/interop/rest/security/v2/report/roleassignmentreport/user" #provide correct url
            st.write("REST End Point is : ", requestURL)
            reqHeaders = {}
            reqHeaders['Content-Type'] = 'application/json'
            getuserRoles(epmurl=requestURL, epmuname=uName, epmpwd=uPwd, apiheaders=reqHeaders)

#st.button("Get Data", type="primary", on_click=getuserRoles(epmurl=requestURL, epmuname=uName, epmpwd=uPwd, apiheaders=reqHeaders))

st.divider()
rowList = []

st.write(roleData)
