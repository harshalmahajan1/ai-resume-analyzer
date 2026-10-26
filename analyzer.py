
import re

import pymupdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_resume_text(uploaded_file):
    """Extract text from an uploaded PDF file."""
    resume_text = ""

    with pymupdf.open(
        stream=uploaded_file.getvalue(),
        filetype="pdf",
    ) as document:
        for page in document:
            resume_text += page.get_text() + "\n"

    return resume_text.strip()


def calculate_match_score(resume_text, job_description):
    """Calculate TF-IDF text similarity as a percentage."""
    if not resume_text or not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    if not job_description or not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    vectorizer = TfidfVectorizer(stop_words="english")

    try:
        tfidf_matrix = vectorizer.fit_transform(
            [resume_text, job_description]
        )
    except ValueError as error:
        raise ValueError(
            "Not enough meaningful text to calculate a match score."
        ) from error

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2],
    )[0][0]

    return round(float(similarity) * 100, 2)



def extract_skills(text):
    """Find selected skills in text."""
    skills = [
        "python", "java", "sql", "machine learning",
        "deep learning", "pytorch", "tensorflow",
        "scikit-learn", "pandas", "numpy", "fastapi",
        "flask", "django", "streamlit", "rest api",
        "api testing", "pytest", "selenium",
        "manual testing", "html", "css", "javascript",
        "react", "node.js", "git", "docker", "aws",
        "communication", "excel", "power bi",
    ]

    text = text.lower()
    found_skills = []

    for skill in skills:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(found_skills)
