import streamlit as st
import pandas as pd
import pickle 

model = pickle.load(open('Frontend/Model/model.pkl', 'rb'))
st.markdown(
    """
    <link rel="stylesheet" type="text/css" href="styles.css">
    """,
    unsafe_allow_html=True
)

st.title("Dubai Property Evaluation")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Clustering", "Classification", "Regression"))

if page == "Home":
    st.header("Welcome to the Home Page")
    # Add content for the home page here

elif page == "Clustering":
    st.header("Clustering Page")

elif page == "Classification":
    st.header("Classification Page")
    # Add content for the classification page here

elif page == "Regression":
    st.header("Regression Page")
    # Add content for the regression page here

st.sidebar.title("Property Features")  


# Collect user input
price = st.number_input("Price", min_value=0)
size_in_sqft = st.number_input("Size in Sqft", min_value=0)
no_of_bedrooms = st.number_input("No of Bedrooms", min_value=0)
no_of_bathrooms = st.number_input("No of Bathrooms", min_value=0)

st.sidebar.title("Amenities")


maid_room = st.radio("Maid Room", ["Available", "N/A"])
unfurnished = st.radio("Unfurnished", ["Yes", "No"])
balcony = st.radio("Balcony", ["Available", "N/A"])
barbecue_area = st.radio("Barbecue Area", ["Available", "N/A"])
built_in_wardrobes = st.radio("Built in Wardrobes", ["Available", "N/A"])
central_ac = st.radio("Central A/C", ["Available", "N/A"])
childrens_play_area = st.radio("Children's Play Area", ["Available", "N/A"])
childrens_pool = st.radio("Children's Pool", ["Available", "N/A"])
concierge = st.radio("Concierge", ["Available", "N/A"])
covered_parking = st.radio("Covered Parking", ["Available", "N/A"])
kitchen_appliances = st.radio("Kitchen Appliances", ["Available", "N/A"])
lobby_in_building = st.radio("Lobby in Building", ["Available", "N/A"])
maid_service = st.radio("Maid Service", ["Available", "N/A"])
networked = st.radio("Networked", ["Yes", "No"])
pets_allowed = st.radio("Pets Allowed", ["Yes", "No"])
private_garden = st.radio("Private Garden", ["Available", "N/A"])
private_gym = st.radio("Private Gym", ["Available", "N/A"])
private_jacuzzi = st.radio("Private Jacuzzi", ["Available", "N/A"])
private_pool = st.radio("Private Pool", ["Available", "N/A"])
security = st.radio("Security", ["Available", "N/A"])
shared_gym = st.radio("Shared Gym", ["Available", "No"])
shared_pool = st.radio("Shared Pool", ["Available", "No"])
shared_spa = st.radio("Shared Spa", ["Available", "No"])
study = st.radio("Study", ["Available", "N/A"])
vastu_compliant = st.radio("Vastu Compliant", ["Yes", "No"])
view_of_landmark = st.radio("View of Landmark", ["Yes", "No"])
view_of_water = st.radio("View of Water", ["Yes", "No"])
walk_in_closet = st.radio("Walk in Closet", ["Available", "N/A"])



if st.button("Predict"):
    # Collect user inputs
    user_input = {
        "Price": price,
        "Size in Sqft": size_in_sqft,
        "No of Bedrooms": no_of_bedrooms,
        "No of Bathrooms": no_of_bathrooms,
        "Maid Room": 1 if maid_room == "Available" else 0,
        "Unfurnished": 1 if unfurnished == "Yes" else 0,
        "Balcony": 1 if balcony == "Available" else 0,
        "Barbecue Area": 1 if barbecue_area == "Available" else 0,
        "Built in Wardrobes": 1 if built_in_wardrobes == "Available" else 0,
        "Central A/C": 1 if central_ac == "Available" else 0,
        "Childrens Play Area": 1 if childrens_play_area == "Available" else 0,
        "Childrens Pool": 1 if childrens_pool == "Available" else 0,
        "Concierge": 1 if concierge == "Available" else 0,
        "Covered Parking": 1 if covered_parking == "Available" else 0,
        "Kitchen Appliances": 1 if kitchen_appliances == "Available" else 0,
        "Lobby in Building": 1 if lobby_in_building == "Available" else 0,
        "Maid Service": 1 if maid_service == "Available" else 0,
        "Networked": 1 if networked == "Yes" else 0,
        "Pets Allowed": 1 if pets_allowed == "Yes" else 0,
        "Private Garden": 1 if private_garden == "Available" else 0,
        "Private Gym": 1 if private_gym == "Available" else 0,
        "Private Jacuzzi": 1 if private_jacuzzi == "Available" else 0,
        "Private Pool": 1 if private_pool == "Available" else 0,
        "Security": 1 if security == "Available" else 0,
        "Shared Gym": 1 if shared_gym == "Available" else 0,
        "Shared Pool": 1 if shared_pool == "Available" else 0,
        "Shared Spa": 1 if shared_spa == "Available" else 0,
        "Study": 1 if study == "Available" else 0,
        "Vastu Compliant": 1 if vastu_compliant == "Yes" else 0,
        "View of Landmark": 1 if view_of_landmark == "Yes" else 0,
        "View of Water": 1 if view_of_water == "Yes" else 0,
        "Walk in Closet": 1 if walk_in_closet == "Available" else 0
    }

    # Preprocess user input if needed

    # Perform the prediction using your model
    prediction = model.predict([list(user_input.values())])

    # Display the prediction result
    st.write("Prediction:", prediction)
