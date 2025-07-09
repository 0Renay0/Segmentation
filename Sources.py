import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(input_file):
    """
    Charge les données depuis un fichier CSV.
    """
    
    df = pd.read_csv(input_file)
    t = df["Time"].values
    x_cols = [col for col in df.columns if col != "Time"]
    X = df[x_cols].values  # shape (N, D)
    return t, x_cols, X

def compute_thresholds(X, x_cols, k=1.0):
    """
    Calcule les seuils dynamiques pour chaque variable.
    """
    
    thresholds = k * np.std(X, axis=0)  # seuils 
    
    for i, col in enumerate(x_cols):
        print(f"[INFO] Seuil pour '{col}': {thresholds[i]:.4f}")
        
    return thresholds

def segment_signal(t, X, x_cols, thresholds, MinPoints=3):
    """
    Segmente le signal en détectant les ruptures.
    """
    
    segments = []
    rupture_logs = []
    transition_points = []
    
    current_t = [t[0], t[1]]
    current_X = [X[0], X[1]]
    
    for i in range(2, len(t)):
        time = np.array(current_t)
        X_data = np.array(current_X)
        
        rupture_detected = False
        rupture_info = {}
        
        for d in range(X_data.shape[1]):
            y = X_data[:,d]
            A = np.vstack([time, np.ones(len(time))]).T
            coeffs = np.linalg.lstsq(A, y, rcond=None)[0]
            y_pred = coeffs[0] * t[i] + coeffs[1]
            error = abs(X[i, d] - y_pred)
            
            if error > thresholds[d]:
                rupture_detected = True
                rupture_info = {
                    "segment_index": len(segments) + 1,
                    "time": t[i],
                    "variable": x_cols[d],
                    "error": error,
                    "threshold": thresholds[d],
                    "value": X[i, d],
                    "predicted": y_pred,
                    "a": coeffs[0],
                    "b": coeffs[1],
                }
                break
            
            if rupture_detected:
                if len(current_t) >= MinPoints:
                    # On sauvegarde le dernier point avant la rupture
                    transition_points.append({
                        "time": t[i-1],
                        "variable": rupture_info["variable"],
                        "value": X[i-1, x_cols.index(rupture_info["variable"])]
                    })
                    segments.append((np.array(current_t), np.array(current_X)))
                    rupture_logs.append(rupture_info)
                    current_t = [t[i-1], t[i]]
                    current_X = [X[i-1], X[i]]
                else:
                    # Trop court : on fusionne avec le prochain segment
                    current_t.append(t[i])
                    current_X.append(X[i])
            else:
                current_t.append(t[i])
                current_X.append(X[i])
    segments.append((np.array(current_t), np.array(current_X)))
    return segments, rupture_logs, transition_points