import Lab2
print ("Test_Lab2")

def test_find_min_max():
    input_temp = [24, 34, 25, 12, 22, 11, 30]
    test_min = min(input_temp)
    test_max = max(input_temp)
    result = Lab2.find_min_max(input_temp)
    assert (result == (test_min, test_max))

def test_calc_average():
    input_temp = [24, 34, 25, 12, 22, 11, 30]
    test_average = 22.571428571428573
    result = Lab2.calc_average(input_temp)
    assert result == test_average

def test_calc_median_temperature():
    input_temp = [24, 34, 25, 12, 22, 11, 30]
    test_median = 24
    result = Lab2.calc_median_temperature(input_temp)
    assert result == test_median

