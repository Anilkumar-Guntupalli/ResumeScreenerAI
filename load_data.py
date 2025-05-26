import os
from extract_text import extract_text_from_pdf

def load_resumes(resume_folder="resumes"):
    resumes = []
    filenames = []
    for file in os.listdir(resume_folder):
        if file.lower().endswith(".pdf"):
            path = os.path.join(resume_folder, file)
            text = extract_text_from_pdf(path)
            if text:
                resumes.append(text)
                filenames.append(file)
    return resumes, filenames
