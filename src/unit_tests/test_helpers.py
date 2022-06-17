"""Tests helpers.py"""
import pytest
from helpers import load_settings


class TestLoadSettings:
    """Tests load_settings from helpers.py"""

    def test_load_settings_no_settings_file_raises_error(self):
        """Test that load_settings raises error if no settings.json file is present."""
        with pytest.raises(FileNotFoundError) as excinfo:
            load_settings()
        assert excinfo.value.args[0] == "settings.json not found"

    # TODO test load_settings with settings.json file present and che ckeck if settings are loaded correctly
