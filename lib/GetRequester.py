import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
            return response.content  # Return bytes instead of text
        except requests.exceptions.RequestException as e:
            print(f"Error making GET request: {e}")
            return None

    def load_json(self):
        response_body = self.get_response_body()
        if response_body:
            try:
                return json.loads(response_body)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return None
        else:
            return None