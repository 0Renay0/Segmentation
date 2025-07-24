# **Segmentation de Séries Temporelles**

Ce projet a pour objectif de **segmenter des séries temporelles multivariées**, **détecter des ruptures structurelles** et **exporter les points de transition** dans le but d'utiliser ces points pour la construction de condition de garde dans le contexte d'un projet ayant pour but de faire la mise à jour d'automate hybride à temps réel.

## **Structure du dépôt**
```
.
|--- Segmentation.py         # Script principal
|--- Sources.py              # Fonctions principales
|--- Data/                   # Dossier contenant les fichiers.csv d'entrée
|--- Results/                # Dossier de sortie contenant les segments et les points de transition
|--- README.md               # Documentation du projet
```

## **Fontionnement**

### 1. **Chargement des données**
Les données doivent être au format CSV avec la structure suivante:
|    Time   |    Var1   |    Var2   |    Var3   |    ....   |
|--- 0.00   |:-: 12.3   |:-: 45.6  |:-: 1.55   |--: ....   |
|   0.01    |   12.4    |    45.7   |   1.6    |  ....     |
|    .   |    .   |   .    |   .    |    ....   |
|   1000    |   x    |    y   |   z    |   ....    |
