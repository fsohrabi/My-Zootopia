from load_data import load_data


def print_animals_info(animals_info):
    """
    Print the information of each animal from a list of dictionaries.

    Args:
        animals_info (list): A list of dictionaries containing animal information.
    """
    for animal in animals_info:
        for key, value in animal.items():
            if value is not None:
                print(f"{key}: {value}")
        print()


def fetch_animals_info():
    """
    Fetch animal data and format it into a new structure.

    Returns:
        list: A list of dictionaries containing formatted animal information,
              including 'Name', 'Diet', 'Location', and 'Type'.
    """
    animals_data = load_data()
    new_animals_data_format = []
    for animal in animals_data:
        name = animal.get('name', None)
        diet = animal["characteristics"].get('diet', None)
        location = animal["locations"][0]
        animal_type = animal["characteristics"].get('type', None)
        new_animals_data_format.append({'Name': name, 'Diet': diet, 'Location': location, 'Type': animal_type})
    return new_animals_data_format


def main():
    """
    Main function to fetch animal information and print it.
    """
    animals_info = fetch_animals_info()
    print_animals_info(animals_info)


if __name__ == "__main__":
    main()
