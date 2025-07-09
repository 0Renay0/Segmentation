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

def compute_thresholds(X, k=1.0):
    """
    Calcule les seuils dynamiques pour chaque variable.
    """
    
    thresholds = k * np.std(X, axis=0)  # seuils 
    
    for i, col in enumerate(x_cols):
        print(f"[INFO] Seuil pour '{col}': {thresholds[i]:.4f}")
        
    return thresholds