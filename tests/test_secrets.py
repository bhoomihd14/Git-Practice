import app


def test_mask_secret():
    """Check whether sensitive values are masked."""

    result = app.mask_secret("abcdefgh12345678")

    assert result == "ab******78"


def test_detect_aws_access_key(tmp_path, monkeypatch):
    """Check whether AWS access keys are detected."""

    monkeypatch.setattr(app, "BASE_DIR", tmp_path)

    file_path = tmp_path / "sample.py"

    fake_key = "AKIA" + "1234567890ABCDEF"

    file_path.write_text(
        f'aws_key = "{fake_key}"'
    )

    findings = app.scan_file(file_path)

    assert len(findings) == 1
    assert findings[0]["type"] == "AWS Access Key"


def test_detect_generic_password(tmp_path, monkeypatch):
    """Check whether hardcoded passwords are detected."""

    monkeypatch.setattr(app, "BASE_DIR", tmp_path)

    file_path = tmp_path / "config.py"

    file_path.write_text(
        'password = "secret12345678"'
    )

    findings = app.scan_file(file_path)

    assert len(findings) == 1
    assert findings[0]["type"] == "Generic Secret Assignment"


def test_ignore_placeholder_values(tmp_path, monkeypatch):
    """Check whether common placeholder values are ignored."""

    monkeypatch.setattr(app, "BASE_DIR", tmp_path)

    file_path = tmp_path / "example.py"

    file_path.write_text(
        'password = "your_password"'
    )

    findings = app.scan_file(file_path)

    assert len(findings) == 0


def test_detect_github_token(tmp_path, monkeypatch):
    """Check whether GitHub tokens are detected."""

    monkeypatch.setattr(app, "BASE_DIR", tmp_path)

    file_path = tmp_path / "sample.py"

    fake_token = "ghp_" + "A" * 30

    file_path.write_text(
        f'github_token = "{fake_token}"'
    )

    findings = app.scan_file(file_path)

    assert len(findings) == 1
    assert findings[0]["type"] == "GitHub Token"