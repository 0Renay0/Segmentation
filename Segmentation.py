from Sources import *

# Paramètres
input_file = "Data/Q4_mode_degradation.csv"
segment_folder = "segments_from_csv"
k = 1.0  # Facteur de tolérance
MinPoints = 50  # Nombre minimum de points pour considérer un segment valide

# Chargement des données
t, x_cols, X = load_data(input_file)

#Calcil des seuils
thresholds = compute_thresholds(X, x_cols, k)

# Segmentation du signal
segments, rupture_logs, transition_points = segment_signal(t, X, x_cols, thresholds, MinPoints)

