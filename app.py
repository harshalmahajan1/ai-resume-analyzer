
import streamlit as st

from analyzer import (
    calculate_match_score,
    extract_resume_text,
    extract_skills,
)

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
)

st.title("📄 AI Resume Analyzer")
st.write(
    "Upload your resume and compare it with a job description "
    "to discover your strengths and skill gaps."
)

resume_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"],
)

job_description = st.text_area(
    "Paste the job description",
    height=220,
    placeholder="Paste the complete job description here...",
)

if st.button("Analyze Resume"):
    if resume_file is None:
        st.error("Please upload a resume PDF.")
    elif not job_description.strip():
        st.error("Please enter a job description.")
    else:
        try:
            resume_text = extract_resume_text(resume_file)

            if not resume_text.strip():
                st.error(
                    "No readable text found in this PDF. "
                    "Please upload a text-based resume PDF."
                )
            else:
                score = calculate_match_score(
                    resume_text,
                    job_description,
                )

                resume_skills = extract_skills(resume_text)
                job_skills = extract_skills(job_description)

                missing_skills = sorted(
                    set(job_skills) - set(resume_skills)
                )

                st.subheader("Analysis Results")
                st.metric("Resume Match Score", f"{score}%")

                st.subheader("Skills Found in Your Resume")
                st.write(
                    ", ".join(resume_skills)
                    if resume_skills
                    else "No recognized skills found."
                )

                st.subheader("Skills Missing from Your Resume")
                st.write(
                    ", ".join(missing_skills)
                    if missing_skills
                    else "No missing skills found from our skill list."
                )

        except (ValueError, RuntimeError) as error:
            st.error(f"Could not analyze the resume: {error}")
        except Exception:
            st.error(
                "Something went wrong while reading the PDF. "
                "Please try another resume file."
            )
