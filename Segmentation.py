from Sources import (load_data,  # type: ignore
                     compute_thresholds, 
                     segment_signal, 
                     save_segments, 
                     save_transition_points, 
                     logs, plot_segments) 

# Paramètres
input_file = "Data/engine_timing.csv"
segment_folder = "Engine_Timing_Results"
k = 1.0  # Facteur de tolérance
MinPoints = 50  # Nombre minimum de points pour considérer un segment valide

# Chargement des données
t, x_cols, X = load_data(input_file)

#Calcil des seuils
thresholds = compute_thresholds(X, x_cols, k)

# Segmentation du signal
segments, rupture_logs, transition_points = segment_signal(t, X, x_cols, thresholds, MinPoints)

# Sauvegarde des segments
save_segments(segments, x_cols, segment_folder)

# Sauvegarde des points de transition
save_transition_points(transition_points, segment_folder)

# Logs des ruptures
logs(rupture_logs)

# Affichage 
plot_segments(segments, x_cols)