import streamlit as st
project = st.number_input('Enter project marks ',min_value=0, max_value=100)
internal = st.number_input('Enter internal marks ',min_value=0, max_value=100)
external = st.number_input('Enter external marks ',min_value=0, max_value=100)
if st.button('find grade'):
    if project<50:
        st.error(f"Failed in project\nscore {project}")
    if internal < 50:
        st.error(f"Failed in internal\nscore {internal}")
    if external < 50:
        st.error(f"Failed in external\nscore {external}")
    else:
        project = 0.7*project
        internal = 0.1*internal
        external = 0.2*external
        total = project + internal + external
        if total>90:
            st.success("A grade")
        elif total>=80:
            st.success("B grade")
        elif total>=50:
            st.success("C grade")

