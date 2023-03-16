import streamlit as st
import pickle

st.title('Revenue Prediction')
a = st.number_input('Revenue Prediction')
if st.button('Predict'):
  filename = 'model.pickle'
  pickle.dump(model, open(filename, "wb"))
  model = pickle.load(open(filename, "rb")) 
  
