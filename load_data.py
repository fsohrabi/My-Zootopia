FILE_HTML_PATH = "animals_template.html"


def load_html_template_data():
    """ Loads an HTML file """
    with open(FILE_HTML_PATH, "r") as handle:
        return handle.read()

