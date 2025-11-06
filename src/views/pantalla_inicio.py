"""
Pantalla de Inicio - Flora Game
=============================

Autor: Alejandro Expósito Navarro
Asistencia: GitHub Copilot
Con amor para: Yudi <3

La primera pantalla que ven los usuarios - diseñada para inspirar el aprendizaje
"""

import tkinter as tk
from PIL import Image, ImageTk
import os
from src.views.components.rounded_button import RoundedButton

class PantallaInicio:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent, bg="#e8d7bd")
        self.crear_interfaz()

    def crear_interfaz(self):
        logo_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "img.png")

        logo_frame = tk.Frame(self.frame, bg="#e8d7bd")
        logo_frame.pack(pady=(20, 10))

        if os.path.exists(logo_path):
            try:
                img = Image.open(logo_path)
                img = img.resize((80, 80), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)

                logo_label = tk.Label(logo_frame, image=photo, bg="#e8d7bd")
                logo_label.image = photo
                logo_label.pack()
            except:
                pass

        title_label = tk.Label(self.frame, text="LUDUS HERBARUM",
                              font=("Roboto", 26, "bold"),
                              bg="#e8d7bd", fg="#2E7D32")
        title_label.pack(pady=(0, 30))

        button_frame = tk.Frame(self.frame, bg="#e8d7bd")
        button_frame.pack(expand=True)

        jugar_btn = RoundedButton(button_frame, text="🎮 Jugar",
                                 command=self.controller.mostrar_modos,
                                 width=300, height=60, parent_bg="#e8d7bd",
                                 bg="#a8ad8d")
        jugar_btn.hover_color = "#9ba090"
        jugar_btn.pack(pady=15)

        # Separador visual
        tk.Frame(button_frame, height=2, bg="#2E7D32").pack(fill='x', pady=15)

        anadir_btn = RoundedButton(button_frame, text="➕ Añadir planta",
                                  command=self.controller.mostrar_anadir,
                                  width=300, height=60, parent_bg="#e8d7bd",
                                  bg="#e1b984")
        anadir_btn.hover_color = "#d4a870"
        anadir_btn.pack(pady=10)

        editar_btn = RoundedButton(button_frame, text="✏️ Editar planta",
                                  command=self.controller.mostrar_editar,
                                  width=300, height=60, parent_bg="#e8d7bd",
                                  bg="#e1b984")
        editar_btn.hover_color = "#d4a870"
        editar_btn.pack(pady=10)

        salir_btn = RoundedButton(button_frame, text="❌ Salir",
                                 command=self.controller.salir,
                                 width=300, height=60, parent_bg="#e8d7bd",
                                 bg="#de8f88")
        salir_btn.hover_color = "#c97f79"
        salir_btn.pack(pady=15)

    def mostrar(self):
        self.frame.pack(expand=True, fill='both', padx=40, pady=40)

    def ocultar(self):
        self.frame.pack_forget()
