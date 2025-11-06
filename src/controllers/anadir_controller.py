from tkinter import messagebox
from src.models.planta import Planta
from src.utils.file_manager import copiar_imagenes_planta

class AnadirController:
    def __init__(self, repository, vista_anadir, cambiar_vista):
        self.repository = repository
        self.vista_anadir = vista_anadir
        self.cambiar_vista = cambiar_vista

    def guardar_planta(self):
        datos = self.vista_anadir.obtener_datos()

        if not datos['nombre_cientifico'] or not datos['imagenes'] or (not datos['nombre_comun_ca'] and not datos['nombre_comun_es']):
            messagebox.showwarning("Error", "Completa todos los campos obligatorios")
            return

        rutas_locales = copiar_imagenes_planta(datos['nombre_cientifico'], datos['imagenes'])

        planta = Planta(
            datos['nombre_cientifico'],
            datos['nombre_comun_ca'],
            datos['nombre_comun_es'],
            rutas_locales
        )

        self.repository.agregar(planta)
        messagebox.showinfo("Éxito", "Planta añadida correctamente")
        self.vista_anadir.limpiar_campos()
        self.cambiar_vista("inicio")

    def cancelar(self):
        self.cambiar_vista("inicio")

