import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

# Creating interface.
st.title("Taxi Price Estmator")
trip=st.number_input("Total Distance in km",step=0.1)
time=['Afternoon','Evening','Morning','Night']
time_day=st.selectbox("Choose time of day",time)
day=['Weekday', 'Weekend']
week=st.selectbox("When are you planning to travel?",day)
passenger=st.number_input("Number of passengers: ")
traffic=st.radio("Current Traffic Conditions: ",['High','Low','Medium'])
weather=st.selectbox("Weather:",['Clear','Rain','Snow'])
base=st.number_input("Base_Fare:")
per_km=st.number_input("Enter per KM rate:")
per_min=st.number_input("Enter per min rate:")
trip_duration=st.number_input("Trip Duration in Minutes:")



# Load the model
model=joblib.load(r'C:\\Users\\rnkha\\OneDrive\\Desktop\\Projects\\taxi_price\\taxi_model.joblib')

# Creating DataFrame
features={'Trip_Distance_km':trip, 'Time_of_Day':time_day, 'Day_of_Week':week, 'Passenger_Count':passenger,
       'Traffic_Conditions':traffic, 'Weather':weather, 'Base_Fare':base, 'Per_Km_Rate':per_km,
       'Per_Minute_Rate':per_min, 'Trip_Duration_Minutes':trip_duration}
features=pd.DataFrame(features,index=[0])

# Label Encoding
categorical_data=['Time_of_Day','Day_of_Week','Traffic_Conditions','Weather']
for i in categorical_data:
    daytime={'Afternoon':0,'Evening':1,'Morning':2,'Night':3}
    weeks={'Weekday':0, 'Weekend':1}
    traffics={'Low':1, 'High':0, 'Medium':2}
    weathers={'Clear':0,'Rain':1, 'Snow':2}
    if i=='Time_of_Day':
          features[i]=features[i].map(daytime)
    elif i=='Day_of_Week':
         features[i]=features[i].map(weeks)
    elif i=='Traffic_Conditions':
         features[i]=features[i].map(traffics)
    elif i=='Weather':
         features[i]=features[i].map(weathers)
 
# if button clicked.
if st.button("Estimate"):
     # scaling
     ss=joblib.load(r"C:\\Users\\rnkha\\OneDrive\\Desktop\\Projects\\taxi_price\\scaling.joblib")
     scaled_features=ss.transform(features)
     scaled_features=pd.DataFrame(scaled_features)
     # Predicting
     Price=model.predict(scaled_features)
     st.write("Your total taxi fare is:",Price[0])