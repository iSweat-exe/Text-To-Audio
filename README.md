# Text to Audio

Text to Audio est un programme Python qui vous permet de convertir du texte en fichier audio. Il utilise la bibliothèque gtts pour générer l'audio et playsound pour le lire.

# Installation
## Prérequis
Python 3.x doit être installé sur votre système. Vous pouvez le télécharger à partir du site officiel : https://www.python.org/downloads/

Étapes

**Clonez** le dépôt ou **téléchargez** le *fichier source*.
Ouvrez un **terminal** ***dans le répertoire racine du projet***.
Installez les dépendances en exécutant la commande suivante : **pip install -r requirements.txt**
Pour lancer le programme, **exécutez** la commande suivante : **python interfacebeta.py**
# Comment utiliser
Entrez le texte que vous souhaitez convertir en audio dans le champ **"Entrez le texte à convertir en audio"**.
Entrez le nom de fichier souhaité (***sans l'extension .mp3***) dans le champ "**Entrez le nom du fichier audio**".
Cliquez sur le bouton "**Générer l'audio**" pour générer le fichier **audio**.
Le fichier audio sera enregistré dans le **même dossier** que le fichier interfacebeta.py.

# Transformation en .exe
## Prérequis
**PyInstaller** doit être installé sur votre système. Si ce n'est pas le cas, vous pouvez l'installer en exécutant la commande suivante : **pip install pyinstaller**

### Étapes

Ouvrez un terminal **dans le répertoire racine du projet**.
Exécutez la commande suivante : **pyinstaller *--onefile* *-noconsole* interfacebeta.py**
Le fichier **.exe** sera généré dans le dossier **dist**.

## Remarque

Le programme génère un **fichier audio au format MP3**. Si vous souhaitez **modifier le format**, vous pouvez le faire en modifiant l'extension **dans la ligne suivante** :

nom_fichier_mp3 = nom_fichier + ".mp3"