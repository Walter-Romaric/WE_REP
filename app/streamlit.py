import streamlit as st
# from fpdf import FPDF
import base64


st.set_page_config(
    page_title='Malaria Detection app',
    page_icon=':shark:',
    initial_sidebar_state="auto"
)

st.title('Malaria Rapid Screening')
# report_text = st.text_input('''Malaria was detected in this sample. Please correlate this
#                             result with the clinical presentation and contact a physician on call if you wish to
#                             discuss the result. Malaria is a notifiable disease and should be reported appropriately.
#                             ''')

st.write('''Malaria screening page
                            ''')
export_as_pdf = st.button("Generate a Report")

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

# if export_as_pdf:
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font('Arial', 'B', 16)
#     pdf.cell(40, 10, report_text)

#     html = create_download_link(pdf.output(dest="S").encode("latin-1"), "Laboratory Report")

#     st.markdown(html, unsafe_allow_html=True)
