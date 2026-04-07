import streamlit as st
import time
st.title('streamlit 超入門')

st.write('INteractive Widgets')



text = st.text_input('あなたの趣味を教えて下さい')

'あなたの趣味：', text

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

# if st.checkbox('show Image'):
#   img = Image.open('sample.jpg')
#   st.image(img, caption='sample', use_column_width=True)