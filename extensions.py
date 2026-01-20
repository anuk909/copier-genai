"""Custom Jinja2 extensions for Copier template."""

from __future__ import annotations

import re
import subprocess
import unicodedata
from datetime import date

from jinja2.ext import Extension


def git_user_name(default: str) -> str:
    """Get git user.name or return default."""
    return subprocess.getoutput("git config user.name").strip() or default


def git_user_email(default: str) -> str:
    """Get git user.email or return default."""
    return subprocess.getoutput("git config user.email").strip() or default


def slugify(value, separator="-"):
    """Convert text to slug with proper unicode normalization."""
    value = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-_\s]+", separator, value).strip("-_")


class GitExtension(Extension):
    """Jinja2 extension for Git-related filters."""

    def __init__(self, environment):
        """Initialize the extension."""
        super().__init__(environment)
        environment.filters["git_user_name"] = git_user_name
        environment.filters["git_user_email"] = git_user_email


class SlugifyExtension(Extension):
    """Jinja2 extension for slugification."""

    def __init__(self, environment):
        """Initialize the extension."""
        super().__init__(environment)
        environment.filters["slugify"] = slugify


class CurrentYearExtension(Extension):
    """Jinja2 extension to get the current year."""

    def __init__(self, environment):
        """Initialize the extension."""
        super().__init__(environment)
        environment.globals["current_year"] = date.today().year
