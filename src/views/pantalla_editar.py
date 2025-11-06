import tkinter as tk
from tkinter import filedialog, messagebox
from src.views.components.rounded_button import RoundedButton

class PantallaEditar:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.frame = tk.Frame(parent, bg="#e8d7bd")
        self.imagenes_path = tk.StringVar()
        self.plantas_list = []
        self.selected_index = None
        self.crear_interfaz()

    def crear_interfaz(self):
        container_centrado = tk.Frame(self.frame, bg="#e8d7bd")
        container_centrado.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.6, relheight=0.9)

        tk.Label(container_centrado, text="✏️ EDITAR PLANTA",
                font=("Roboto", 20, "bold"), bg="#e8d7bd", fg="#2E7D32").pack(pady=(0, 20))

        self.listbox_frame = tk.Frame(container_centrado, bg="#e8d7bd")

        # Frame para controles de ordenamiento
        controls_frame = tk.Frame(self.listbox_frame, bg="#e8d7bd")
        controls_frame.pack(fill='x', pady=(0, 10))

        tk.Label(controls_frame, text="Ordenar por:",
                font=("Roboto", 12), bg="#e8d7bd", fg="#2E7D32").pack(side='left', padx=(0, 10))

        self.orden_var = tk.StringVar(value="cientifico")
        orden_cientifico = tk.Radiobutton(controls_frame, text="Nombre científico",
                                         variable=self.orden_var, value="cientifico",
                                         bg="#e8d7bd", fg="#2E7D32",
                                         command=self.ordenar_lista)
        orden_cientifico.pack(side='left', padx=5)

        orden_comun = tk.Radiobutton(controls_frame, text="Nombre común",
                                    variable=self.orden_var, value="comun",
                                    bg="#e8d7bd", fg="#2E7D32",
                                    command=self.ordenar_lista)
        orden_comun.pack(side='left', padx=5)

        orden_fecha = tk.Radiobutton(controls_frame, text="Más recientes",
                                    variable=self.orden_var, value="reciente",
                                    bg="#e8d7bd", fg="#2E7D32",
                                    command=self.ordenar_lista)
        orden_fecha.pack(side='left', padx=5)

        header_frame = tk.Frame(self.listbox_frame, bg="#2E7D32", height=40)
        header_frame.pack(fill='x', pady=(0, 2))
        header_frame.pack_propagate(False)

        left_header = tk.Frame(header_frame, bg="#2E7D32")
        left_header.pack(side='left', fill='both', expand=True)

        right_header = tk.Frame(header_frame, bg="#2E7D32")
        right_header.pack(side='left', fill='both', expand=True)

        tk.Label(left_header, text="Nombre Científico",
                font=("Roboto", 14, "bold"), bg="#2E7D32", fg="#FFFFFF").pack(expand=True)
        tk.Label(right_header, text="Nombre Común",
                font=("Roboto", 14, "bold"), bg="#2E7D32", fg="#FFFFFF").pack(expand=True)

        list_container = tk.Frame(self.listbox_frame, bg="#FFFFFF", relief="solid", bd=1)
        list_container.pack(fill='both', expand=True)

        canvas = tk.Canvas(list_container, bg="#FFFFFF", highlightthickness=0, height=300)
        scrollbar = tk.Scrollbar(list_container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg="#FFFFFF")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        def _on_canvas_configure(event):
            canvas.itemconfig(canvas.find_withtag("all")[0], width=event.width)

        canvas.bind('<Configure>', _on_canvas_configure)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.canvas = canvas
        self.list_items = []

        buttons_container = tk.Frame(self.listbox_frame, bg="#e8d7bd")
        buttons_container.pack(pady=20)

        editar_btn = RoundedButton(buttons_container, text="✏️ Editar seleccionada",
                                  command=lambda: self.controller.abrir_formulario_editar(),
                                  width=327, height=60, parent_bg="#e8d7bd",
                                  bg="#a8ad8d",
                                  font=("Roboto", 16, "bold"))
        editar_btn.hover_color = "#9ba090"
        editar_btn.pack(pady=5)

        eliminar_btn = RoundedButton(buttons_container, text="🗑️ Eliminar seleccionada",
                                    command=lambda: self.controller.eliminar_planta(),
                                    width=327, height=60, parent_bg="#e8d7bd",
                                    bg="#de8f88",
                                    font=("Roboto", 16, "bold"))
        eliminar_btn.hover_color = "#c97f79"
        eliminar_btn.pack(pady=5)

        volver_btn = RoundedButton(buttons_container, text="🏠 Volver",
                                  command=lambda: self.controller.volver_inicio(),
                                  width=327, height=60, parent_bg="#e8d7bd",
                                  bg="#e1b984",
                                  font=("Roboto", 16, "bold"))
        volver_btn.hover_color = "#d4a870"
        volver_btn.pack(pady=5)

        self.form_frame = tk.Frame(container_centrado, bg="#e8d7bd")
        fields_container = tk.Frame(self.form_frame, bg="#e8d7bd")
        fields_container.pack()

        tk.Label(fields_container, text="Nombre científico:",
                font=("Roboto", 16, "italic"), bg="#e8d7bd", fg="#2E7D32").pack(anchor='w', pady=(10, 2))
        self.nombre_cientifico = tk.Entry(fields_container, font=("Roboto", 16, "italic"), width=35)
        self.nombre_cientifico.pack(pady=(0, 10))

        tk.Label(fields_container, text="Nombre común catalán:",
                font=("Roboto", 16), bg="#e8d7bd", fg="#2E7D32").pack(anchor='w', pady=(0, 2))
        self.nombre_comun_ca = tk.Entry(fields_container, font=("Roboto", 16), width=35)
        self.nombre_comun_ca.pack(pady=(0, 10))

        tk.Label(fields_container, text="Nombre común castellano:",
                font=("Roboto", 16), bg="#e8d7bd", fg="#2E7D32").pack(anchor='w', pady=(0, 2))
        self.nombre_comun_es = tk.Entry(fields_container, font=("Roboto", 16), width=35)
        self.nombre_comun_es.pack(pady=(0, 10))

        self.imagenes_label = tk.Label(fields_container, text="",
                                       font=("Roboto", 12), bg="#e8d7bd", fg="#4CAF50")

        cambiar_img_btn = RoundedButton(fields_container, text="📷 Cambiar imágenes",
                                       command=self.seleccionar_imagenes,
                                       width=275, height=50, parent_bg="#e8d7bd",
                                       bg="#e1b984",
                                       font=("Roboto", 14, "bold"))
        cambiar_img_btn.hover_color = "#d4a870"
        cambiar_img_btn.pack(pady=10)
        self.imagenes_label.pack()

        button_frame = tk.Frame(fields_container, bg="#e8d7bd")
        button_frame.pack(pady=20)

        guardar_btn = RoundedButton(button_frame, text="💾 Guardar",
                                   command=lambda: self.controller.guardar_edicion(),
                                   width=150, height=45, parent_bg="#e8d7bd",
                                   bg="#a8ad8d",
                                   font=("Roboto", 14, "bold"))
        guardar_btn.hover_color = "#9ba090"
        guardar_btn.pack(side='left', padx=10)

        cancelar_btn = RoundedButton(button_frame, text="❌ Cancelar",
                                    command=lambda: self.controller.cancelar_edicion(),
                                    width=165, height=50, parent_bg="#e8d7bd",
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

    def cargar_lista_plantas(self, plantas):
        self.plantas_list = plantas
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.list_items = []

        for idx, p in enumerate(plantas):
            item_frame = tk.Frame(self.scrollable_frame, bg="#FFFFFF", highlightthickness=1,
                                 highlightbackground="#CCCCCC", highlightcolor="#CCCCCC")
            item_frame.pack(fill='x', pady=3, padx=5, ipady=5)

            row_frame = tk.Frame(item_frame, bg="#FFFFFF")
            row_frame.pack(fill='x', expand=True)

            left_container = tk.Frame(row_frame, bg="#FFFFFF")
            left_container.pack(side='left', fill='both', expand=True, padx=10, pady=8)

            right_container = tk.Frame(row_frame, bg="#FFFFFF")
            right_container.pack(side='left', fill='both', expand=True, padx=10, pady=8)

            cientifico_label = tk.Label(left_container, text=p.nombre_cientifico,
                                        font=("Roboto", 14, "italic"), bg="#FFFFFF", fg="#1B5E20")
            cientifico_label.pack()

            comun_label = tk.Label(right_container, text=p.get_nombre_comun(),
                                   font=("Roboto", 14), bg="#FFFFFF", fg="#333333")
            comun_label.pack()

            for widget in [item_frame, row_frame, left_container, right_container, cientifico_label, comun_label]:
                widget.bind("<Button-1>", lambda e, i=idx: self._select_item(i))

            self.list_items.append(item_frame)

        self.canvas.update_idletasks()
        self.canvas.config(width=self.canvas.winfo_width())

    def _select_item(self, index):
        for item in self.list_items:
            item.config(bg="#FFFFFF", highlightbackground="#DDDDDD")
            for child in item.winfo_children():
                child.config(bg="#FFFFFF")
                for subchild in child.winfo_children():
                    subchild.config(bg="#FFFFFF")
                    for subsubchild in subchild.winfo_children():
                        subsubchild.config(bg="#FFFFFF")

        if index < len(self.list_items):
            item = self.list_items[index]
            item.config(bg="#C8E6C9", highlightbackground="#4CAF50")
            for child in item.winfo_children():
                child.config(bg="#C8E6C9")
                for subchild in child.winfo_children():
                    subchild.config(bg="#C8E6C9")
                    for subsubchild in subchild.winfo_children():
                        subsubchild.config(bg="#C8E6C9")

            self.selected_index = index

    def obtener_seleccion(self):
        return self.selected_index

    def cargar_datos_planta(self, planta):
        self.nombre_cientifico.delete(0, tk.END)
        self.nombre_cientifico.insert(0, planta.nombre_cientifico)

        self.nombre_comun_ca.delete(0, tk.END)
        self.nombre_comun_ca.insert(0, planta.nombre_comun_ca or "")

        self.nombre_comun_es.delete(0, tk.END)
        self.nombre_comun_es.insert(0, planta.nombre_comun_es or "")

        self.imagenes_path.set(";".join(planta.imagenes))
        self.imagenes_label.config(text=f"📷 {len(planta.imagenes)} imágenes", fg="#4CAF50")

    def obtener_datos(self):
        return {
            'nombre_cientifico': self.nombre_cientifico.get(),
            'nombre_comun_ca': self.nombre_comun_ca.get(),
            'nombre_comun_es': self.nombre_comun_es.get(),
            'imagenes': self.imagenes_path.get().split(";") if self.imagenes_path.get() else []
        }

    def mostrar_lista(self):
        self.listbox_frame.pack(expand=True, fill='both', pady=10)
        self.form_frame.pack_forget()

    def mostrar_formulario(self):
        self.listbox_frame.pack_forget()
        self.form_frame.pack(expand=True, fill='both')

    def mostrar(self):
        self.frame.pack(expand=True, fill='both', padx=20, pady=20)

    def ocultar(self):
        self.frame.pack_forget()

    def ordenar_lista(self):
        criterio = self.orden_var.get()
        if criterio == "cientifico":
            plantas_ordenadas = sorted(self.plantas_list, key=lambda p: p.nombre_cientifico)
        elif criterio == "comun":
            plantas_ordenadas = sorted(self.plantas_list, key=lambda p: p.get_nombre_comun())
        else:
            plantas_ordenadas = self.plantas_list  # Orden por defecto

        self.cargar_lista_plantas(plantas_ordenadas)

