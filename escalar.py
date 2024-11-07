import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class EscaladorImagenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Escalador de Imagen")
        self.imagen = None
        self.imagen_escalada = None

        # Crear la interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        self.boton_cargar = tk.Button(self.root, text="Cargar Imagen", command=self.cargar_imagen)
        self.boton_cargar.pack()

        self.lienzo = tk.Canvas(self.root, width=500, height=500)
        self.lienzo.pack()

        self.slider_escala = tk.Scale(self.root, from_=0.1, to=3.0, resolution=0.1, orient="horizontal", label="Factor de Escala", command=self.escalar_imagen)
        self.slider_escala.set(1.0)
        self.slider_escala.pack()

        self.boton_guardar = tk.Button(self.root, text="Guardar Imagen", command=self.guardar_imagen)
        self.boton_guardar.pack()

    def cargar_imagen(self):
        ruta_archivo = filedialog.askopenfilename()
        if ruta_archivo:
            self.imagen = Image.open(ruta_archivo)
            self.imagen_escalada = self.imagen
            self.mostrar_imagen(self.imagen)

    def mostrar_imagen(self, img):
        img_mostrar = img.resize((500, 500), Image.LANCZOS)
        self.imagen_tk = ImageTk.PhotoImage(img_mostrar)
        self.lienzo.create_image(0, 0, anchor="nw", image=self.imagen_tk)

    def escalar_imagen(self, factor_escala):
        if self.imagen:
            factor_escala = float(factor_escala)
            nuevo_ancho = int(self.imagen.width * factor_escala)
            nueva_altura = int(self.imagen.height * factor_escala)
            self.imagen_escalada = Image.new("RGB", (nuevo_ancho, nueva_altura))

            pixeles_originales = self.imagen.load()
            pixeles_escalados = self.imagen_escalada.load()

            for y in range(nueva_altura):
                for x in range(nuevo_ancho):
                    origen_x = int(x / factor_escala)
                    origen_y = int(y / factor_escala)
                    pixeles_escalados[x, y] = pixeles_originales[origen_x, origen_y]

            self.mostrar_imagen(self.imagen_escalada)

    def guardar_imagen(self):
        if self.imagen_escalada:
            ruta_guardado = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
            if ruta_guardado:
                self.imagen_escalada.save(ruta_guardado)
                print("Imagen guardada en:", ruta_guardado)

ventana = tk.Tk()
app = EscaladorImagenApp(ventana)
ventana.mainloop()
