import json

FILE_JSON_PATH = "animals_data.json"
FILE_HTML_PATH = "animals_template.html"


def load_animals_data():
    """ Loads a JSON file """
    with open(FILE_JSON_PATH, "r") as handle:
        return json.load(handle)


def load_html_template_data():
    """ Loads a HTML file """
    with open(FILE_HTML_PATH, "r") as handle:
        return handle.read()
