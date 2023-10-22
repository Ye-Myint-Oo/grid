
import requests
from decouple import config


def callback(call_back_url):
    # Get the callback URL from the environment file
    if call_back_url==None:
        callback_url = config('CALLBACK_URL')
    else:
        callback_url=call_back_url
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