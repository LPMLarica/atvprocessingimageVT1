import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import time
import os

def average_method(r, g, b):
    return int((r + g + b) / 3)


def luminosity_method(r, g, b):
    return int(0.21 * r + 0.72 * g + 0.07 * b)


def desaturation_method(r, g, b):
    return int((max(r, g, b) + min(r, g, b)) / 2)


#Image processing function

def convert_image(image_path, method_name):
    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    pixels = img.load()

    new_img = Image.new("L", (width, height))
    new_pixels = new_img.load()

    start_time = time.perf_counter()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            if method_name == "Average":
                gray = average_method(r, g, b)
            elif method_name == "Luminosity":
                gray = luminosity_method(r, g, b)
            elif method_name == "Desaturation":
                gray = desaturation_method(r, g, b)

            new_pixels[x, y] = gray

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    # Saving the new image
    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)
    output_name = f"{name}_{method_name.lower()}.png"
    new_img.save(output_name)

    return new_img, execution_time, output_name

# Grafic interface

class GrayScaleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor para Escala de Cinza")

        self.image_path = None

        self.label = tk.Label(root, text="Selecione uma imagem e o método:")
        self.label.pack(pady=10)

        self.btn_select = tk.Button(root, text="Selecionar Imagem", command=self.select_image)
        self.btn_select.pack(pady=5)

        self.method_var = tk.StringVar(value="Average")

        methods = ["Average", "Luminosity", "Desaturation"]
        for method in methods:
            tk.Radiobutton(root, text=method, variable=self.method_var, value=method).pack()

        self.btn_convert = tk.Button(root, text="Converter", command=self.convert)
        self.btn_convert.pack(pady=10)

        self.timer_label = tk.Label(root, text="")
        self.timer_label.pack(pady=5)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if self.image_path:
            messagebox.showinfo("Imagem Selecionada", f"{self.image_path}")

    def convert(self):
        if not self.image_path:
            messagebox.showerror("Erro", "Selecione uma imagem primeiro.")
            return

        method = self.method_var.get()

        new_img, exec_time, output_name = convert_image(self.image_path, method)

        self.timer_label.config(
            text=f"Tempo de execução: {exec_time:.6f} segundos\nImagem salva como: {output_name}"
        )
        resized = new_img.resize((300, 300))
        tk_img = ImageTk.PhotoImage(resized)
        self.image_label.config(image=tk_img)
        self.image_label.image = tk_img


if __name__ == "__main__":
    root = tk.Tk()
    app = GrayScaleApp(root)
    root.mainloop()
