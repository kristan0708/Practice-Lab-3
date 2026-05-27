import price_info as pri

def test_total_cost_shopping():
    expected_result = 46.75
    result = pri.total_cost_shopping()

    assert (result == expected_result)

def test_cost_of_fruit():
    expected_result = 18.9
    result = pri.cost_of_fruits("pineapple", 7)

    assert (result == expected_result)