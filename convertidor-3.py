import os
from tkinter import Tk, filedialog, messagebox
from PIL import Image

def convert_folder_to_webp(folder_path, output_folder_path):
    output_folder = os.path.join(output_folder_path, os.path.basename(folder_path) + "_webp")
    os.makedirs(output_folder, exist_ok=True)

    converted_files = []  # Lista para almacenar los nombres de los archivos convertidos

    file_count = len([filename for filename in os.listdir(folder_path) if filename.endswith((".png", ".jpg"))])

    for index, filename in enumerate(os.listdir(folder_path)):
        if filename.endswith((".png", ".jpg")):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            output_filename = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(output_folder, output_filename)

            image.save(output_path, "webp", lossless=True)
            converted_files.append(output_filename)

    if converted_files:
        message = "Archivos convertidos:\n" + "\n".join(converted_files)
    else:
        message = "No se encontraron archivos para convertir."

    message += "\n\nCarpeta de salida:\n" + output_folder
    messagebox.showinfo("Conversión completada", message)

def main():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal

    folder_path = filedialog.askdirectory(title="Seleccionar carpeta a convertir")
    if folder_path:
        output_folder_path = filedialog.askdirectory(title="Seleccionar ubicación de la carpeta de salida")
        if output_folder_path:
            convert_folder_to_webp(folder_path, output_folder_path)
        else:
            messagebox.showwarning("Error", "No se seleccionó ninguna ubicación de carpeta de salida.")
    else:
        messagebox.showwarning("Error", "No se seleccionó ninguna carpeta.")

    root.mainloop()

# Ejecutar el programa
main()
