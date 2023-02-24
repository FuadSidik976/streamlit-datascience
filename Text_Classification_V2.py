import pickle
import streamlit as st


# Membaca model
model976 = pickle.load(open('model976.sav','rb'))

# judul web
st.title('Buat ujian')

Message = st.text_input ('input text spam')
#Category = st.text_input ('input text category')

# code untuk prediksi
model_diagnosis = ''

# membuat tombol untuk prediksi
#if st.button('Test cek spam ') :
	#model_prediction = model976.predict([[Message, Category]])

	#if(model_prediction[0] == 1):
		#model_diagnosis = 'Text pesan tidak spam'
	#else :
		#model_diagnosis = 'Text pesan  spam'
	#st.success(model_diagnosis)

if st.button('Classify'):
    model_prediction = model976.predict([Message])
    st.write('Prediction:', data[prediction[0]])
    st.success(model_diagnosis)

