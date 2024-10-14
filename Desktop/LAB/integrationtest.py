import requests

def fetch_data(url):
    """Fetch JSON data from the given URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def validate_json_structure(data):
    """Check if the JSON response is a list and if 'id' and 'name' are unique."""
    if not isinstance(data, list):
        print("Response is not a list.")
        return False

    ids = set()
    names = set()

    for item in data:
        if 'id' not in item or 'name' not in item:
            print("Item is missing 'id' or 'name'.")
            return False

        ids.add(item['id'])
        names.add(item['name'])

    # Check uniqueness
    if len(ids) != len(data):
        print("Duplicate 'id' found!")
        return False
    if len(names) != len(data):
        print("Duplicate 'name' found!")
        return False

    print("Response is a valid list with unique 'id' and 'name'.")
    return True

if __name__ == "__main__":
    url = 'https://60a21d3f745cd70017576092.mockapi.io/api/v1/repos'

    try:
        data = fetch_data(url)
        result = validate_json_structure(data)
        if result:
            print("Integration Test Passed: JSON structure is valid and unique.")
        else:
            print("Integration Test Failed: JSON structure is not valid.")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
