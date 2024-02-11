# This file contains the main functions used throughout the code.

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset(year):
    if year in {"2018", "2019", "2020"}:
        directorio_actual = os.path.dirname(__file__)
        ruta_dataset = os.path.join(directorio_actual, '..', 'datasets', f'water_{year}.csv')
        if os.path.exists(ruta_dataset):
            return pd.read_csv(ruta_dataset, header=0)
        else:
            print(f"El archivo water_{year}.csv no existe en el directorio datasets.")
            return None
    else:
        print("""El año proporcionado no es válido. Por favor seleccione uno de los siguientes años: "2018", "2019", "2020".""")
        return None