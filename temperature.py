import streamlit as st

st.title('Revenue Prediction')
x = st.number_input('Input Temperature')
filename = 'model.pickle'
model = pickle.load(open(filename, "rb"))
if st.button('Predict'):
   pickled_model.predict(X_test)
  
