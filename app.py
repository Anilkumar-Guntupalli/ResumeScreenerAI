import streamlit as st
import pandas as pd
from main import get_top_matches
from load_data import load_resumes

# Load job descriptions
job_df = pd.read_csv("job_descriptions.csv")

st.title("📄 Resume Screening AI")
st.write("Select a job and find top matching resumes based on description similarity.")

job_titles = job_df["Job Title"].tolist()
selected_title = st.selectbox("Select Job Title", job_titles)

job_row = job_df[job_df["Job Title"] == selected_title].iloc[0]
job_desc = job_row["Job Description"]
st.subheader("📋 Job Description")
st.write(job_desc)

resumes, filenames = load_resumes()

if not resumes:
    st.warning("⚠️ No resumes found in the 'resumes/' folder.\n\nPlease add some PDF resumes and restart the app.")
else:
    st.subheader("📈 Top Matching Resumes")
    top_matches = get_top_matches(job_desc, resumes, filenames)
    for i, (file, score) in enumerate(top_matches, 1):
        st.write(f"**{i}. {file}** — Similarity Score: `{score:.2f}`")
