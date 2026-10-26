import pytest

from analyzer import calculate_match_score, extract_skills


def test_match_score_is_between_zero_and_100():
    resume = "Python developer with experience in machine learning"
    job = "Python developer with machine learning skills"

    score = calculate_match_score(resume, job)

    assert 0 <= score <= 100


def test_identical_text_has_100_percent_similarity():
    text = "Python developer with machine learning skills"

    score = calculate_match_score(text, text)

    assert score == 100.0


def test_extract_skills_finds_technical_skills():
    text = "I use Python, SQL, FastAPI, and PyTorch."

    skills = extract_skills(text)

    assert "python" in skills
    assert "sql" in skills
    assert "fastapi" in skills
    assert "pytorch" in skills


def test_extract_skills_returns_empty_list_when_none_found():
    text = "I enjoy reading books and travelling."

    skills = extract_skills(text)

    assert skills == []

def test_empty_resume_raises_error():
    with pytest.raises(ValueError, match="Resume text cannot be empty"):
        calculate_match_score("", "Python developer")


def test_empty_job_description_raises_error():
    with pytest.raises(ValueError, match="Job description cannot be empty"):
        calculate_match_score("Python developer", "")


def test_text_without_meaningful_words_raises_error():
    with pytest.raises(ValueError, match="Not enough meaningful text"):
        calculate_match_score("the and is", "a an the")
