# 📄 ResumeScreenerAI – AI-Powered Resume Screening Tool

An AI-driven tool for HR professionals and recruiters to automate resume screening by matching candidate resumes to job descriptions using NLP. Built with Python, Streamlit, and `scikit-learn`, it extracts key information and ranks resumes based on similarity.

---

## ✨ Features
✅ Upload PDF resumes to a `resumes/` folder  
📝 Matches resumes to job descriptions using TF-IDF and cosine similarity  
📊 Displays top matching resumes with similarity scores  
💻 Interactive Streamlit interface for selecting job titles  
📂 Supports custom job descriptions via `job_descriptions.csv`

---

## 🛠 Tech Stack
- Python 3.8+  
- Streamlit (Web app framework)  
- `scikit-learn` (NLP and similarity scoring)  
- `spaCy` (NLP preprocessing)  
- `PyPDF2` (PDF text extraction)  
- `pandas` (Data handling)

---

## 🚀 Installation
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/AnilKumar-Guntupalli/ResumeScreenerAI.git
   cd ResumeScreenerAI
   ```

2. **Create a virtual environment (optional but recommended)**:  
   ```bash
   python -m venv venv
   # Activate it
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Install `spaCy` model**:  
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. **Prepare the `resumes/` folder**:  
   Create a `resumes/` folder in the project directory and add PDF resumes.

6. **Ensure `job_descriptions.csv` is ready**:  
   The repository includes a sample `job_descriptions.csv`. Update it with your own job titles and descriptions if needed.

---

## 🧪 Run the App
1. **Launch the Streamlit app**:  
   ```bash
   streamlit run app.py
   ```

2. **Interact with the app**:  
   - Open the provided URL (e.g., `http://localhost:8501`) in your browser.
   - Select a job title from the dropdown.
   - View the job description and top matching resumes with similarity scores.

---

## 📂 Project Structure
```
ResumeScreenerAI/
│
├── app.py                 # Streamlit frontend logic
├── main.py                # Computes resume-job description similarity
├── load_data.py           # Loads and extracts text from PDF resumes
├── preprocess.py          # Cleans text for NLP processing
├── extract_text.py        # Extracts text from PDFs using PyPDF2
├── job_descriptions.csv   # Sample job descriptions
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## ⚠️ Notes
- Ensure the `resumes/` folder contains PDF files; otherwise, the app will display a warning.
- The `job_descriptions.csv` must have columns `Job Title` and `Job Description`.
- For large PDFs, text extraction may be slow; consider optimizing `PyPDF2` usage in future updates.
- Add more resumes and job descriptions to improve matching accuracy.

---

## 📈 Example Usage
- Select "Software Engineer" from the dropdown.
- View the job description.
- See top matches like:  
  - `resume1.pdf — Similarity Score: 0.85`  
  - `resume2.pdf — Similarity Score: 0.72`

---

## 🔮 Future Improvements
- Add keyword extraction using `spaCy` for better matching.  
- Support additional file formats (e.g., DOCX).  
- Deploy on Streamlit Cloud for online access.  
- Integrate a scoring system for specific skills.

---

## 📜 License
MIT License