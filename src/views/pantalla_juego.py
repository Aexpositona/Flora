import tkinter as tk
from PIL import Image, ImageTk
import os
from src.views.components.rounded_button import RoundedButton

class PantallaJuego:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent, bg="#e8d7bd")
        self.crear_interfaz()

    def crear_interfaz(self):
        content_frame = tk.Frame(self.frame, bg="#e8d7bd")
        content_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.titulo = tk.Label(content_frame, text="",
                              font=("Roboto", 20, "bold"),
                              bg="#e8d7bd", fg="#2E7D32")
        self.titulo.pack(pady=10)

        self.contenido = tk.Label(content_frame, text="",
                                 font=("Roboto", 24),
                                 bg="#e8d7bd", fg="#1B5E20")
        self.contenido.pack(pady=20)

        self.imagen_frame = tk.Frame(content_frame, bg="#e8d7bd")
        self.imagen_frame.pack(pady=10)

        self.hint = tk.Label(content_frame, text="",
                            font=("Roboto", 12),
                            bg="#e8d7bd", fg="#666")
        self.hint.pack()

        self.entries_frame = tk.Frame(content_frame, bg="#e8d7bd")
        self.entries_frame.pack(pady=5)

        self.entry = tk.Entry(self.entries_frame, font=("Roboto", 16),
                             width=50, justify='center')
        self.entry.pack()

        self.entry_cientifico_label = tk.Label(self.entries_frame, text="Nombre científico:",
                                               font=("Roboto", 14, "italic"),
                                               bg="#e8d7bd", fg="#2E7D32")
        self.entry_cientifico = tk.Entry(self.entries_frame, font=("Roboto", 16, "italic"),
                                         width=50, justify='center')

        self.entry_comun_label = tk.Label(self.entries_frame, text="Nombre común:",
                                          font=("Roboto", 14),
                                          bg="#e8d7bd", fg="#2E7D32")
        self.entry_comun = tk.Entry(self.entries_frame, font=("Roboto", 16),
                                    width=50, justify='center')

        # Crear un frame fijo para el resultado que aparecerá después de las entradas
        self.resultado_frame = tk.Frame(content_frame, bg="#e8d7bd", height=50)
        self.resultado_frame.pack(pady=10, fill='x')
        self.resultado_frame.pack_propagate(False)

        self.resultado = tk.Label(self.resultado_frame, text="",
                                 font=("Roboto", 16), bg="#e8d7bd")
        self.resultado.pack(expand=True)

        button_frame = tk.Frame(content_frame, bg="#e8d7bd")
        button_frame.pack(pady=20)

        self.verificar_btn = RoundedButton(button_frame, text="Verificar",
                                          command=lambda: self.controller.verificar_respuesta(),
                                          width=150, height=45, parent_bg="#e8d7bd",
                                          bg="#a8ad8d",
                                          font=("Roboto", 16, "bold"))
        self.verificar_btn.hover_color = "#9ba090"
        self.verificar_btn.pack(side='left', padx=10)

        self.continuar_btn = RoundedButton(button_frame, text="Continuar",
                                          command=lambda: self.controller.siguiente_pregunta(),
                                          width=150, height=45, parent_bg="#e8d7bd",
                                          bg="#e1b984",
                                          font=("Roboto", 16, "bold"))
        self.continuar_btn.hover_color = "#d4a870"

    def limpiar_imagen(self):
        for widget in self.imagen_frame.winfo_children():
            widget.destroy()

    def mostrar_imagen(self, ruta_imagen):
        if ruta_imagen and os.path.exists(ruta_imagen):
            try:
                img = Image.open(ruta_imagen)
                # Mantener proporción original y ajustar a tamaño máximo de 600x400
                img.thumbnail((600, 400), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)

                img_label = tk.Label(self.imagen_frame, image=photo, bg="#e8d7bd", relief="solid", bd=2)
                img_label.image = photo
                img_label.pack(pady=10)
            except Exception as e:
                tk.Label(self.imagen_frame, text=f"❌ Error al cargar imagen",
                        font=("Roboto", 16), bg="#e8d7bd", fg="#D32F2F").pack(pady=20)
        else:
            tk.Label(self.imagen_frame, text="❌ Imagen no encontrada",
                    font=("Roboto", 16), bg="#e8d7bd", fg="#D32F2F").pack(pady=20)

    def mostrar_entrada_simple(self, es_cientifico=False):
        # Limpiar todos los campos antes de ocultar
        self.entry.delete(0, 'end')
        self.entry_cientifico.delete(0, 'end')
        self.entry_comun.delete(0, 'end')

        # Ocultar los campos dobles
        self.entry_cientifico_label.pack_forget()
        self.entry_cientifico.pack_forget()
        self.entry_comun_label.pack_forget()
        self.entry_comun.pack_forget()

        if es_cientifico:
            self.entry.config(font=("Roboto", 16, "italic"))
        else:
            self.entry.config(font=("Roboto", 16))

        self.entry.pack()

    def mostrar_entradas_dobles(self):
        # Limpiar todos los campos antes de mostrar
        self.entry.delete(0, 'end')
        self.entry_cientifico.delete(0, 'end')
        self.entry_comun.delete(0, 'end')

        # Ocultar el campo simple
        self.entry.pack_forget()

        self.entry_cientifico_label.pack(pady=(5, 2))
        self.entry_cientifico.pack(pady=(0, 10))
        self.entry_comun_label.pack(pady=(5, 2))
        self.entry_comun.pack(pady=(0, 10))

    def limpiar_entradas(self):
        self.entry.delete(0, 'end')
        self.entry_cientifico.delete(0, 'end')
        self.entry_comun.delete(0, 'end')

    def mostrar(self):
        self.frame.pack(expand=True, fill='both', padx=20, pady=20)

    def ocultar(self):
        self.frame.pack_forget()
