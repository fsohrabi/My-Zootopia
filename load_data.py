import requests

FILE_HTML_PATH = "animals_template.html"
API_KEY = 'VQ2Jo/JzVAsiUR5qYQYrWA==8if53JokPGdnG3bz'

def load_animals_data(name ='Fox'):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return False


def load_html_template_data():
    """ Loads an HTML file """
    with open(FILE_HTML_PATH, "r") as handle:
        return handle.read()

