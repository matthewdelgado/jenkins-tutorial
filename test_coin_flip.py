from coin_flip import coin_flip

expected_outcomes = ["Heads", "Tails"]

def test_coin_flip():
    assert coin_flip() in expected_outcomes