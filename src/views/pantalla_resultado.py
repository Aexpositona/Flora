import tkinter as tk
from src.views.components.rounded_button import RoundedButton

class PantallaResultado:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent, bg="#e8d7bd")
        self.crear_interfaz()

    def crear_interfaz(self):
        content_frame = tk.Frame(self.frame, bg="#e8d7bd")
        content_frame.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(content_frame, text="🎉 PARTIDA FINALIZADA 🎉",
                font=("Roboto", 26, "bold"), bg="#e8d7bd", fg="#2E7D32").pack(pady=20)

        tk.Label(content_frame, text="Tu resultado:",
                             font=("Roboto", 16), bg="#e8d7bd", fg="#1B5E20").pack(pady=10)

        self.resultado_label = tk.Label(content_frame, text="",
                                   font=("Roboto", 48, "bold"), bg="#e8d7bd")
        self.resultado_label.pack(pady=30)

        volver_btn = RoundedButton(content_frame, text="🏠 Volver al inicio",
                                  command=self.controller.volver_inicio,
                                  width=250, height=50, parent_bg="#e8d7bd",
                                  bg="#a8ad8d",
                                  font=("Roboto", 16, "bold"))
        volver_btn.hover_color = "#9ba090"
        volver_btn.pack(pady=20)

    def actualizar_resultado(self, aciertos, total):
        porcentaje = round((aciertos / total) * 100, 2)
        self.resultado_label.config(text=f"Has acertado {aciertos} de {total} preguntas")
        color_nota = "#4CAF50" if porcentaje >= 70 else "#FF9800" if porcentaje >= 50 else "#D32F2F"
        self.resultado_label.config(text=f"{porcentaje}%", fg=color_nota)

    def mostrar(self):
        self.frame.pack(expand=True, fill='both', padx=30, pady=30)

    def ocultar(self):
        self.frame.pack_forget()
