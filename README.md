# Automate_management

Développement du backend d’un logiciel de gestion pour une société gestionnaire de 15 distributeurs automatiques à Paris.

# Introduction

Ce document présente un ensemble de fonctions Python pour gérer
un système de machines distributrices. Les fonctions permettent d'effectuer
des opérations telles que la création de nouvelles machines, la mise à jour des
prix des produits, la vente de produits, le réapprovisionnement, le calcul des
revenus, la consultation des stocks et la détection des machines nécessitant un
réapprovisionnement. Le système est conçu pour gérer plusieurs machines
distributrices situées à divers endroits.

# Bibliothèques utilisées

Le code utilise plusieurs bibliothèques Python pour différentes tâches :

1. os: Cette bibliothèque est utilisée pour effectuer des opérations sur le
   système de fichiers, y compris la création de dossiers pour chaque
   machine, la gestion des fichiers de données et la détection des machines
   existantes.
2. json: La bibliothèque json est utilisée pour lire et écrire des données au
   format JSON. Elle est utilisée pour stocker les informations sur les
   transactions, les produits disponibles, et les prix des produits.
3. datetime: La bibliothèque datetime est utilisée pour gérer les dates et les
   heures, en particulier pour enregistrer la date et l'heure des ventes et des
   réapprovisionnements.
4. matplotlib.pyplot: Cette bibliothèque est utilisée pour générer des
   graphiques, en l'occurrence pour afficher les revenus.
5. numpy: La bibliothèque numpy est utilisée pour effectuer des opérations
   mathématiques, notamment pour calculer les revenus totaux.
6. random: La bibliothèque random est utilisée pour générer des
   coordonnées aléatoires pour les machines distributrices.
   Structure des données
   Le système utilise plusieurs fichiers JSON pour stocker différentes informations :
   • transaction_data: Contient des informations sur les transactions, y
   compris la date(t), l'identifiant du produit et le montant total du produit
   vendu à date t.
   • information_data: Stocke les informations sur les produits disponibles, y
   compris leur nom, quantité, et prix.
   • price_data: Contient les prix de chaque produit.

# Fonctions du système

Le système comprend les fonctions suivantes :

1. Add(ID): Cette fonction permet d'ajouter une nouvelle machine
   distributrice en créant un dossier pour la machine et en y enregistrant les
   données de transaction et d'information.
2. Repricing(XI, price): Permet de mettre à jour le prix d'un produit
   spécifique (défini par son identifiant XI) dans toutes les machines.
3. Sell(ID, Xi): Enregistre une vente d'un produit spécifique (Xi) dans une
   machine donnée (ID). Elle met à jour la quantité de produits disponibles,
   enregistre la transaction et le montant total de la vente.
4. Refill\_(ID, Xi, Date): Réapprovisionne un produit spécifique (Xi) dans une
   ou plusieurs machines (ID). Elle vérifie les niveaux de stock et
   réapprovisionne si nécessaire.
5. Revenues(ID, Xi, Date_start, Date_end): Calcule les revenus totaux pour
   un produit spécifique (Xi) sur une période donnée, dans une ou plusieurs
   machines (ID). Elle génère également un graphique des revenus.
6. Available(ID, Xi): Consulte la disponibilité des produits (Xi) dans une ou
   plusieurs machines (ID) et affiche le pourcentage de produits disponibles.
7. Scan_to_refill(percentage, Xi): Détecte les machines dont le stock est
   inférieur à un pourcentage spécifié et génère une liste des produits
   nécessitant un réapprovisionnement.
