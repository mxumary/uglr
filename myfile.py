# testing form

# source: https://guides.ll.georgetown.edu/bluebook/citing-cases

import streamlit as st

# having trouble with the underlining...

with st.form("my_form"):
    case_name = st.text_input('Case Name')
    vol_num = st.text_input('Volume Number')
    reporter = st.text_input('Reporter abbreviation')
    case_page = st.text_input('First page of case')
    pinpoint = st.text_input('Pinpoint')
    court_name = st.text_input('Court')
    decision_yr = st.text_input('Decision Year')
    # test_string = 'hello'
    # st.write("Inside the form")
    # slider_val = st.slider("Form slider")
    # checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(case_name + ', ' + vol_num + ' ' + reporter + ' ' + case_page + ', ' + pinpoint
        + ' (' + court_name + ' ' + decision_yr + ')')
        # st.write('here is the text input: ' + text_input)
        # st.write("slider", slider_val, "checkbox", checkbox_val)
        # st.markdown('Streamlit is **_really_ cool**.')
        # st.markdown('**_' + test_string + '_**')

st.write("Outside the form")
st.markdown('Streamlit is **_really_ cool**.')