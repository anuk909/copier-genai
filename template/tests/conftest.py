"""
Test configuration and fixtures

TODO: Add your pytest fixtures here.
"""

import pytest
from pathlib import Path


@pytest.fixture
def test_config_path():
    """Provide path to test configuration"""
    return Path(__file__).parent / "fixtures" / "test_config.yaml"


@pytest.fixture
def sample_messages():
    """Provide sample messages for testing"""
    from src.core import Message
    
    return [
        Message(role="system", content="You are a helpful assistant."),
        Message(role="user", content="Hello!"),
    ]


# TODO: Add more fixtures as needed
