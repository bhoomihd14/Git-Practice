import re
import json
import argparse
from pathlib import Path

from config import (
    BASE_DIR,
    REPORTS_DIR,
    REPORT_FILE,
    EXCLUDED_DIRS,
    MAX_FILE_SIZE,
    SUPPORTED_EXTENSIONS
)


# Secret detection patterns

SECRET_PATTERNS = {
    "AWS Access Key": re.compile(
        r"\bAKIA[0-9A-Z]{16}\b"
    ),

    "GitHub Token": re.compile(
        r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"
    ),

    "Generic Secret Assignment": re.compile(
        r"""(?i)\b(api_key|apikey|secret_key|password|passwd|access_token)\b\s*[:=]\s*["']?([A-Za-z0-9_./+=-]{8,})"""
    ),

    "Private Key": re.compile(
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
    )
}


# Ignore common placeholder values

PLACEHOLDERS = {
    "your_api_key",
    "your_secret_key",
    "your_password",
    "example_password",
    "changeme",
    "replace_me",
    "placeholder"
}


def mask_secret(secret):
    """Hide sensitive characters before displaying a finding."""

    if len(secret) <= 4:
        return "*" * len(secret)

    return secret[:2] + "*" * 6 + secret[-2:]


def scan_file(file_path):
    """Scan an individual file for exposed secrets."""

    findings = []

    try:
        if file_path.stat().st_size > MAX_FILE_SIZE:
            return findings

        content = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        for line_number, line in enumerate(
            content.splitlines(), start=1
        ):

            for rule_name, pattern in SECRET_PATTERNS.items():

                for match in pattern.finditer(line):

                    if rule_name == "Generic Secret Assignment":
                        secret = match.group(2)
                    else:
                        secret = match.group(0)

                    if secret.lower() in PLACEHOLDERS:
                        continue

                    findings.append({
                        "file": str(
                            file_path.relative_to(BASE_DIR)
                        ),
                        "line": line_number,
                        "type": rule_name,
                        "masked_secret": mask_secret(secret)
                    })

    except (OSError, ValueError) as error:
        print(f"Could not scan {file_path}: {error}")

    return findings


def scan_directory(directory):
    """Scan all supported source files in a directory."""

    all_findings = []

    for file_path in directory.rglob("*"):

        if not file_path.is_file():
            continue

        if any(
            excluded in file_path.parts
            for excluded in EXCLUDED_DIRS
        ):
            continue

        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        all_findings.extend(scan_file(file_path))

    return all_findings


def generate_report(findings):
    """Generate a JSON security scan report."""

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    report = {
        "project": "DevSecOps Secret Scanner",
        "total_findings": len(findings),
        "status": "FAILED" if findings else "PASSED",
        "findings": findings
    }

    REPORT_FILE.write_text(
        json.dumps(report, indent=4),
        encoding="utf-8"
    )

    print("\nSecurity Scan Summary")
    print("---------------------")
    print(f"Total findings: {len(findings)}")
    print(f"Status: {report['status']}")
    print(f"Report saved to: {REPORT_FILE}")

    return report


def main():
    parser = argparse.ArgumentParser(
        description="DevSecOps Automated Secret Scanner"
    )

    parser.add_argument(
        "directory",
        nargs="?",
        default=str(BASE_DIR),
        help="Directory to scan"
    )

    args = parser.parse_args()

    target_directory = Path(args.directory).resolve()

    if not target_directory.is_dir():
        print("Error: Invalid directory.")
        raise SystemExit(2)

    print("Starting security scan...")

    findings = scan_directory(target_directory)

    report = generate_report(findings)

    if report["total_findings"] > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()