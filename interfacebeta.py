from gtts import gTTS
from playsound import playsound
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

# Fonction appelée lorsque le bouton est cliqué
def generer_audio():
    texte = texte_entree.get()
    tts = gTTS(texte, lang='fr')
    nom_fichier = nom_fichier_entree.get()
    nom_fichier_mp3 = nom_fichier + ".mp3"  # Ajouter l'extension ".mp3" ou la modifié
    tts.save(nom_fichier_mp3)  # Enregistrer le fichier avec l'extension ".mp3"
    message_confirmation.config(text="Fichier audio généré avec succès !", fg="green")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Text to Audio by iSweatCode")

# Ajouter un label pour le champ de texte
texte_label = tk.Label(fenetre, text="Entrez le texte à convertir en audio :", font=("Arial", 14, tk.font.BOLD), padx=25, pady=25)
texte_label.pack()

# Ajouter un champ de texte pour entrer le texte
texte_entree = tk.Entry(fenetre, width=75, borderwidth=1, font=("Arial", 14))
texte_entree.pack()

# Ajouter un label pour le champ de nom de fichier
nom_fichier_label = tk.Label(fenetre, text="Entrez le nom du fichier audio (merci de ne pas mettre l'extension .mp3) :", font=("Arial", 14, tk.font.BOLD))
nom_fichier_label.pack()

# Ajouter un champ de texte pour entrer le nom du fichier de sortie
nom_fichier_entree = tk.Entry(fenetre, width=75, borderwidth=1, font=("Arial", 14))
nom_fichier_entree.pack()

# Ajouter un bouton pour générer l'audio
bouton_generer = tk.Button(fenetre, text="Générer l'audio", command=generer_audio, bg="#007bff", fg="white", borderwidth=1, padx=10, pady=5)
bouton_generer.pack(pady=10)

# Ajouter un message de confirmation
message_confirmation = tk.Label(fenetre, text="", font=("Arial", 14))
message_confirmation.pack()

# Lancer la fenêtre principale
fenetre.mainloop()
