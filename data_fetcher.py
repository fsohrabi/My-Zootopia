
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def load_animals_data(name ='Fox'):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return False
    

def fetch_data(animal_name):
    """
    Fetch and format animal data into a list of dictionaries.

    Returns:
        list: A list of dictionaries with keys 'Name', 'Diet', 'Location', 'Type'.
    """
    animals_data = load_animals_data(animal_name)
    if not animals_data:
        raise ValueError("Failed to fetch animal data from API")
    new_animals_data_format = []
    for animal in animals_data:
        name = animal.get('name', None)
        diet = animal["characteristics"].get('diet', None)
        location = animal["locations"][0]
        animal_type = animal["characteristics"].get('type', None)
        new_animals_data_format.append({'Name': name, 'Diet': diet, 'Location': location, 'Type': animal_type})
    return new_animals_data_format