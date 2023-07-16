import os
from tkinter import Tk, filedialog
from PIL import Image

def convert_folder_to_webp(folder_path, output_folder_path):
    output_folder = os.path.join(output_folder_path, folder_path + "_webp")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            output_filename = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(output_folder, output_filename)

            image.save(output_path, "webp", lossless=True)
            print(f"Archivo convertido: {output_path}")

    print("¡Conversión completada!")

# Interfaz gráfica para seleccionar la carpeta y la ubicación de la carpeta de salida
root = Tk()
root.withdraw()  # Oculta la ventana principal

folder_path = filedialog.askdirectory(title="Seleccionar carpeta a convertir")
if folder_path:
    output_folder_path = filedialog.askdirectory(title="Seleccionar ubicación de la carpeta de salida")
    if output_folder_path:
        convert_folder_to_webp(folder_path, output_folder_path)
    else:
        print("No se seleccionó ninguna ubicación de carpeta de salida.")
else:
    print("No se seleccionó ninguna carpeta.")

