import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('synthetic_wtp_laptop_data.csv')

atual = {
    'Memory': '16',
    'Storage': '512',
    'CPU_class': '1',
    'Screen_size': '14.0',
    'year': '2025',
    'price': '111.000'
}

upgrade_option = {
    'Add 16 GB memory': '7,000',
    'Add 512 GB storage': '5,000',
    'Upgrade CPU class by 1 level': '15,000',
    'Increase screen size from 14 to 16 inches': '3,000',
}

X = df[['Memory',
        'Storage',
        'CPU_class',
        'Screen_size',
        'year',
        'price']]
