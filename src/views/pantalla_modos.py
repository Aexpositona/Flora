import tkinter as tk
from PIL import Image, ImageTk
import os
from src.views.components.rounded_button import RoundedButton

class PantallaModos:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent, bg="#e8d7bd")
        self.crear_interfaz()

    def crear_interfaz(self):
        title_frame = tk.Frame(self.frame, bg="#e8d7bd")
        title_frame.pack(pady=(20, 10))

        title_label = tk.Label(title_frame, text="MODOS DE JUEGO",
                              font=("Roboto", 24, "bold"),
                              bg="#e8d7bd", fg="#2E7D32")
        title_label.pack()

        button_frame = tk.Frame(self.frame, bg="#e8d7bd")
        button_frame.pack(expand=True)

        jugar10_btn = RoundedButton(button_frame, text="🎮 Partida Rápida (10)",
                                   command=self.controller.iniciar_partida_rapida,
                                   width=450, height=60, parent_bg="#e8d7bd",
                                   bg="#a8ad8d")
        jugar10_btn.hover_color = "#9ba090"
        jugar10_btn.pack(pady=10)

        jugar_ultimas_btn = RoundedButton(button_frame, text="⏰ Últimas 10 plantas",
                                         command=self.controller.iniciar_partida_ultimas,
                                         width=450, height=60, parent_bg="#e8d7bd",
                                         bg="#a8ad8d")
        jugar_ultimas_btn.hover_color = "#9ba090"
        jugar_ultimas_btn.pack(pady=10)

        jugarTodas_btn = RoundedButton(button_frame, text="🎯 Todas las plantas",
                                      command=self.controller.iniciar_partida_completa,
                                      width=450, height=60, parent_bg="#e8d7bd",
                                      bg="#a8ad8d")
        jugarTodas_btn.hover_color = "#9ba090"
        jugarTodas_btn.pack(pady=10)

        jugar_rapido_nombres_btn = RoundedButton(button_frame, text="⚡ Rápido - Imágenes",
                                               command=self.controller.iniciar_partida_rapida_nombres,
                                               width=450, height=60, parent_bg="#e8d7bd",
                                               bg="#a8ad8d")
        jugar_rapido_nombres_btn.hover_color = "#9ba090"
        jugar_rapido_nombres_btn.pack(pady=10)

        jugar_ultimas_nombres_btn = RoundedButton(button_frame, text="⏰ Últimas 10 - Imágenes",
                                                 command=self.controller.iniciar_partida_ultimas_nombres,
                                                 width=450, height=60, parent_bg="#e8d7bd",
                                                 bg="#a8ad8d")
        jugar_ultimas_nombres_btn.hover_color = "#9ba090"
        jugar_ultimas_nombres_btn.pack(pady=10)

        jugar_todas_nombres_btn = RoundedButton(button_frame, text="📚 Todas - Imágenes",
                                              command=self.controller.iniciar_partida_todas_nombres,
                                              width=450, height=60, parent_bg="#e8d7bd",
                                              bg="#a8ad8d")
        jugar_todas_nombres_btn.hover_color = "#9ba090"
        jugar_todas_nombres_btn.pack(pady=10)

        tk.Frame(button_frame, height=2, bg="#2E7D32").pack(fill='x', pady=15)

        volver_btn = RoundedButton(button_frame, text="🔙 Volver",
                                  command=self.controller.volver_inicio,
                                  width=450, height=60, parent_bg="#e8d7bd",
                                  bg="#e1b984")
        volver_btn.hover_color = "#d4a870"
        volver_btn.pack(pady=10)

    def mostrar(self):
        self.frame.pack(expand=True, fill='both', padx=40, pady=40)

    def ocultar(self):
        self.frame.pack_forget()
