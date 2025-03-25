import streamlit as st
import joblib
import numpy as np
from PIL import Image
import base64
import numpy as np

price = joblib.load('HousePrice_pridiction.pkl')

with open('bghouse2.jpg','rb') as f:
    data=f.read()
imgs= base64.b64encode(data).decode()

css = f"""
    <style>
        [data-testid="stMain"]{{
            background-image:url('data:image/jpg;base64,{imgs}');
            background-repeat:no-repeat;
            background-size:cover;
        }}
        #house-price-prediction{{
            background:linear-gradient(to right,#0fe3b2,#8ed9c8,#011a14,#8ed9c8,#0fe3b2);
            color:transparent;
            background-clip:text;
            text-align:center;
            border:2px solid black;
            border-radius:5px;
        }}  
        [data-testid="stColumn"]{{
            display:flex;
            justify-content:center;
            align-items:center;
            color:#0fe3b2;
        }}  
        [data-testid="stVerticalBlockBorderWrapper"]{{
            width:100%;
        }}
        [data-testid="stHeadingWithActionElements"]{{
            color:#0fe3b2;
        }}
    </style>
"""
st.set_page_config('House price predict',layout='wide')
st.markdown(css,unsafe_allow_html=True)
st.header('House price prediction')

col1,col2= st.columns((1,1),gap='medium')

with col1:
    st.header('Check The Price Of Your Dream House.')
    st.write('Predict the price of house based on its specification.')

with col2:
    img = Image.open('house1.jpg')
    st.image(img,width=600)

with st.form("prediction_form"):
    c1,c2,c3,c4 = st.columns((1,1,1,1),gap='large')
    
    with c1:
        area = st.number_input(' House Area (sq ft):', min_value=0)

        brooms = st.number_input(' Bedrooms:', min_value=0)

        sto = st.number_input(' Stories:', min_value=0)

    with c2:
        bath = st.number_input(' Bathrooms:', min_value=0)

        main = st.radio(" Is the house on the main road?", ["Yes", "No"])
        main = 1 if main == "Yes" else 0

        guest = st.radio("Is guest room available?",['Yes','No'])
        guest = 1 if guest == 'Yes' else 0

    with c3:
        base = st.radio("Is basement available?",['Yes','No'])
        base = 1 if base == 'Yes' else 0

        hot = st.radio("Is hotwater available?",['Yes','No'])
        hot = 1 if hot == 'Yes' else 0

        air = st.radio("Is airconditioning available?",['Yes','No'])
        air = 1 if air == 'Yes' else 0
    
    with c4:
        park = st.number_input('No. of Parkings:',min_value=0)

        pre = st.radio("Is prefarea available?",['Yes','No'])
        pre = 1 if pre == 'Yes' else 0

        fur = st.radio("Is Fursished?",['Furnished','Semifurnished','Unfurnished'])
        if fur == 'Furnished':
            fur = 0
        elif fur == "Semifurnished":
            fur = 1
        else:
            fur = 2

    bb = st.form_submit_button("Predict")

    if(bb):
        arr = np.array([area,brooms,bath,sto,main,guest,base,hot,air,park,pre,fur])
        pp = price.predict([arr])
        st.success('Price Predicted')
        st.header(f'Price of your house is {pp}')