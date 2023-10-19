
import requests
from decouple import config


def callback():
    # Get the callback URL from the environment file
    callback_url = config('CALLBACK_URL')

    # Perform the callback request here
    # Example using requests library:

    callback_data = {'status': 'completed'}
    response = requests.post(callback_url, data=callback_data)
    print(response.status_code)
    print(response.text)
    # Check the response status
    if response.status_code == 201:
        print("Callback successful")
    else:
        print("Callback failed")