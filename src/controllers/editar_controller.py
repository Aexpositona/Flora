from tkinter import messagebox
from src.models.planta import Planta
from src.utils.file_manager import copiar_imagenes_planta, eliminar_carpeta_planta, IMAGENES_DIR

class EditarController:
    def __init__(self, repository, vista_editar, cambiar_vista):
        self.repository = repository
        self.vista_editar = vista_editar
        self.cambiar_vista = cambiar_vista
        self.planta_editando_idx = None

    def mostrar_editar(self):
        plantas = self.repository.obtener_todas()
        if not plantas:
            messagebox.showinfo("Info", "No hay plantas añadidas")
            return False

        self.vista_editar.cargar_lista_plantas(plantas)
        self.vista_editar.mostrar_lista()
        return True

    def abrir_formulario_editar(self):
        idx = self.vista_editar.obtener_seleccion()
        if idx is None:
            messagebox.showwarning("Advertencia", "Selecciona una planta para editar")
            return

        self.planta_editando_idx = idx
        planta = self.repository.obtener_todas()[idx]
        self.vista_editar.cargar_datos_planta(planta)
        self.vista_editar.mostrar_formulario()

    def guardar_edicion(self):
        datos = self.vista_editar.obtener_datos()

        if not datos['nombre_cientifico'] or not datos['imagenes'] or (not datos['nombre_comun_ca'] and not datos['nombre_comun_es']):
            messagebox.showwarning("Error", "Completa todos los campos obligatorios")
            return

        rutas_actuales = datos['imagenes']
        rutas_nuevas = [r for r in rutas_actuales if not r.startswith(IMAGENES_DIR)]

        if rutas_nuevas:
            rutas_existentes = [r for r in rutas_actuales if r.startswith(IMAGENES_DIR)]
            rutas_copiadas = copiar_imagenes_planta(datos['nombre_cientifico'], rutas_nuevas)
            todas_rutas = rutas_existentes + rutas_copiadas
        else:
            todas_rutas = rutas_actuales

        planta = Planta(
            datos['nombre_cientifico'],
            datos['nombre_comun_ca'],
            datos['nombre_comun_es'],
            todas_rutas
        )

        self.repository.actualizar(self.planta_editando_idx, planta)
        messagebox.showinfo("Éxito", "Planta editada correctamente")
        self.cambiar_vista("inicio")

    def eliminar_planta(self):
        idx = self.vista_editar.obtener_seleccion()
        if idx is None:
            messagebox.showwarning("Advertencia", "Selecciona una planta para eliminar")
            return

        respuesta = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar esta planta y sus imágenes?")
        if respuesta:
            planta = self.repository.obtener_todas()[idx]
            eliminar_carpeta_planta(planta.nombre_cientifico)
            self.repository.eliminar(idx)
            messagebox.showinfo("Éxito", "Planta eliminada correctamente")
            self.cambiar_vista("inicio")

    def cancelar_edicion(self):
        self.vista_editar.mostrar_lista()

    def volver_inicio(self):
        self.cambiar_vista("inicio")

