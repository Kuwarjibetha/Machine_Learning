import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn


st.set_page_config(page_title = "Prediction", page_icon ="🪄️")


st.title('Page 1')

with open('df (1).pkl','rb') as file:
   df = pickle.load(file)

with open('pipeline (1).pkl','rb') as file:
   pipeline = pickle.load(file)

# st.dataframe(df)



# ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
#        'agePossession', 'built_up_area', 'servant room', 'store room',
#        # 'furnishing_type', 'luxury_category', 'floor_category']

st.header('Enter Your Inputs')
# Property Type
property_type = st.selectbox('# Property Type',['flat','house'])
 # sector
sector = st.selectbox('Sector',sorted(df['sector'].unique()))
# bedroom
bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique())))

#bathroom
bathroom = float(st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique())))

# balcony
balcony = st.selectbox('Number of Balcony',sorted(df['balcony'].unique()))

# agePossession
Property_Age = st.selectbox('Property Age',sorted(df['agePossession'].unique()))

# built_up_area
built_up_area = float(st.number_input('Built Up Area'))

# Servant Room
servant_room = float(st.selectbox('Servant Room',[0.0, 1.0]))
# store_room
store_room = float(st.selectbox('Store Room',[0.0, 1.0]))

# furnishing_type

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique()))
# luxury_category
luxury_category = st.selectbox('Luxury Category ',sorted(df['luxury_category'].unique()))

# floor_category

floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique()))

if st.button('Predict'):
    # form a data frame
    data = [[property_type, sector, bedrooms, bathroom, balcony,
             Property_Age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    # st.dataframe(one_df)
    pred = np.expm1(pipeline.predict(one_df))[0]

    low = pred - 0.22
    high = pred + 0.22

    # display

    st.text('The Price of your Property is in Between {} Cr to {}Cr'.format(round(low,2),round(high,2)))



