import streamlit as st
import pickle
import pandas as pd

# Load data
medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend medicines
def recommend(medicine):
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
    return recommended_medicines

# Streamlit app
st.title("MediMatch👨🏼‍⚕️")

# Dropdown for selecting medicine
selected_medicine_name = st.selectbox("Select a Medicine:", medicines['Drug_Name'].values)

# Button to get recommendations
if st.button("Recommend"):
    recommendations = recommend(selected_medicine_name)
    
    # Display recommendations
    st.write(f"Recommended Medicines for **{selected_medicine_name}**:")
    for med in recommendations:
        st.write(f"- {med}")
