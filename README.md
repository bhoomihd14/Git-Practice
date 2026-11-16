# Git-Practice
Learning Git and GitHub
DevSecOps – Automated Secret Scanner

1. Project Overview

The Automated Secret Scanner is a DevSecOps-based security project designed to identify exposed sensitive information in source code.

It detects common security risks such as hardcoded passwords, API keys, access tokens and private keys.

The project combines Python-based secret detection with Gitleaks and GitHub Actions to automate security scanning.

2. Objectives

- Identify exposed secrets in source code.
- Detect hardcoded passwords and API keys.
- Automate security scanning.
- Generate security scan reports.
- Integrate security testing into the development workflow.
- Improve application security through early vulnerability detection.

3. Technologies Used

- Python
- Git
- GitHub
- Gitleaks
- GitHub Actions
- Pytest

4. Project Structure

Git-Practice/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitleaks.toml
├── reports/
├── tests/
│   └── test_secrets.py
└── .github/
    └── workflows/
        └── security-scan.yml

5. Features

1. Secret Detection – Identifies exposed credentials in source code.
2. Secret Masking – Hides sensitive values in scan results.
3. Automated Testing – Validates detection functionality using Pytest.
4. Security Reports – Generates JSON reports containing scan results.
5. Continuous Security Scanning – Uses GitHub Actions to automate security checks.
6. Gitleaks Integration – Provides additional secret detection using built-in rules.

6. Installation

Clone the repository:

git clone <repository-url>

Navigate into the project directory:

cd Git-Practice

Install dependencies:

pip install -r requirements.txt

7. Running the Application

Run the secret scanner:

python app.py

Run automated tests:

pytest -v

8. Expected Outcome

The application scans supported source code files and identifies potential exposed secrets.

A JSON report is generated inside the reports directory.

GitHub Actions automatically executes the configured security workflow when code is pushed or a pull request is created against the main branch.

9. Conclusion

This project demonstrates how DevSecOps practices can improve application security by integrating automated secret detection and security testing into the software development lifecycle.

It helps developers identify exposed credentials early and encourages secure coding practices.