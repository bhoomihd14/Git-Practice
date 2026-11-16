from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

REPORTS_DIR = BASE_DIR / "reports"

REPORT_FILE = REPORTS_DIR / "secret_scan_report.json"

EXCLUDED_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "reports",
    "tests"
}

MAX_FILE_SIZE = 1024 * 1024

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
