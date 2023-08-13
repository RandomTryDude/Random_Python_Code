import sqlite3

# Créer une connexion à la base de données (ou la créer si elle n'existe pas)
conn = sqlite3.connect('P.db')
cursor = conn.cursor()

# Créer la table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS MaTable (
        identifiant INT PRIMARY KEY,
        prenom TEXT,
        nom TEXT,
        ville TEXT
    )
''')

# Insérer des données dans la table
donnees = [
    (1, 'Pierre', 'Dupond', 'Paris'),
    (2, 'Sabrina', 'Durand', 'Nantes'),
    (3, 'Julien', 'Martin', 'Lyon'),
    (4, 'David', 'Bernard', 'Marseille'),
    (5, 'Marie', 'Leroy', 'Grenoble')
]

cursor.executemany('INSERT INTO MaTable (identifiant, prenom, nom, ville) VALUES (?, ?, ?, ?)', donnees)

# Valider les changements et fermer la connexion
conn.commit()
conn.close()
