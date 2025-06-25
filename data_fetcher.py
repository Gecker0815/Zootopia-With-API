import requests
import os
from dotenv import load_dotenv

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
        ...
        },
        'locations': [
        ...
        ],
        'characteristics': {
        ...
        }
    },
    """
    load_dotenv()

    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': os.getenv("API_KEY")})

    if response.status_code == requests.codes.ok:
        data = response.json()

        if data:
            return data
        else:
            return {"error": 404, "name": animal_name}
    else:
        return response.status_code