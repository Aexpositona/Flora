import random
from tkinter import messagebox
import tkinter as tk

class JuegoController:
    def __init__(self, repository, vista_juego, vista_resultado, cambiar_vista):
        self.repository = repository
        self.vista_juego = vista_juego
        self.vista_resultado = vista_resultado
        self.cambiar_vista = cambiar_vista

        self.seleccion = []
        self.tipos_preguntas = []
        self.pregunta_actual = 0
        self.aciertos = 0
        self.total_preguntas = 0
        self.respuesta_correcta = ""

    def iniciar_juego(self, cantidad):
        plantas = self.repository.obtener_todas()
        if not plantas:
            messagebox.showinfo("Info", "No hay plantas añadidas")
            return

        self.seleccion = plantas.copy()
        random.shuffle(self.seleccion)
        self.seleccion = self.seleccion[:min(cantidad, len(self.seleccion))]

        self._configurar_juego()

    def iniciar_juego_con_plantas(self, plantas_especificas):
        if not plantas_especificas:
            messagebox.showinfo("Info", "No hay plantas disponibles")
            return

        self.seleccion = plantas_especificas.copy()
        random.shuffle(self.seleccion)

        self._configurar_juego()

    def iniciar_juego_solo_nombres(self, cantidad):
        plantas = self.repository.obtener_todas()
        if not plantas:
            messagebox.showinfo("Info", "No hay plantas añadidas")
            return

        self.seleccion = plantas.copy()
        random.shuffle(self.seleccion)
        self.seleccion = self.seleccion[:min(cantidad, len(self.seleccion))]

        self._configurar_juego_solo_nombres()

    def iniciar_juego_solo_nombres_con_plantas(self, plantas_especificas):
        if not plantas_especificas:
            messagebox.showinfo("Info", "No hay plantas disponibles")
            return

        self.seleccion = plantas_especificas.copy()
        random.shuffle(self.seleccion)

        self._configurar_juego_solo_nombres()

    def _configurar_juego(self):
        self.aciertos = 0
        self.total_preguntas = len(self.seleccion)
        self.pregunta_actual = 0

        tipos_preguntas = []
        num_cada_tipo = self.total_preguntas // 3
        tipos_preguntas.extend([0] * num_cada_tipo)
        tipos_preguntas.extend([1] * num_cada_tipo)
        tipos_preguntas.extend([2] * (self.total_preguntas - 2 * num_cada_tipo))
        random.shuffle(tipos_preguntas)
        self.tipos_preguntas = tipos_preguntas

        self.cambiar_vista("juego")
        self.mostrar_pregunta_actual()

    def _configurar_juego_solo_nombres(self):
        self.aciertos = 0
        self.total_preguntas = len(self.seleccion)
        self.pregunta_actual = 0

        # Solo tipo 2: imagen + ambos nombres
        self.tipos_preguntas = [2] * self.total_preguntas

        self.cambiar_vista("juego")
        self.mostrar_pregunta_actual()

    def mostrar_pregunta_actual(self):
        vista = self.vista_juego
        vista.limpiar_imagen()
        vista.limpiar_entradas()

        vista.entry.config(state='normal')
        vista.entry_cientifico.config(state='normal')
        vista.entry_comun.config(state='normal')
        vista.resultado.config(text="")

        # Limpiar y ocultar hint para evitar interferencias
        vista.hint.config(text="")
        vista.hint.pack_forget()

        # Ocultar contenido por defecto para evitar interferencias
        vista.contenido.pack_forget()

        # Mostrar solo botón verificar, ocultar continuar
        vista.verificar_btn.pack(side='left', padx=10)
        vista.continuar_btn.pack_forget()

        p = self.seleccion[self.pregunta_actual]
        tipo = self.tipos_preguntas[self.pregunta_actual]

        if tipo == 0:
            vista.titulo.config(text="¿Cuál es el NOMBRE COMÚN?")
            # Mostrar el nombre científico en el área de imagen
            texto_label = tk.Label(vista.imagen_frame, text=p.nombre_cientifico,
                                  font=("Roboto", 24, "italic"),
                                  bg="#e8d7bd", fg="#1B5E20")
            texto_label.pack(pady=20)
            vista.mostrar_entrada_simple(es_cientifico=False)
            vista.entry.focus()
            self.respuesta_correcta = p.get_nombre_comun()

        elif tipo == 1:
            vista.titulo.config(text="¿Cuál es el NOMBRE CIENTÍFICO?")
            # Mostrar el nombre común en el área de imagen
            texto_label = tk.Label(vista.imagen_frame, text=p.get_nombre_comun(),
                                  font=("Roboto", 24),
                                  bg="#e8d7bd", fg="#1B5E20")
            texto_label.pack(pady=20)
            vista.mostrar_entrada_simple(es_cientifico=True)
            vista.entry.focus()
            self.respuesta_correcta = p.nombre_cientifico

        else:
            vista.titulo.config(text="¿Cuáles son el NOMBRE CIENTÍFICO y COMÚN de esta planta?")

            imagen_aleatoria = p.get_imagen_aleatoria()
            vista.mostrar_imagen(imagen_aleatoria)

            vista.mostrar_entradas_dobles()
            vista.entry_cientifico.focus()

            self.respuesta_correcta = f"{p.nombre_cientifico}|{p.get_nombre_comun()}"

        vista.entry.bind('<Return>', lambda e: self.verificar_respuesta())
        vista.entry_cientifico.bind('<Return>', lambda e: self.verificar_respuesta())
        vista.entry_comun.bind('<Return>', lambda e: self.verificar_respuesta())

    def verificar_respuesta(self):
        vista = self.vista_juego
        tipo = self.tipos_preguntas[self.pregunta_actual]

        if tipo < 2:
            entrada = vista.entry.get().strip()
        else:
            entrada_cientifico = vista.entry_cientifico.get().strip()
            entrada_comun = vista.entry_comun.get().strip()
            entrada = f"{entrada_cientifico}|{entrada_comun}"

        if not entrada or (tipo == 2 and (not entrada_cientifico or not entrada_comun)):
            return

        p = self.seleccion[self.pregunta_actual]

        # Aceptar respuestas en ambos idiomas (catalán y castellano)
        if tipo == 0:  # Pregunta nombre común
            entrada_lower = entrada.lower()
            nombre_ca_lower = (p.nombre_comun_ca or "").lower()
            nombre_es_lower = (p.nombre_comun_es or "").lower()
            correcto = entrada_lower == nombre_ca_lower or entrada_lower == nombre_es_lower
        elif tipo == 1:  # Pregunta nombre científico
            correcto = entrada.lower() == p.nombre_cientifico.lower()
        else:  # Pregunta ambos nombres
            entrada_cientifico_lower = entrada_cientifico.lower()
            entrada_comun_lower = entrada_comun.lower()
            cientifico_lower = p.nombre_cientifico.lower()
            nombre_ca_lower = (p.nombre_comun_ca or "").lower()
            nombre_es_lower = (p.nombre_comun_es or "").lower()

            cientifico_correcto = entrada_cientifico_lower == cientifico_lower
            comun_correcto = entrada_comun_lower == nombre_ca_lower or entrada_comun_lower == nombre_es_lower
            correcto = cientifico_correcto and comun_correcto

        if correcto:
            self.aciertos += 1
            vista.resultado.config(text="✅ ¡CORRECTO!", fg="#4CAF50")
        else:
            vista.resultado.config(text="❌ Incorrecto", fg="#D32F2F", font=("Roboto", 16))

            # Mostrar la respuesta correcta en el área de imagen
            if tipo == 2:
                hint_text = f"Nombre científico: {p.nombre_cientifico}\nNombre común: {p.get_nombre_comun()}"
            elif tipo == 1:
                hint_text = f"Nombre científico: {p.nombre_cientifico}"
            else:
                hint_text = f"Nombre común: {p.get_nombre_comun()}"

            # Crear label del hint en el área de imagen
            hint_label = tk.Label(vista.imagen_frame, text=hint_text,
                                font=("Roboto", 14, "italic"),
                                bg="#e8d7bd", fg="#D32F2F",
                                justify="center")
            hint_label.pack(pady=10)

        # Deshabilitar entradas y ocultar botón verificar, mostrar continuar
        vista.entry.config(state='disabled')
        vista.entry_cientifico.config(state='disabled')
        vista.entry_comun.config(state='disabled')

        vista.verificar_btn.pack_forget()

        if self.pregunta_actual + 1 < self.total_preguntas:
            vista.continuar_btn.pack(side='left', padx=10)
        else:
            vista.parent.after(2000, self.mostrar_resultado_final)

    def siguiente_pregunta(self):
        self.pregunta_actual += 1
        self.mostrar_pregunta_actual()

    def mostrar_resultado_final(self):
        self.vista_resultado.actualizar_resultado(self.aciertos, self.total_preguntas)
        self.cambiar_vista("resultado")
