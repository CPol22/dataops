import pandas as pd
import matplotlib.pyplot as plt
import os
import json

# -----------------------------
# Crear carpeta de reportes si no existe
os.makedirs("reportes", exist_ok=True)

# -----------------------------
# Lectura de datos JSON → DataFrame
with open("datos/datosclima.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

df = pd.DataFrame(datos)
df["fecha"] = pd.to_datetime(df["fecha"])  # convertir a formato de fecha

# -----------------------------
# Generación del gráfico (usando directamente columnas del DataFrame)
plt.figure(figsize=(10,5))
plt.plot(df["fecha"], df["temperatura"], color='red', marker='D', linestyle='--', linewidth=2, label="Temperatura (°C)")
plt.plot(df["fecha"], df["lluvia_mm"], color='blue', marker='o', linestyle='-', linewidth=2, label="Lluvia (mm)")
plt.title("Reporte Climático - Ciudad Carcas (Septiembre 2025)")
plt.xlabel("Fecha")
plt.ylabel("Valores")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# -----------------------------
# Guardar gráfico
plt.savefig("reportes/grafico_clima.png")
print("📊 Gráfico guardado como 'reportes/grafico_clima.png'.")

print("\n✅ Análisis completado exitosamente.")
