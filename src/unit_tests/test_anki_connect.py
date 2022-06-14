from app.anki_connect import request


def test_request_one_parameter():
    expected = {
        "action": "getEaseFactors",
        "version": 6,
        "params": {"cards": [1483959291685, 1483959293217]},
    }
    actual = request("getEaseFactors", cards=[1483959291685, 1483959293217])
    assert actual == expected


def test_request_multiple_parameters():
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
