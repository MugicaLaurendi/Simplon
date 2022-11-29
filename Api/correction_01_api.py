# recuperer le csv
# recuperer la colonne "github name" dans le csv
# initialiser un dictionnaire
# Pour chaque nom dans github name
    # on creer l'url a partir de "nom"
    # on recupere le json sur l'api github
    # on recupere le "name" dans le json qu'on stock dans une variable
    # on transforme en Title la variable
    # on ajoute au dictionnaire le couple "github name" comme clé et la valeur comme valeur

#afficher le dictionnaire

import pandas as pd
import requests as req


user_names = pd.read_csv("akinator.csv")
print(user_names)
user_names.dropna(subset = ["github name"], inplace= True)
print(user_names)
user_names = user_names["github name"].tolist()

github_id = {}

for user_name in user_names :
    #if type(user_name) == float : continue

    url = f"https://api.github.com/users/{user_name}"

    response_api = req.get(url).json()

    full_name = response_api["name"]

    full_name = full_name.title()

    github_id[user_name] = full_name

print(github_id)
