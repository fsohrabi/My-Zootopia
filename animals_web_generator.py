import load_data
from data_fetcher import fetch_data
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
    

def create_animals_template():
    """
    Create an HTML template by embedding formatted animal information.

    Returns:
        str: An HTML string with animal information replacing a placeholder.
    """
    try:
        animal_name = input('Enter a name of an animal: ')
        template = load_data.load_html_template_data()
        animals_info = fetch_data(animal_name)  # This could raise an exception if data fetching fails
        animals_string = create_animals_info_string(animals_info)
        template = template.replace('__REPLACE_ANIMALS_INFO__', animals_string)
        print('Website was successfully generated to the file animals.html.')
        return template
    except Exception as e:
        print(f"An error occurred: {e}")
        return f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'


def main():
    """
    Main function to generate an HTML template with animal information and write it to a file.
    """
    template = create_animals_template()
    write_data(template)

if __name__ == "__main__":
    main()
