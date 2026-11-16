from pathlib import Path

# Project directory
BASE_DIR = Path(__file__).resolve().parent

# Reports directory
REPORTS_DIR = BASE_DIR / "reports"

# Security scan report
REPORT_FILE = REPORTS_DIR / "secret_scan_report.json"

# Directories to exclude during scanning
EXCLUDED_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "reports"
}

# Maximum file size to scan (1 MB)
MAX_FILE_SIZE = 1024 * 1024

# Supported file extensions
SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".java",
    ".html",
    ".css",
    ".json",
    ".yaml",
    ".yml",
    ".txt",
    ".env",
    ".config"
}