import tkinter as tk
from tkinter import filedialog, messagebox
from src.views.components.rounded_button import RoundedButton

class PantallaAnadir:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent, bg="#e8d7bd")
        self.imagenes_path = tk.StringVar()
        self.crear_interfaz()

    def crear_interfaz(self):
        content_frame = tk.Frame(self.frame, bg="#e8d7bd")
        content_frame.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(content_frame, text="➕ AÑADIR NUEVA PLANTA",
                font=("Roboto", 20, "bold"), bg="#e8d7bd", fg="#2E7D32").pack(pady=(0, 20))

        fields_frame = tk.Frame(content_frame, bg="#e8d7bd")
        fields_frame.pack()

        tk.Label(fields_frame, text="Nombre científico:",
                font=("Roboto", 16, "italic"), bg="#e8d7bd", fg="#2E7D32").pack(anchor='w', pady=(10, 2))
        self.nombre_cientifico = tk.Entry(fields_frame, font=("Roboto", 16, "italic"), width=35)
        self.nombre_cientifico.pack(pady=(0, 10))

        tk.Label(fields_frame, text="Nombre común catalán:",
                font=("Roboto", 16), bg="#e8d7bd", fg="#2E7D32").pack(anchor='w', pady=(0, 2))
        self.nombre_comun_ca = tk.Entry(fields_frame, font=("Roboto", 16), width=35)
        self.nombre_comun_ca.pack(pady=(0, 10))

        tk.Label(fields_frame, text="Nombre común castellano:",
                font=("Roboto", 16), bg="#e8d7bd", fg="#2E7D32").pack(anchor='w', pady=(0, 2))
        self.nombre_comun_es = tk.Entry(fields_frame, font=("Roboto", 16), width=35)
        self.nombre_comun_es.pack(pady=(0, 10))

        self.imagenes_label = tk.Label(fields_frame, text="No se han seleccionado imágenes",
                                       font=("Roboto", 12), bg="#e8d7bd", fg="#666")

        sel_img_btn = RoundedButton(fields_frame, text="📷 Seleccionar imágenes",
                                   command=self.seleccionar_imagenes,
                                   width=275, height=50, parent_bg="#e8d7bd",
                                   bg="#e1b984",
                                   font=("Roboto", 14, "bold"))
        sel_img_btn.hover_color = "#d4a870"
        sel_img_btn.pack(pady=10)
        self.imagenes_label.pack()

        button_frame = tk.Frame(fields_frame, bg="#e8d7bd")
        button_frame.pack(pady=20)

        guardar_btn = RoundedButton(button_frame, text="💾 Guardar",
                                   command=lambda: self.controller.guardar_planta(),
                                   width=150, height=45, parent_bg="#e8d7bd",
                                   bg="#a8ad8d",
                                   font=("Roboto", 14, "bold"))
        guardar_btn.hover_color = "#9ba090"
        guardar_btn.pack(side='left', padx=10)

        cancelar_btn = RoundedButton(button_frame, text="❌ Cancelar",
                                    command=lambda: self.controller.cancelar(),
                                    width=150, height=45, parent_bg="#e8d7bd",
                                    bg="#de8f88",
                                    font=("Roboto", 14, "bold"))
        cancelar_btn.hover_color = "#c97f79"
        cancelar_btn.pack(side='left', padx=10)

    def seleccionar_imagenes(self):
        paths = filedialog.askopenfilenames(
            filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        if paths:
            self.imagenes_path.set(";".join(paths))
            self.imagenes_label.config(text=f"📷 {len(paths)} imágenes seleccionadas", fg="#4CAF50")

    def limpiar_campos(self):
        self.nombre_cientifico.delete(0, tk.END)
        self.nombre_comun_ca.delete(0, tk.END)
        self.nombre_comun_es.delete(0, tk.END)
        self.imagenes_path.set("")
        self.imagenes_label.config(text="No se han seleccionado imágenes", fg="#666")

    def obtener_datos(self):
        return {
            'nombre_cientifico': self.nombre_cientifico.get(),
            'nombre_comun_ca': self.nombre_comun_ca.get(),
            'nombre_comun_es': self.nombre_comun_es.get(),
            'imagenes': self.imagenes_path.get().split(";") if self.imagenes_path.get() else []
        }

    def mostrar(self):
        self.frame.pack(expand=True, fill='both', padx=30, pady=30)

    def ocultar(self):
        self.frame.pack_forget()
