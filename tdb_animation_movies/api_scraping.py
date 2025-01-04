import requests
import json
import time

# URL de base pour récupérer les films d'animation
base_url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=fr-FR&sort_by=popularity.desc&with_genres=16&release_date.gte=2000-01-01&page="


headers = {
    "accept": "application/json",
    "Authorization": "Bearer ACCESS TOKEN"
}

# Initialisation des variables
page = 1
all_movies = []

# Récupérer la première page pour savoir combien de pages il y a au total
response = requests.get(base_url + str(page), headers=headers)

if response.status_code != 200:
    print(f"Erreur lors de la requête : {response.status_code} - {response.text}")
else:
    data = response.json()
    total_pages = data.get('total_pages', 1)

    # Ajouter les résultats de la première page
    all_movies.extend(data.get('results', []))

    # Boucle pour récupérer toutes les pages (limite de 500 par l'API)
    for page in range(2, total_pages + 1):
        response = requests.get(base_url + str(page), headers=headers)
        
        if response.status_code != 200:
            print(f"Erreur lors de la requête à la page {page} : {response.status_code} - {response.text}")
            continue
        
        data = response.json()
        
        # Ajoutez les films de chaque page
        all_movies.extend(data.get('results', []))
        print(f"Page {page} récupérée sur {total_pages}")

# Sauvegarder tous les films dans un fichier JSON
with open("films_animation_complet.json", "w") as file:
    json.dump(all_movies, file, indent=4)

print(f"Tous les films d'animation (jusqu'à 500 pages) ont été sauvegardés dans 'films_animation_complet.json'")

movie_details = []


#Utilisation des id des films pour récupérer les détails de chaque film
for movie in all_movies:
    movie_id = movie['id']
    details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=fr-FR"
    
    # Envoyer une requête pour obtenir les détails du film
    details_response = requests.get(details_url, headers=headers)
    
    if details_response.status_code == 200:
        movie_details.append(details_response.json())
        print(f"Détails du film ID {movie_id} récupérés.")
    else:
        print(f"Erreur pour récupérer les détails du film ID {movie_id}: {details_response.status_code}")
    
    # Pause pour éviter de dépasser le quota de l'API
    time.sleep(0.2)

# Sauvegarder tous les détails dans un fichier JSON
with open("films_animation_complet_détails.json", "w") as file:
    json.dump(movie_details, file, indent=4)

print(f"Tous les détails des films ont été sauvegardés dans 'films_animation_complet_détails.json'")

