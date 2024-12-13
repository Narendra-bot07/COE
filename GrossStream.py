import streamlit as st
st.title('Bank Streamlit')
salary = st.number_input('Enter your salary',min_value=0,step=1)
gs,hra,da = 0,0,0
if st.button('calculate gross salary'):
    if salary<=10000:
        hra = (67/100)*salary
        da = (73/100)*salary
    elif salary<20000:
        hra = (69/100)*salary
        da = (76/100)*salary
    else:
        hra = (73/100)*salary
        da = (80/100)*salary
gs = hra + da +salary
st.success(f" Gross salary:{gs:.2f} ")


