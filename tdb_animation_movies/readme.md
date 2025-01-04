# Tableau de Bord Power BI pour l'Analyse des Résultats des Films d'Animation et des Films (2000+)

Ce projet a pour objectif de créer un tableau de bord interactif sur Power BI permettant d’analyser les performances des films d’animation et des films sortis à partir des années 2000. Les données utilisées proviennent de l'API **The Movie Database (TMDb)**, et le processus inclut l'extraction, la transformation et la visualisation des données.

---

## Fonctionnalités Principales

- **Extraction des données** : Utilisation d'un algorithme Python pour interagir avec l'API TMDb et récupérer les données sous format JSON.
- **Transformation des données** : Nettoyage et mise en forme des données pour les convertir au format CSV exploitable dans Power BI.
- **Création d'un tableau de bord Power BI** : Visualisation des métriques clés comme le budget, les revenus, la rentabilité et les genres des films.

---

## Détail des Étapes du Projet

### 1. **Extraction des Données**
Un algorithme Python a été développé pour interagir avec l'API TMDb. Il permet de :
- Récupérer des informations détaillées sur les films (métadonnées, genres, sociétés de production, pays d'origine, etc.).
- Sauvegarder ces données au format JSON pour une manipulation ultérieure.

### 2. **Transformation des Données**
Les données JSON ont été transformées afin de :
- Permettre de rendre exploitables les données imbriqués comme le genre, le pays d'origine ou encore la société de production.
- Structurer les informations pour obtenir un fichier CSV prêt à être utilisé dans Power BI.
- Les colonnes suivantes ont été générées : 
  - **budget** : Budget du film (en dollars).
  - **original_language** : Langue originale du film.
  - **original_title** : Titre original.
  - **release_date** : Date de sortie.
  - **revenue** : Revenus générés (en dollars).
  - **runtime** : Durée du film (en minutes).
  - **tagline** : Slogan du film.
  - **title** : Titre traduit.
  - **vote_average** : Note moyenne des spectateurs.
  - **vote_count** : Nombre de votes des spectateurs.
  - **id_genres** et **name_genres** : Identifiants et noms des genres.
  - **name_production_companies** et **id_production_companies** : Sociétés de production.
  - **origin_country_production_companies** : Pays d'origine des sociétés de production.
  - **name_production_countries** : Pays de production.

### 3. **Création du Tableau de Bord**
Un tableau de bord interactif a été développé sur Power BI pour analyser les performances des films d’animation selon plusieurs dimensions. Les principales fonctionnalités et visualisations sont :

    Indicateurs clés :
        Chiffre d’affaire total : Affiché en haut sous forme de carte ($3,34Md dans l'exemple).
        Bénéfice moyen : Affiché en haut sous forme de carte ($85,59M dans l'exemple).
        Budget moyen : Affiché en haut sous forme de carte (40,55M dans l'exemple).
        Rentabilité moyenne : Exprimée en pourcentage (-97,37% dans l'exemple).
        Nombre total de films : Indiqué également en haut (34 films dans l'exemple).

    Filtrage interactif :
        Par compagnie de production (exemple : "Disney").
        Par plage d'années (exemple : 2000 - 2023).
        Par statut de rentabilité (rentable ou non rentable).
        Par métrique de visualisation (bénéfice, budget, chiffre d’affaires ou nombre de films).

    Graphiques dynamiques :
        Évolution dans le temps par année : Un graphique en barres qui illustre le nombre de films produits chaque année, avec des événements majeurs (COVID, crise financière de 2008, etc.) mis en évidence.
        Top/Flop des Films : Liste des films avec leur rentabilité respective.
        Top/Flop des Compagnies : Liste des compagnies de production classées par leur rentabilité.
        Répartition des bénéfices selon le genre : Un graphique circulaire (ou en anneau) qui montre la part des bénéfices par genre de film (exemple : Familial 44,43%, Aventure 39,93%, Autres 15,64%).
        Rentabilité selon la durée des films : Un graphique en barres horizontales qui compare la rentabilité des films en fonction de leur durée (exemple : moins de 60 minutes, entre 60 et 90 minutes, ou entre 90 et 120 minutes).

---

## Technologies Utilisées

- **Python** : Pour l'extraction et la transformation des données.
  - Librairies clés : `requests`, `json`, `pandas`.
- **API TMDb** : Pour récupérer les données des films.
- **Power BI** : Pour la visualisation des données et la création du tableau de bord.

---

## Prérequis

### 1. Clés et Configuration
Pour utiliser l'algorithme Python d'extraction, vous aurez besoin :
- D'une clé API TMDb.
- D'installer les dépendances listées dans le fichier `requirements.txt`.

### 2. Données Transformées
Le fichier CSV généré (via l'étape de transformation) doit être disponible pour l'importation dans Power BI. (directement disponible dans le dossier static/data_animation.csv )

---

## Instructions d'Utilisation

### 1. Extraction et Transformation
1. Clonez ce dépôt :  
   ```bash
   git clone <url_du_dépôt>
   cd <nom_du_dossier>
   ```
2. Exécutez l'algorithme Python pour extraire les données :  
   ```bash
   python extract_data.py
   ```
3. Lancez le script de transformation des données :  
   ```bash
   python transform_data.py
   ```

### 2. Importation dans Power BI
1. Modifiez la source du fichier pour qu'elle corresponde à votre fichier CSV généré.
2. Connectez les différentes visualisations et configurez les filtres.
3. Publiez le tableau de bord pour un partage ou une collaboration.

---

## Auteurs

- **Alyssa DERENSY-GUY**  
  Créateur et développeur du projet.  


---

