import streamlit as st

def convert_text(text):
    # Replace each new line or empty line with <br/>
    return text.replace('\n', '<br/>')

st.title("new lines to `<br/>`")

with st.form(key='my_form', border=False):
    input_text = st.text_area("Input Text", height=300)
    convert_button = st.form_submit_button("Convert")

if convert_button:
    output_text = convert_text(input_text)
    st.session_state['output'] = output_text

output_text = st.text_area("Converted Text", height=300, value=st.session_state.get('output', ''))
