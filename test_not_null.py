from coin_flip import coin_flip

expected_outcomes = ["Heads", "Tails"]

def test_coin_flip():
    assert coin_flip() is not None, "Result should not be None"
