from unittest.mock import patch
import requests
# A function that uses an external API to get the current weather
def get_current_weather():
    # This would normally make an API call to get the current weather
    # return "Sunny"
    response = requests.get('https://google.com')
    return response.status_code

# A function that calls get_current_weather and prints the result
def print_current_weather():
    current_weather = get_current_weather()
    print(f"The current weather is: {current_weather}")

# A test that uses patch to mock the get_current_weather function
@patch('__main__.get_current_weather')
def test_print_current_weather(mock_get_current_weather):
    # Configure the mock object to return a specific value
    mock_get_current_weather.return_value = "Rainy"
    
    # Call the function that we want to test
    print_current_weather()
    
    # Check that the function printed the correct output
    assert mock_get_current_weather.called
    # assert "Rainy" in mock_get_current_weather.call_args[0][0]
print("data")
print_current_weather()
test_print_current_weather()