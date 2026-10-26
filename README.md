
# AI Resume Analyzer

A Python-based web application that analyzes a resume against a job description and highlights relevant skills and potential skill gaps.

## Features

- Upload resumes in PDF format.
- Extract text from PDF resumes.
- Calculate a text similarity score using TF-IDF and cosine similarity.
- Identify recognized skills in resumes and job descriptions.
- Highlight skills that appear in the job description but not in the resume.
- Handle empty inputs and unreadable PDF text.
- Include automated tests using pytest.

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- scikit-learn
- pytest

## Project Structure

```text
ai-resume-analyzer/
├── app.py
├── analyzer.py
├── test_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-resume-analyzer
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run the application

```powershell
python -m streamlit run app.py
```

Open the local URL displayed in your terminal.

## Run Tests

```powershell
python -m pytest -v
```

## How It Works

1. The user uploads a PDF resume.
2. The application extracts text from the PDF.
3. The user provides a job description.
4. TF-IDF vectorization and cosine similarity calculate a text similarity score.
5. The application identifies recognized skills and highlights potential skill gaps.

## Limitations

- The similarity score measures text similarity; it is not an official ATS score or a guarantee of hiring suitability.
- Skill detection is based on a predefined list of skills.
- Scanned PDFs without an embedded text layer may not be readable.

## Future Improvements

- Expand the skill database.
- Add support for more document formats.
- Improve skill matching and resume feedback.

## Author

Harshal Mahajan
