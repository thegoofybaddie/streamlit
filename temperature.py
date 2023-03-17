import streamlit as st
import pickle
import sklearn
import numpy as np

st.title('Revenue Prediction')
x = st.number_input('Input Temperature')
filename = 'model.pickle'
model = pickle.load(open(filename, "rb"))
if st.button('Predict'):
   x = np.array(x).reshape(-1,1)
   result = model.predict(x)
   st.caption('Revenue Prediction')
   st.success(f'{result})
 
