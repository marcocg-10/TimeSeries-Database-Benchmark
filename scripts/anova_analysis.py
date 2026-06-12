import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

df = pd.read_csv("/content/drive/MyDrive/Results/Stage3/datos_completos.csv")

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

df.rename(columns={
    "Tiempo_simple_ms": "TiempoSimple",
    "Tiempo_agregado_ms": "TiempoAgregado",
    "Throughput_req_s": "Throughput",
    "Base_de_datos": "Motor",
    "Tamaño": "Tamano"
}, inplace=True)

# ================================
# ANOVA Tiempo Simple
# ================================
modelo_simple = ols('TiempoSimple ~ Motor * Tamano', data=df).fit()
anova_simple = sm.stats.anova_lm(modelo_simple, typ=2)
print("\n=== ANOVA - Tiempo Simple ===")
print(anova_simple)

print("\n--- Tukey Tiempo Simple (Motor) ---")
print(pairwise_tukeyhsd(df["TiempoSimple"], df["Motor"]))

print("\n--- Tukey Tiempo Simple (Tamaño) ---")
print(pairwise_tukeyhsd(df["TiempoSimple"], df["Tamano"]))


# ================================
# ANOVA Tiempo Agregado
# ================================
modelo_ag = ols('TiempoAgregado ~ Motor * Tamano', data=df).fit()
anova_ag = sm.stats.anova_lm(modelo_ag, typ=2)
print("\n=== ANOVA - Tiempo Agregado ===")
print(anova_ag)

print("\n--- Tukey Tiempo Agregado (Motor) ---")
print(pairwise_tukeyhsd(df["TiempoAgregado"], df["Motor"]))

print("\n--- Tukey Tiempo Agregado (Tamaño) ---")
print(pairwise_tukeyhsd(df["TiempoAgregado"], df["Tamano"]))


# ================================
# ANOVA Throughput
# ================================
modelo_thr = ols('Throughput ~ Motor * Tamano', data=df).fit()
anova_thr = sm.stats.anova_lm(modelo_thr, typ=2)
print("\n=== ANOVA - Throughput ===")
print(anova_thr)

print("\n--- Tukey Throughput (Motor) ---")
print(pairwise_tukeyhsd(df["Throughput"], df["Motor"]))

print("\n--- Tukey Throughput (Tamaño) ---")
print(pairwise_tukeyhsd(df["Throughput"], df["Tamano"]))
