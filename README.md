# AnalyzWEB

AnalyzWEB is a simple WEB for data scientists, analysts or anyone who studies or work with Data Science.

## Technologies behind

- uv (Project Management)
- Python
- Streamlit
- Scikit-learn
- Pandas
- Numpy

## Important commands

### UV

Create virtual env: `uv venv`

Activate virtual env on Linux and MacOS: `source .venv/bin/activate`

Activate virtual env on Windows: `.venv\Scripts\activate.ps1` or `.venv\Scripts\activate.bat`

Deactivate virtual env: `deactivate`

Add dependencies: `uv add <dependency_name>`

To lock dependencies declared in a pyproject.toml: `uv pip compile pyproject.toml -o requirements.txt`

Sync virtual env with requirements.txt: `uv pip sync requirements.txt`

[UV Documentation](https://docs.astral.sh/uv/getting-started/)

### Streamlit

Run streamlit: `uv run streamlit run app.py`

[Streamlit Documentation](https://docs.streamlit.io/get-started/installation/command-line#install-streamlit-in-your-environment)
