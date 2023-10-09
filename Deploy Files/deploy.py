import streamlit as st
import numpy as np
import pickle
import gzip

# Load the compressed pickle file for the random forest model
with gzip.open("compressed_xgb_grid.pkl.gz", "rb") as file:
    pickled_model = pickle.load(file)

# Load the scaler
with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)


# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1

# Initialize input variables with default values
(
    age,
    sex,
    education,
    cigs_per_day,
    bp_meds,
    prevalent_stroke,
    prevalent_hyp,
    diabetes,
) = (30, "Male", 1, 0, "No", "No", "No", "No")

# Function to reset the step to 1


def reset_step():
    st.session_state.step = 1


# Define input fields
st.title(":blue[Heart Disease] :red[Risk] :blue[Prediction]")
st.write("**Please provide the following information**")

# Step 1: Demographic data
if st.session_state.step == 1:
    st.write("## :green[Demographic Data]")
    age = st.slider("**Age**", 1, 100, age)
    sex = st.radio("**Sex**", ["Male", "Female"])
    education = st.selectbox("**Education Level**", [1, 2, 3, 4], education)

    # Add Behavioral Data button
    if st.button("Add Behavioral Data"):
        st.session_state.step = 2

# Step 2: Behavioral Data
if st.session_state.step == 2:
    st.write("## :green[Behavioral Data]")
    cigs_per_day = st.number_input(
        "**Cigarettes Per Day**", min_value=0, max_value=50, value=cigs_per_day, step=1
    )

    # Add Medical History button
    if st.button("Add Medical History"):
        st.session_state.step = 3

# Step 3: Medical history
if st.session_state.step == 3:
    st.write("## :green[Medical History]")
    bp_meds = st.radio("**Taking Blood Pressure Medication?**", ["Yes", "No"])
    prevalent_stroke = st.radio("**Prevalent Stroke?**", ["Yes", "No"])
    prevalent_hyp = st.radio("**Prevalent Hypertension?**", ["Yes", "No"])
    diabetes = st.radio("**Diabetes?**", ["Yes", "No"])

    # Add Medical Current button
    if st.button("Add Medical Current"):
        st.session_state.step = 4

# Step 4: Medical current and predict button
if st.session_state.step == 4:
    st.write("## :green[Medical Current]")
    tot_chol = st.number_input(
        "**Total Cholesterol**", min_value=0.0, max_value=600.0, value=200.0, step=1.0
    )
    bmi = st.number_input(
        "**BMI**", min_value=10.0, max_value=50.0, value=25.0, step=0.1
    )
    heart_rate = st.slider("**Heart Rate**", 40, 150, 75)
    glucose = st.number_input(
        "**Glucose**", min_value=40.0, max_value=400.0, value=100.0, step=1.0
    )
    pulse_pressure = st.number_input(
        "**Pulse Pressure**", min_value=0.0, max_value=100.0, value=40.0, step=1.0
    )

    # Predict button
    if st.button(":green[Predict]"):
        # Convert sex, bp_meds, prevalent_stroke, prevalent_hyp, and diabetes to integers
        sex_int = 1 if sex == "Male" else 0
        bp_meds_int = 1 if bp_meds == "Yes" else 0
        prevalent_stroke_int = 1 if prevalent_stroke == "Yes" else 0
        prevalent_hyp_int = 1 if prevalent_hyp == "Yes" else 0
        diabetes_int = 1 if diabetes == "Yes" else 0

        # Create a numpy array with input values
        input_values = np.array(
            [
                age,
                education,
                sex_int,
                cigs_per_day,
                bp_meds_int,
                prevalent_stroke_int,
                prevalent_hyp_int,
                diabetes_int,
                tot_chol,
                bmi,
                heart_rate,
                glucose,
                pulse_pressure,
            ]
        )

        # Scale the input values using the loaded scaler
        scaled_values = scaler.transform(input_values.reshape(1, -1))

        # Make predictions
        prediction = pickled_model.predict(scaled_values)
        st.subheader(":green[Prediction Result]:")
        if prediction[0] == 1:
            st.write(":red[The model predicts that you have a risk of heart disease.]")
        else:
            st.write(
                ":green[The model predicts that you do not have a risk of heart disease.]"
            )

# Restart button
if st.button("Restart", key="restart"):
    reset_step()
