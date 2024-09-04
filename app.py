from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os
import PyPDF2
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyDOO-L8kwzrUzYyxCTUBbpA7ggGyrf-WPw"))

model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

input_prompt = """ As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect, Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial in offering top-notch guidance for resume enhancement. Assign precise matching percentages based on the JD (Job Description) and meticulously identify any missing keywords with utmost accuracy. 
resume: {text} 
description: {id}
I want the response in the following structure: 
The first line indicates the percentage match with the job description (JD). 
The second line presents a list of missing keywords. 
The third section provides a profile summary. Mention the title for all the three sections. 
While generating the response put some space to separate all the three sections"""

st.set_page_config(page_title="ATS Resume Tracker", layout="wide")
avs.add_vertical_space(4)

col1, col2 = st.columns([3, 2])
with col1:
    st.title("Career Craft")
    st.markdown("<h2 style='color: SteelBlue;'> Navigate the job Market with Confidence!</h2>",unsafe_allow_html=True)
    st.markdown("""<p style='text-align: justify;'>
        CareerCraft, an ATS-Optimized Resume Analyzer is a cutting-edge project designed to revolutionize the job application process using advanced ATS (Applicant Tracking System) technology. This innovative system empowers job seekers by providing insights into their resumes' compatibility with job descriptions, highlighting missing keywords, and offering tailored profile summaries for optimal presentation to potential employers.
        </p>""", unsafe_allow_html=True)

with col2:
    st.image('https://i.pinimg.com/564x/fc/51/42/fc514289c5f44f58b777da04b38ae0f1.jpg', use_column_width=True)
avs.add_vertical_space(10)

col1, col2 = st.columns([3, 2])
with col2:
    st.markdown("<h1 style='color: Purple;'>Wide Range of Offerings</h1>", unsafe_allow_html=True)
    st.write('• ATS-Optimized Resume Analysis')
    st.write('• Resume Optimization')
    st.write('• Skill Enhancement')
    st.write('• Career Progression Guidance')
    st.write('• Tailored Profile Summaries')
    st.write('• Streamlined Application Process')
    st.write('• Personalized Recommendations')
    st.write('• Efficient Career Navigation')

with col1:
    img1 = Image.open("images/icon1.png")
    st.image(img1, use_column_width=True)

avs.add_vertical_space(5)

col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
    jd = st.text_area("**Paste the Job Description**")
    uploaded_file = st.file_uploader("**Upload Your Resume**", type="pdf", help="Please upload the pdf")
    submit = st.button("Submit")
    if submit:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_gemini_response(input_prompt)
            st.subheader(response)

with col2:
    img2 = Image.open("images/icon2.png")
    st.image(img2, use_column_width=True)

avs.add_vertical_space(10)

col1, col2 = st.columns([2, 3])
with col2:
    st.markdown("<h1 style='text-align: center;color: Orange '>FAQ</h1>", unsafe_allow_html=True)
    st.write("**Question:** How does CareerCraft analyze resumes and job descriptions?")
    st.write("**Answer:** CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two.")
    avs.add_vertical_space(3)
    st.write("**Question:** Can CareerCraft suggest improvements for my resume?")
    st.write("**Answer:** Yes, CareerCraft provides personalized recommendations to optimize your resume for specific job openings, including suggestions for missing keywords and alignment with desired job roles.")
    avs.add_vertical_space(3)
    st.write("**Question:** Is CareerCraft suitable for both entry-level and experienced professionals?")
    st.write("**Answer:** Absolutely! CareerCraft caters to job seekers at all career stages, offering tailored insights and guidance to enhance their resumes and advance their careers.")

with col1:
    img3 = Image.open("images/icon3.png")
    st.image(img3, use_column_width=True)
