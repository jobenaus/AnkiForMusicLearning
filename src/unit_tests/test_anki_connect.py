from app.anki_connect import request


def test_request_one_parameter():
    expected = {
        "action": "getEaseFactors",
        "params": {"cards": [1483959291685, 1483959293217]},
        "version": 6,
    }
    actual = request("getEaseFactors", cards=[1483959291685, 1483959293217])
    assert actual == expected
