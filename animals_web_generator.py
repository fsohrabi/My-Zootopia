import load_data
from write_data import write_data


def create_animals_info_string(animals_info):
    """
    Print the information of each animal from a list of dictionaries.

    Args:
        animals_info (list): A list of dictionaries containing animal information.
    """
    animals = ''
    for animal in animals_info:
        for key, value in animal.items():
            if value is not None:
                animals += f"{key}: {value}\n"
    return animals


def fetch_animals_info():
    """
    Fetch animal data and format it into a new structure.

    Returns:
        list: A list of dictionaries containing formatted animal information,
              including 'Name', 'Diet', 'Location', and 'Type'.
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
    template = load_data.load_html_template_data()
    animals_info = fetch_animals_info()
    animals_string = create_animals_info_string(animals_info)
    template = template.replace('__REPLACE_ANIMALS_INFO__',animals_string)
    return template


def main():
    """
    Main function to fetch animal information and print it.
    """
    template = create_animals_template()
    write_data(template)


if __name__ == "__main__":
    main()
