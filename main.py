import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
# -----------------------------
# Funciones estadísticas
def calcular_media(valores):
    return round(np.mean(valores), 2)

def calcular_max(valores):
    return round(np.max(valores), 2)

def calcular_min(valores):
    return round(np.min(valores), 2)

def calcular_desviacion(valores):
    return round(np.std(valores, ddof=0), 2)  # desviación poblacional

def calcular_estadisticas(datos, clave):
    valores = np.array([d[clave] for d in datos])
    return {
        "media": calcular_media(valores),
        "max": calcular_max(valores),
        "min": calcular_min(valores),
        "desviacion": calcular_desviacion(valores)
    }

# -----------------------------
# Funciones de análisis y formato
def top_n(datos, clave, n=5, reverse=True):
    return sorted(datos, key=lambda d: d[clave], reverse=reverse)[:n]

def formato_fecha(fecha):
    """Convierte 'YYYY-MM-DD' a 'DD/MM/YY'"""
    año, mes, dia = fecha.split("-")
    return f"{dia}/{mes}/{año[2:]}"

def filtros(datos, clave, operador, valor):
    if operador == ">":
        return [d for d in datos if d[clave] > valor]
    elif operador == "<":
        return [d for d in datos if d[clave] < valor]
    elif operador == ">=":
        return [d for d in datos if d[clave] >= valor]
    elif operador == "<=":
        return [d for d in datos if d[clave] <= valor]
    elif operador == "==":
        return [d for d in datos if d[clave] == valor]
    else:
        return []

# -----------------------------
def main():
    # Crear carpeta de reportes si no existe
    os.makedirs("reportes", exist_ok=True)

    # Leer archivo JSON
    with open("datos/datosclima.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    # Cálculo de estadísticas
    estad_temp = calcular_estadisticas(datos, "temperatura")
    estad_lluvia = calcular_estadisticas(datos, "lluvia_mm")

    print("=== ESTADÍSTICAS GENERALES ===")
    print(f" Temperatura promedio: {estad_temp['media']}°C")
    print(f"   Máx: {estad_temp['max']}°C | Mín: {estad_temp['min']}°C | Desv: {estad_temp['desviacion']}")
    print(f" Lluvia promedio: {estad_lluvia['media']} mm")
    print(f"   Máx: {estad_lluvia['max']} mm | Mín: {estad_lluvia['min']} mm | Desv: {estad_lluvia['desviacion']}")
    print("------------------------------------")

    # Top 5 temperaturas altas y bajas
    top_temp_altas = top_n(datos, "temperatura", 5, reverse=True)
    top_temp_bajas = top_n(datos, "temperatura", 5, reverse=False)
    top_lluvias_altas = top_n(datos, "lluvia_mm", 5, reverse=True)
    top_lluvias_bajas = top_n(datos, "lluvia_mm", 5, reverse=False)

    print("\n Top 5 días más calurosos:")
    for d in top_temp_altas:
        print(f"{formato_fecha(d['fecha'])} → {d['temperatura']} °C")

    print("\n Top 5 días más fríos:")
    for d in top_temp_bajas:
        print(f"{formato_fecha(d['fecha'])} → {d['temperatura']} °C")

    print("\n Top 5 días con más lluvia:")
    for d in top_lluvias_altas:
        print(f"{formato_fecha(d['fecha'])} → {d['lluvia_mm']} mm")

    print("\n Top 5 días con menos lluvia:")
    for d in top_lluvias_bajas:
        print(f"{formato_fecha(d['fecha'])} → {d['lluvia_mm']} mm")

    # Filtros especiales
    dias_calor = filtros(datos, "temperatura", ">", 30)
    dias_frio = filtros(datos, "temperatura", "<=", 20)
    dias_lluvia_fuerte = filtros(datos, "lluvia_mm", ">=", 15)
    dias_sin_lluvia = filtros(datos, "lluvia_mm", "==", 0)

    print("\n Días con temperatura > 30°C:")
    for d in dias_calor:
        print(f"{formato_fecha(d['fecha'])} → {d['temperatura']} °C")

    print("\n Días con temperatura <= 20°C:")
    for d in dias_frio:
        print(f"{formato_fecha(d['fecha'])} → {d['temperatura']} °C")

    print("\n Días con lluvia >= 15 mm:")
    for d in dias_lluvia_fuerte:
        print(f"{formato_fecha(d['fecha'])} → {d['lluvia_mm']} mm")

    print("\n Días sin lluvia:")
    if dias_sin_lluvia:
        for d in dias_sin_lluvia:
            print(f"{formato_fecha(d['fecha'])}")
    else:
        print("No hubo días completamente secos en el periodo.")

    # -----------------------------
    # Creación del reporte CSV
    df = pd.DataFrame(datos)
    df.to_csv("reportes/reporte_clima.csv", index=False, encoding="utf-8-sig")
    print("\n Reporte CSV guardado en 'reportes/reporte_clima.csv'.")

    # -----------------------------
    # Generación del gráfico
    fechas = [d["fecha"] for d in datos]
    temp = [d["temperatura"] for d in datos]
    lluvia = [d["lluvia_mm"] for d in datos]

    plt.figure(figsize=(10,5))
    plt.plot(fechas, temp, color='red', marker='D', linestyle='--', linewidth=2, label="Temperatura (°C)")
    plt.plot(fechas, lluvia, color='blue', marker='o', linestyle='-', linewidth=2, label="Lluvia (mm)")
    plt.title("Reporte Climático - Ciudad Carcas (Septiembre 2025)")
    plt.xlabel("Fecha")
    plt.ylabel("Valores")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("reportes/grafico_clima.png")
    print(" Gráfico guardado como 'reportes/grafico_clima.png'.")

    print("\n Análisis completado exitosamente.")

# -----------------------------
if __name__ == "__main__":
    main()

