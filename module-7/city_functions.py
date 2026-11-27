# Name: Ajanae Stanback
# Assignment: Module 7.2 - Test Cases
# Date: November 26, 2026
# Description: Format city and country with optional population and language.


def city_country(city, country, population=None, language=None):
    """Return formatted city and country information."""
    formatted_city = f"{city.title()}, {country.title()}"

    if population is not None:
        formatted_city += f" - population {population}"

    if language is not None:
        formatted_city += f", {language.title()}"

    return formatted_city


if __name__ == "__main__":
    print(city_country("Greensboro", "United States"))
    print(city_country("Paris", "France", 2100000))
    print(city_country("Santiago", "Chile", 5000000, "Spanish"))
