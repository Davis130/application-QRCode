import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")

label_choix = tk.Label(root, text = "veuillez faire un choix !")
label_choix.pack()

# Création de la iste des éléments du combobox

liste_etat = ["En stock","En cours d'utilisation"]
liste_sous_etats = ["A arbitrer",
"A livrer",
"A préparer",
"A rechercher",
"A réinitialiser",
"A sortir ",
"Disponible",
"En cours de RETEX",
"Maintenance IFG",
"Maintenance SAV",
"Réservé",
"Spare"
]

liste_motif_a_sortir = [
"A donner",
"A rendre au loueur",
"A vendre",
"A détruire",
"En cours de reprise",
"A rendre Mainteneur"
]

liste_motif_reserve = [
"Opportunité",
"Prêt",
"Projet",
"Revalorisation"
]

liste_entrepot_physique = [

]

liste_sites = [

]


# Création de l'objet combobox

liste_combo = ttk.Combobox(root, values = liste_motif_a_sortir)
liste_combo.pack()

root.mainloop()
