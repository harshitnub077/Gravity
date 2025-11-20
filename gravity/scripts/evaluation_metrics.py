# Evaluation metric functions
import numpy as np

def relative_l2_error(y_true, y_pred):
    diff = np.linalg.norm(y_true - y_pred)
    norm = np.linalg.norm(y_true)
    return float(diff / (norm + 1e-8))

def mean_squared_error(y_true, y_pred):
    return float(np.mean((y_true - y_pred) ** 2))
