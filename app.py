import re

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def validate_email(email):
    """Return True if the email address looks valid."""
    if not isinstance(email, str):
        return False
    return bool(EMAIL_RE.match(email.strip()))