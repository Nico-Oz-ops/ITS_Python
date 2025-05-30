from my_project.weather import check_weather
import pytest
'''
# Test 1 - passed
def test_check_weather1():
    assert check_weather(21.00) == "hot", 'temperatures greater than 20 degree \
must be considered as hot'

# Test 2 - failed
def test_check_weather2():
    assert check_weather(5.00) == "average", 'temperatures between 10 and 20 degree \
must be considered as average temperature'

# Test 3 - passed
def test_check_weather3():
    assert check_weather(5.00) == "cold", 'temperatures lower 10 must be considered as cold'

# Test 4 - passed
def test_check_weather4():
    assert check_weather(13.00) == "average", 'temperatures between 10 and 20 degree \
must be considered as average temperature'

# Test 5 - failed because every def test_function() is considered as a single test
def test_check_weather5():
    assert check_weather(30.00) == "hot", 'temperatures greater than 20 degree must be considered as hot'
    assert check_weather(11.00) == "cold", 'temperatures lower 10 must be considered as cold'
'''
'''
@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
])
def test_check_weather(temperature, expected):
    assert check_weather(temperature) == expected
'''

@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
])
def test_check_weather(temperature, expected):
    ae: str = ""
    if temperature > 20:
        ae = "temperature greater than 20 degree must be considered as hot"
    elif 10 < temperature <= 20:
        ae = "temperatures between 10 and 20 degree must be considered as average temperature"
    else:
        ae = "temperatures lower 10 must be considered as cold"
    assert check_weather(temperature) == expected, ae


