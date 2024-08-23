import load_data
from write_data import write_data

def create_animals_info_string(animals_info):
    """
    Create a formatted string containing the information of each animal.

    Args:
        animals_info (list): A list of dictionaries with animal information.

    Returns:
        str: A formatted string with the details of each animal.
    """
    animals = ''
    for animal in animals_info:
        animals += '<li class="cards__item">'
        other_items_except_name = ''
        for key, value in animal.items():
            if key == "Name":
                animals += f'<div class="card__title"> {value}</div>'
            elif value is not None and key != "Name":
                other_items_except_name += f"<li>{key}: {value}</li>"
        animals += f' <p class="card__text"> <ul>{other_items_except_name}</ul></p></li>'
    return animals

def fetch_animals_info():
    """
    Fetch and format animal data into a list of dictionaries.

    Returns:
        list: A list of dictionaries with keys 'Name', 'Diet', 'Location', 'Type'.
    """
    animals_data = load_data.load_animals_data()
    new_animals_data_format = []
    for animal in animals_data:
        name = animal.get('name', None)
        diet = animal["characteristics"].get('diet', None)
        location = animal["locations"][0]
        animal_type = animal["characteristics"].get('type', None)
        new_animals_data_format.append({'Name': name, 'Diet': diet, 'Location': location, 'Type': animal_type})
    return new_animals_data_format

def create_animals_template():
    """
    Create an HTML template by embedding formatted animal information.

    Returns:
        str: An HTML string with animal information replacing a placeholder.
    """
    template = load_data.load_html_template_data()
    animals_info = fetch_animals_info()
    animals_string = create_animals_info_string(animals_info)
    template = template.replace('__REPLACE_ANIMALS_INFO__', animals_string)
    return template

def main():
    """
    Main function to generate an HTML template with animal information and write it to a file.
    """
    template = create_animals_template()
    write_data(template)

if __name__ == "__main__":
    main()
