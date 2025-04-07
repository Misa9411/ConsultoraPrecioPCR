import pandas as pd

# Leer el archivo Excel. Se asume que la fila 9 (índice 8 en 0-index) contiene los encabezados deseados.
ruta_archivo = r"C:\Users\misad\Downloads\LISTAPCR.xlsx"
df = pd.read_excel(ruta_archivo, header=8)

# Mostrar las primeras filas para confirmar la correcta lectura
print("Primeras filas del DataFrame:")
print(df.head())

# Convertir el DataFrame a formato JSON (lista de diccionarios)
json_data = df.to_json(orient="records", force_ascii=False)

# Guardar el JSON resultante en un archivo
ruta_json = r"C:\Users\misad\Downloads\Lista_de_precios.json"
with open(ruta_json, "w", encoding="utf-8") as f:
    f.write(json_data)

print(f"\nEl procesamiento se completó. El archivo JSON se ha guardado en: {ruta_json}")