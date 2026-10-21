import pytest

from app import validate_email


@pytest.mark.parametrize(
    "email",
    [
        "user@example.com",
        "first.last@example.co.uk",
        "user+tag@example.org",
        "user_name-1@sub.example.io",
    ],
)
def test_valid_emails(email):
    assert validate_email(email) is True


def test_missing_at():
    assert validate_email("userexample.com") is False


@pytest.mark.parametrize("email", ["user@", "user@.com", "user@com"])
def test_missing_domain(email):
    assert validate_email(email) is False


@pytest.mark.parametrize("email", ["  user@example.com", "user@example.com  ", "\tuser@example.com\n"])
def test_leading_and_trailing_spaces_are_stripped(email):
    assert validate_email(email) is True


@pytest.mark.parametrize("value", [None, 123, 1.5, ["user@example.com"], b"user@example.com"])
def test_non_string_input(value):
    assert validate_email(value) is False


@pytest.mark.parametrize("email", ["user..name@example.com", "user@example..com"])
def test_consecutive_dots(email):
    assert validate_email(email) is False


def test_domain_starting_with_hyphen():
    assert validate_email("user@-example.com") is False
