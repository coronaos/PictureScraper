import os
import requests

# URL base con un espacio reservado ({}) donde irá el número
base_url = (
    "https://ejemplos.com/wp-content/uploads/2024/04/hola-quetal-{}.jpg"
)

# Crear una carpeta para guardar las imágenes descargadas
output_dir = "imagenes_descargadas"
os.makedirs(output_dir, exist_ok=True)

# Bucle desde el 1 hasta el 179 (el 180 no se incluye, por lo que llega hasta el 179)
for i in range(1, 180):
  url = base_url.format(i)
  filename = os.path.join(output_dir, f"hola-quetal-{i}.jpg")

  try:
    response = requests.get(url, timeout=10)
    # Comprobamos si la imagen existe en el servidor (código 200 OK)
    if response.status_code == 200:
      with open(filename, "wb") as f:
        f.write(response.content)
      print(f"[Éxito] Descargada: {url}")
    else:
      print(f"[No encontrada] Código {response.status_code}: {url}")
  except Exception as e:
    print(f"[Error] No se pudo conectar con {url}: {e}")