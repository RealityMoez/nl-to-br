import streamlit as st

def convert_text(text):
    # Replace each new line or empty line with <br/>
    return text.replace('\n', '<br/>')

st.title("new lines to `<br/>`")

with st.form(key='my_form', border=False):
    input_text = st.text_area("Input Text", height=300)
    convert_button = st.form_submit_button("Convert")

output_text_area = st.empty()

if convert_button:
    output_text = convert_text(input_text)
    output_text_area.text_area("Converted Text", height=300, value=output_text, key='output')
else:
    output_text_area.text_area("Converted Text", height=300, value=st.session_state.get('output', ''), key='output')
