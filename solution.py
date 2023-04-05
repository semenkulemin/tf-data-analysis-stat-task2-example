import pandas as pd
import numpy as np

# from scipy.stats import norm
# from scipy.stats import chi2
from scipy.stats import expon

chat_id = 341395919 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x = x / 25
    alpha = 1 - p
    left = min(1/2 - expon.ppf(alpha) / (n * (min(x) / 5**2)), 1/2 - expon.ppf(1 - alpha) / (n * (min_x / 5**2)))
    right = max(1/2 - expon.ppf(alpha) / (n * (min(x) / 5**2)), 1/2 - expon.ppf(1 - alpha) / (n * (min_x / 5**2)))
    return left, right
    
#     alpha = 1 - p
#     loc = x.mean()
#     scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
#     return loc - scale * norm.ppf(1 - alpha / 2), \
#            loc - scale * norm.ppf(alpha / 2)
