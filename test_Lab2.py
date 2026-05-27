import Lab2.Lab2 as lab2

def test_min_max():
    result = []
    input_arr = [4,1,6,45,23,76,12,32,4324,12,4,2,34]
    test_arr = [1,4324]

    result = lab2.find_min_max(input_arr)
    assert (result == test_arr)

def test_calc_average():
    input_arr = [1,2,3,4,5,6,7,8,9,10]
    test_result = 5.5

    result = lab2.calc_average(input_arr)
    assert (result == test_result)

def test_odd_number_of_calc_median_temperature():
    input_arr = [12,34,5,45,76]
    test_result = 34

    result = lab2.calc_median_temperature(input_arr)
    assert(result == test_result)

def test_even_number_of_calc_median_temperature():
    input_arr = [12,34,5,94,45,76]
    test_result = 39.5

    result = lab2.calc_median_temperature(input_arr)
    assert (result == test_result)