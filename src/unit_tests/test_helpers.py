"""Tests helpers.py"""
import json
from unittest import mock



from helpers import load_settings


class TestLoadSettings:
    """
    Test the following behaviours of load_settings()
    if settings.json exists:
        - load settings from settings.json
    if settings.json does not exist:
        - create default_settings file and load settings from that file.

    Don't use the actual settings.json file for the test. Instead use a mock objeckt.
    """

    def test_load_settings_if_settings_file_exists(self, mocker):
        """
        Test that load_settings() loads settings from settings.json if it exists.
        """
        # Mock the open() function to return a mock object.
        mocker.patch(
            "helpers.open",
            mocker.mock_open(
                read_data=json.dumps({"test_mode": False, "override_deck": False})
            ),
        )

        # Call load_settings() and assert that the settings are loaded from settings.json.
        assert load_settings() == {"test_mode": False, "override_deck": False}

    def test_load_settings_if_settings_file_does_not_exist(self, mocker):
        """
        Test that load_settings() creates a default settings.json file if it does not exist. The mock has to raise a FileNotFoundError."""
        # Mock the open() function to return a mock object.
        # TODO: mock.mock_open(side_effect=FileNotFoundError) does not work.

    def test_load_settings_if_settings_file_is_empty(self, mocker):
        """
        Test that load_settings() creates a default settings.json file if it is empty.
        """
        # Mock the open() function to return a mock object.

        mocker.patch("helpers.open", mocker.mock_open(read_data=""))

        # Call load_settings() and assert that the settings are loaded from settings.json.
        assert load_settings() == {}

    def test_load_settings_if_settings_file_is_not_json(self, mocker):
        """
        Test that load_settings() creates a default settings.json file if it is not json.
        """
        # Mock the open() function to return a mock object
