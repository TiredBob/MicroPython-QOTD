import requests
import json

def get_quote_of_the_day(api_url="https://zenquotes.io/api/today"):
    """
    Fetch the quote of the day from ZenQuotes.io.

    Args:
        api_url (str): The URL of the API to fetch the quote from. Defaults to 'https://zenquotes.io/api/today'.

    Returns:
        dict: A dictionary containing the quote and author, or an error message if the request fails.
    """
    try:
        response = requests.get(api_url)
        print(f"Status Code: {response.status_code}")  # Debugging: Print status code
        print(f"Response Content: {response.text}")    # Debugging: Print raw response content
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Use MicroPython-compatible JSON parsing
        data = json.loads(response.text)
        if data and isinstance(data, list):  # ZenQuotes returns a list of quotes
            quote_data = data[0]  # Get the first (and only) quote of the day
            return {"quote": quote_data.get("q"), "author": quote_data.get("a")}
        else:
            return {"error": "Unexpected API response format"}
    except Exception as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    result = get_quote_of_the_day()
    if "error" in result:
        print(f"Error fetching quote: {result['error']}")
    else:
        print(f"'{result['quote']}' - {result['author']}")
