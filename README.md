Solar Challenge Week 1
This repository contains the code and resources for Week 1 of the Solar Challenge.
Folder Structure
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md

Setup Instructions
To reproduce the environment locally:

Clone the repository:
git clone https://github.com/redietamare/solar-challenge-week1.git
cd solar-challenge-week1


Set up a Python virtual environment:
python -m venv venv
source venv/Scripts/activate  # On Windows (Git Bash)


Install dependencies:
pip install -r requirements.txt


Verify setup:
python --version
pip list



Development

Use the src/ folder for core Python modules.
Use notebooks/ for Jupyter notebooks.
Use scripts/ for utility scripts.
Run tests from the tests/ folder (to be implemented).

CI Pipeline
A GitHub Actions workflow (.github/workflows/ci.yml) runs on push and pull requests to main and setup-task, installing dependencies and checking the Python version.
