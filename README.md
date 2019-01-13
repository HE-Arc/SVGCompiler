# Pre-requis
- python 3.6
- pip
- bibliothèques externes:
    - ply 3.11
    - pydot 1.4.1
- un navigateur pour visualiser les documents SVG

# Comment installer SVGCompiler ?
1. `git clone https://github.com/HE-Arc/SVGCompiler.git` ou extraire l'archive contenant le code source
2. depuis la racine du code source: `pip install -r requirements.txt`

# Comment utiliser SVGCompiler ?
1. Créer un fichier source contenant du code de notre langage ou utiliser le fichier d'exemple fournis (`exemples/all_instructions.phvg`)
2. Executer `synthese.py` dans la ligne de commande avec comme argument le chemin vers le fichier source (p. ex `./synthese.py exemples/all_instructions.phvg`)
3. Ouvrir le fichier `.svg` généré dans votre navigateur préféré pour admirer le résultat (remarque: chaque portion de code délimitée avec des accolades donnera un fichier différent, p. ex pour le fichier `exemples/all_instructions.phvg` il y aura 3 fichiers `.svg` générés)
