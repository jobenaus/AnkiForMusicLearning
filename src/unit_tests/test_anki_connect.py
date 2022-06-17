"""
Test that the request function returns the correct request.
"""
from anki_connect import request


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


