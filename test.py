import streamlit as st
import pandas as pd
import os

# Create a title for the app
st.title("User Data Collection App")

# Create a form with input fields
with st.form("user_data_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    height = st.number_input("Height (cm)", min_value=0, step=1)
    weight = st.number_input("Weight (kg)", min_value=0, step=1)
    submit_button = st.form_submit_button("Submit")

# Define the CSV file path
csv_file = "user_data.csv"

# Check if the form has been submitted
if submit_button:
    # Create a dictionary to store the user data
    user_data = {"Name": name, "Age": age, "Height": height, "Weight": weight}

    # Check if the CSV file exists
    if not os.path.exists(csv_file):
        # Create a new CSV file with the header row
        pd.DataFrame(columns=["Name", "Age", "Height", "Weight"]).to_csv(csv_file, index=False)

    # Append the new user data to the CSV file
    pd.DataFrame([user_data]).to_csv(csv_file, mode="a", header=False, index=False)

    # Display a success message
    st.success("Data submitted successfully!")

# Display a table with the collected user data
if os.path.exists(csv_file):
    user_data_df = pd.read_csv(csv_file)
    st.dataframe(user_data_df)
else:
    st.write("No data collected yet!")
