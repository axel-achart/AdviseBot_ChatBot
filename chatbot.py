import requests, json


class ConnectToAPI:
    import requests
import json

class ConnectToAPI:
    def fetch_movies_by_genre_and_year(self, genre=None, year=None):
        """Cherche des films selon un genre et/ou une année en interrogeant l'API OMDb."""
        url = f'http://www.omdbapi.com/?apikey=d3053818&type=movie'

        # Ajouter les paramètres en fonction des entrées utilisateur
        if genre:
            url += f'&s={genre}'
        elif year:
            url += f'&y={year}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if 'Search' in data:
                # Filtrer et garder uniquement les informations utiles
                filtred_data = [
                    {key: movie.get(key, "N/A") for key in ["Title", "Year", "Genre"]}
                    for movie in data['Search']
                ]
                return filtred_data

        return []  # Retourne une liste vide si aucun résultat

    
    def write(self, filtred_data):
        # Enregistre les données JSON dans un fichier
        with open('data/api.json', 'w') as fichier:
            json.dump(filtred_data, fichier, indent=4)

    def read(self):
        """Lit les films enregistrés dans api.json"""
        try:
            with open('data/api.json', 'r') as fichier:
                contenu = fichier.read().strip()  # Supprime les espaces vides

                # Vérifie si le fichier est vide avant de le parser
                if not contenu:
                    return []

                return json.loads(contenu)  # Convertit en dictionnaire Python
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Retourne une liste vide en cas d'erreur
