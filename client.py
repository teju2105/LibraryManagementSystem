import requests

# Define the narrative to be processed
narrative = 'This is a Library that has Book and Member.'

# Define the request payload as a JSON object
payload = {'narrative': narrative}

# Make a POST request to the server
try:
    # Use the correct endpoint and HTTP method
    response = requests.post('http://localhost:5000/extract', json=payload)

    # Check the status code of the response
    response.raise_for_status()

    # Print the response content
    print(response.json())

except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)
