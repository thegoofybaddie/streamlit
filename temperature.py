import streamlit as st
import pickle
import sklearn

st.title('Revenue Prediction')
x = st.number_input('Input Temperature')
filename = 'model.pickle'
model = pickle.load(open(filename, "rb"))
if st.button('Predict'):
   model.predict(x_test)
  
