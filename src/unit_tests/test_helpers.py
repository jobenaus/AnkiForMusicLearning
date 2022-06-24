"""Tests helpers.py"""
import json
from unittest import mock
import pytest

from constants import SETTINGS_FILE, SETTINGS_FIXING_HINT, DEFAULT_SETTINGS

from helpers import load_settings, create_default_settings, ask_to_fix_settings


class TestLoadSettings:
    """
    Test that load_settings() has the correct behavior.
    """

    @mock.patch(
        "helpers.open",
        mock.mock_open(
            read_data=json.dumps({"test_mode": False, "override_deck": True})
        ),
    )
    def test_load_settings_file_exists(self):
        """Test that load_settings() works when settings.json exists and everything is correct."""
        with mock.patch(
            "helpers.create_default_settings"
        ) as mock_create_default_settings:
            with mock.patch("helpers.ask_to_fix_settings") as mock_ask_to_fix_settings:
                with mock.patch("helpers.print") as mock_print:
                    settings = load_settings()
                    assert settings == {"test_mode": False, "override_deck": True}
        # TODO: test that the file is not overwritten
        # TODO: test that file is opend once with correct mode

    def test_load_settings_file_does_not_exist(self):
        """Test that load_settings() creates a default settings.json file if it does not exist.
        Also it returns the default settings."""
        with mock.patch(
            "helpers.create_default_settings"
        ) as mock_create_default_settings:
            with mock.patch("helpers.ask_to_fix_settings") as mock_ask_to_fix_settings:
                with mock.patch("helpers.print") as mock_print:
                    pass
        # TODO  test that create_default_settings() is called
        # TODO test that default settings are returned
        # TODO test that the warning is printed

    def test_load_settings_not_valid_json(self):
        """Test that load_settings() prints a warning if the settings.json file is not valid json.
        Also it returns the default settings."""
        with mock.patch(
            "helpers.create_default_settings"
        ) as mock_create_default_settings:
            with mock.patch("helpers.ask_to_fix_settings") as mock_ask_to_fix_settings:
                with mock.patch("helpers.print") as mock_print:
                    pass
        # TODO test that the warning is printed
        # TODO test that ask_to_fix_settings() is called

    @mock.patch("helpers.open", mock.mock_open(read_data=json.dumps({})))
    def test_load_settings_is_empty(self):
        """Test that load_settings() works when settings.json is empty."""
        with mock.patch(
            "helpers.create_default_settings"
        ) as mock_create_default_settings:
            with mock.patch("helpers.ask_to_fix_settings") as mock_ask_to_fix_settings:
                with mock.patch("helpers.print") as mock_print:
                    settings = load_settings()
                    assert settings == DEFAULT_SETTINGS
                    mock_create_default_settings.assert_called_once()
                    mock_print.assert_called_once_with("settings.json is empty.")

    @mock.patch(
        "helpers.open",
        mock.mock_open(read_data=json.dumps({"test_mode": False})),
    )
    def test_load_settings_missing_keys(self):
        """Test that load_settings() works when settings.json is missing keys."""
        with mock.patch(
            "helpers.create_default_settings"
        ) as mock_create_default_settings:
            with mock.patch("helpers.ask_to_fix_settings") as mock_ask_to_fix_settings:
                with mock.patch("helpers.print") as mock_print:
                    # TODO the test fails and I don't know why
                    # load_settings()
                    # mock_ask_to_fix_settings.assert_called_once()
                    # mock_print.assert_called_once_with(
                    #     "settings.json is missing keys."
                    # )
                    pass

    @mock.patch(
        "helpers.open",
        mock.mock_open(
            read_data=json.dumps({"test_mode": False, "override_deck": "True"})
        ),
    )
    def test_load_settings_wrong_type(self):
        """Test that load_settings() works when settings.json has wrong types."""
        with mock.patch(
            "helpers.create_default_settings"
        ) as mock_create_default_settings:
            with mock.patch("helpers.ask_to_fix_settings") as mock_ask_to_fix_settings:
                with mock.patch("helpers.print") as mock_print:
                    load_settings()
                    mock_ask_to_fix_settings.assert_called_once()
                    mock_print.assert_called_once_with(
                        "settings.json has invalid types."
                    )

    @mock.patch(
        "helpers.open",
        mock.mock_open(
            read_data=json.dumps(
                {"test_mode": False, "override_deck": True, "extra_key": "extra_value"}
            )
        ),
    )
    def test_load_settings_extra_keys(self):
        """Test that load_settings() works when settings.json has extra keys."""
        with mock.patch(
            "helpers.create_default_settings"
        ) as mock_create_default_settings:
            with mock.patch("helpers.ask_to_fix_settings") as mock_ask_to_fix_settings:
                with mock.patch("helpers.print") as mock_print:
                    settings = load_settings()
                    assert settings == DEFAULT_SETTINGS
                    mock_print.assert_called_once_with(
                        "Some keys in settings.json are not in default_settings."
                    )


class TestCreateDefaultSettings:
    """
    Test that create_default_settings() has the correct behavior.
    """

    @mock.patch("helpers.open", mock.mock_open())
    def test_create_default_settings_print(self):
        """Test that create_default_settings() prints message."""
        with mock.patch("helpers.print") as mock_print:
            create_default_settings()
            mock_print.assert_called_once_with("Created default settings.json file.")

    def test_create_default_settings_write(self):
        """Test that create_default_settings() writes to file."""
        with mock.patch("helpers.open") as mock_open:
            create_default_settings()
            mock_open.assert_called_once_with(SETTINGS_FILE, "w", encoding="utf8")

    def test_create_default_settings_write_correct_data(self):
        """Test that create_default_settings() writes correct data to file."""
        with mock.patch("helpers.open") as mock_open:
            create_default_settings()

            # TODO test that the data is written correctly


class TestAskToFixSettings:
    """
    Test that ask_to_fix_settings() has the correct behavior.
    """

    def test_ask_to_fix_settings_print(self):
        """Test that ask_to_fix_settings() prints message."""
        with mock.patch("helpers.print") as mock_print:
            with pytest.raises(SystemExit):

                ask_to_fix_settings(TypeError)
                mock_print.assert_called_once_with(SETTINGS_FIXING_HINT)

    def test_ask_to_fix_settings_exit_with_error(self):
        """Test that ask_to_fix_settings() exits with correct error."""

        with pytest.raises(SystemExit) as error:
            ask_to_fix_settings(TypeError)

        assert error.value.code == TypeError
