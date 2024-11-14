import streamlit as st
import pandas as pd

# Create some sample data (latitude and longitude)
data = {
    'Latitude': [37.7749, 34.0522, 40.7128],  # San Francisco, Los Angeles, New York
    'Longitude': [-122.4194, -118.2437, -74.0060]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Rename columns to match Streamlit's expected names
df = df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})

# Display the map
st.title("Map of the world with Shamhoon")
st.map(df)
