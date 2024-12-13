import streamlit as st
st.title('This is a simple application')
num1 = st.number_input('Enter number',min_value=1,step=1)
if st.button('Even/odd'):
    if num1 % 2 == 0:
        st.success('Even')
    else:
        st.error('odd number')