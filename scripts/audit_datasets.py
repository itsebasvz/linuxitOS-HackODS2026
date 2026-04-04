import pandas as pd
import numpy as np

print("--- AUDITORÍA DE DATOS: FINAL_MERGED_DATA.CSV ---")
df = pd.read_csv("datos/final_merged_data.csv")

print(f"Total de registros (Municipios): {len(df)}")
print("\n1. Nulos por columna:")
print(df.isnull().sum())

print("\n2. Rango de valores críticos:")
print(df[['Pobreza_pct', 'Pobreza_extrema_pct', 'Carencia_servicios_pct', 'carencia_agua_conagua_pct', 'pct_rural']].describe().T[['min', 'max', 'mean']])

print("\n3. Auditoría de la Anomalía Financiera (SHCP vs CONAGUA/CONEVAL):")
# Buscando municipios con alta carencia de agua (>90%) y recaudación > 0
anomalias = df[(df['carencia_agua_conagua_pct'] > 90) & (df['monto_agua'] > 0)]
print(f"Municipios con >90% carencia de agua de CONAGUA y monto_agua > 0: {len(anomalias)}")
if len(anomalias) > 0:
    print(anomalias[['Municipio', 'carencia_agua_conagua_pct', 'monto_agua', 'tomas_pagadas']].head())

print("\nRevisión alternativa usando CONEVAL (Carencia_servicios_pct > 95%):")
anomalias_coneval = df[(df['Carencia_servicios_pct'] > 95) & (df['monto_agua'] > 0)]
print(f"Municipios con >95% carencia servicios CONEVAL y monto_agua > 0: {len(anomalias_coneval)}")

print("\n4. Verificación de SHCP:")
df_shcp = pd.read_csv("datos/derecho_agua_municipal.csv")
print("Años en dataset SHCP original:", df_shcp['anio'].unique() if 'anio' in df_shcp.columns else "Sin columna de año visible")
