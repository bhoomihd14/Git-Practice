DevSecOps – Automated Secret Scanner

1. Project Overview

The Automated Secret Scanner is a DevSecOps-based security project developed to identify exposed sensitive information in source code.

It detects common security risks such as hardcoded passwords, AWS access keys, GitHub tokens, API keys and private keys.

The project combines a Python-based secret detection application with Gitleaks and GitHub Actions to automate security scanning and integrate security checks into the software development lifecycle.

2. Problem Statement

Developers sometimes accidentally include sensitive information such as passwords, API keys and access tokens in source code.

If these credentials are pushed to a public or shared repository, they may be exposed to unauthorized users and lead to security risks.

Manual checking is not always reliable. Therefore, an automated solution is required to identify exposed secrets during the development process.

3. Objectives

- Identify exposed secrets in source code.
- Detect hardcoded passwords, API keys and access tokens.
- Mask sensitive values in scan results.
- Generate security scan reports in JSON format.
- Automate security testing using Pytest.
- Integrate Gitleaks for additional secret detection.
- Implement continuous security scanning using GitHub Actions.

4. Technologies Used

Technology| Purpose
Python| Developing the secret scanner
Git| Version control
GitHub| Source code hosting
Gitleaks| Secret detection
GitHub Actions| Workflow automation
Pytest| Automated testing
JSON| Security report generation

5. Project Structure

Git-Practice/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── gitleaks.toml
│
├── tests/
│   └── test_secrets.py
│
├── reports/
│   └── secret_scan_report.json
│
└── .github/
    └── workflows/
        └── security-scan.yml

Note: The "reports/" directory contains generated scan reports and is excluded from Git tracking.

6. Features and Functionalities

6.1 Secret Detection

Identifies potentially exposed credentials, including:

- AWS access keys
- GitHub tokens
- Generic secret assignments
- Private keys

6.2 Secret Masking

Masks sensitive values before displaying findings to prevent unnecessary exposure.

6.3 Placeholder Filtering

Ignores common placeholder values such as "your_password" and "changeme".

6.4 Automated Testing

Uses Pytest to validate secret detection, masking and placeholder filtering.

6.5 JSON Security Reports

Generates a JSON report containing:

- Total number of findings
- Scan status
- File location
- Line number
- Type of detected secret
- Masked secret value

6.6 Gitleaks Integration

Uses Gitleaks to perform additional repository-level secret scanning.

6.7 Continuous Integration

Uses GitHub Actions to automatically execute security checks when code is pushed or a pull request is created against the "main" branch.

7. Installation and Setup

Step 1: Clone the Repository

git clone https://github.com/bhoomihd14/Git-Practice.git

Step 2: Navigate to the Project Directory

cd Git-Practice

Step 3: Create a Virtual Environment

python -m venv .venv

Step 4: Activate the Virtual Environment

For Windows PowerShell:

.venv\Scripts\Activate.ps1

Step 5: Install Dependencies

pip install -r requirements.txt

8. Running the Application

Run the Secret Scanner

python app.py

The scanner examines supported files in the project directory and generates a JSON security report.

Run Automated Tests

python -m pytest -v

The test suite validates the following functionalities:

1. Secret masking
2. AWS access key detection
3. Generic password detection
4. Placeholder value filtering
5. GitHub token detection

9. Security Scan Report

The application generates a report at:

reports/secret_scan_report.json

The report contains the scan status and details of detected findings.

Sample successful scan output:

Starting security scan...

Security Scan Summary
---------------------
Total findings: 0
Status: PASSED

10. GitHub Actions Workflow

The project uses GitHub Actions to automate security checks.

The workflow is configured to execute on:

- Push events to the "main" branch.
- Pull requests targeting the "main" branch.
- Manual workflow execution.

Workflow Execution Steps

1. Checkout Repository
2. Set up Python
3. Install Dependencies
4. Run Automated Tests
5. Run Gitleaks Security Scan

The workflow displays the execution status on the GitHub Actions dashboard.

A successful execution indicates that the configured automated tests and security scanning steps have completed without errors.

11. Testing Results

The project includes five automated test cases.

Test Case| Expected Result| Status
Secret masking| Sensitive value is masked| Passed
AWS key detection| AWS key is detected| Passed
Password detection| Hardcoded password is detected| Passed
Placeholder filtering| Placeholder is ignored| Passed
GitHub token detection| GitHub token is detected| Passed

Total automated tests: 5

Result: All 5 tests passed.

The complete project scan also completed successfully with zero findings.

12. Conclusion

The DevSecOps Automated Secret Scanner demonstrates how automated security practices can improve the software development lifecycle.

By combining Python-based secret detection, Pytest, Gitleaks and GitHub Actions, the project provides an automated approach to identifying exposed credentials and validating security checks.

It encourages secure coding practices and demonstrates the importance of integrating security into the development and deployment process.