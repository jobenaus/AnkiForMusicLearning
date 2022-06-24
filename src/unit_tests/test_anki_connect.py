"""
Test that the request function returns the correct request.
"""

from anki_connect import request, handle_response
import pytest


class TestRequest:
    """Tests the request function with one or more parameters."""

    def test_request_one_parameter(self):
        """Tast that one parameter is correctly handled by request."""
        expected = {
            "action": "getEaseFactors",
            "version": 6,
            "params": {"cards": [1483959291685, 1483959293217]},
        }
        actual = request("getEaseFactors", cards=[1483959291685, 1483959293217])
        assert actual == expected

    def test_request_multiple_parameters(self):
        """Test that multiple parameters are correctly handled by request."""
        expected = {
            "action": "setSpecificValueOfCard",
            "version": 6,
            "params": {
                "card": 1483959291685,
                "keys": ["flags", "odue"],
                "newValues": ["1", "-100"],
            },
        }
        actual = request(
            "setSpecificValueOfCard",
            card=1483959291685,
            keys=["flags", "odue"],
            newValues=["1", "-100"],
        )
        assert actual == expected


class TestHandleResponse:
    """Tests that handle_resonse behaves correctly."""

    # No error
    def test_handle_response_no_error(self):
        """Test that handle_response returns the correct result, when no error is present."""
        response = {"result": ["Default", "Filtered Deck 1"], "error": None}
        actual = handle_response(response)
        expected = ["Default", "Filtered Deck 1"]
        assert actual == expected

    # Error ist present
    def test_handle_response_error(self):
        """Test that handle_response raises an exception, when an error is present."""
        response = {"result": None, "error": "unsupported action"}
        with pytest.raises(Exception) as excinfo:
            handle_response(response)

        assert excinfo.value.args[0] == "unsupported action"

    # Unexpected number of fields
    def test_handle_response_error_no_result(self):
        """Test that handle_response raises an exception, when an error is present and no result is present."""
        response = {"error": "unsupported action"}
        with pytest.raises(Exception) as excinfo:
            handle_response(response)

        assert excinfo.value.args[0] == "response has an unexpected number of fields"

    def test_handle_response_result_no_error(self):
        """Test that handle_response raises an exception, when an result is present and no error is present."""
        response = {"result": ["Default", "Filtered Deck 1"]}
        with pytest.raises(Exception) as excinfo:
            handle_response(response)

        assert excinfo.value.args[0] == "response has an unexpected number of fields"

    def test_handle_response_no_result_no_error(self):
        """Test that handle_response raises an exception, when no result and no error is present."""
        response = {}
        with pytest.raises(Exception) as excinfo:
            handle_response(response)

        assert excinfo.value.args[0] == "response has an unexpected number of fields"

    def test_handle_response_to_many_fields(self):
        """Test that handle_response raises an exception, when too many fields are present."""
        response = {
            "result": ["Default", "Filtered Deck 1"],
            "error": None,
            "extra": "field",
        }
        with pytest.raises(Exception) as excinfo:
            handle_response(response)

        assert excinfo.value.args[0] == "response has an unexpected number of fields"

    # No error field
    def test_handle_response_no_error_field(self):
        """Test that handle_response raises an exception, when no error field is present. But right number of fields."""
        response = {"result": ["Default", "Filtered Deck 1"], "extra": "field"}
        with pytest.raises(Exception) as excinfo:
            handle_response(response)

        assert excinfo.value.args[0] == "response is missing required error field"

    # No result field
    def test_handle_response_no_result_field(self):
        """
        Test that handle_response raises an exception, when no result field is present. But right number of fields.
        """
        response = {"error": "unsupported action", "extra": "field"}
        with pytest.raises(Exception) as excinfo:
            handle_response(response)

        assert excinfo.value.args[0] == "response is missing required result field"
