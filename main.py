
from swapi import swapi, get_person


def get_films_info(film_id):
    film = swapi.get_film(film_id)
    print (f"Фільм:{film.title}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    film_id = input('введіть ідентифікатор фільму:')
    get_films_info(film_id)

