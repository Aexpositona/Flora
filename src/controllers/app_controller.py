"""
Flora Game - Controlador Principal
=================================

Autor: Alejandro Expósito Navarro
Asistencia: GitHub Copilot
Dedicado: Para Yudi <3

Gestiona la navegación entre pantallas y coordinación de controladores
"""

import tkinter as tk
from src.models.planta_repository import PlantaRepository
from src.views.pantalla_inicio import PantallaInicio
from src.views.pantalla_modos import PantallaModos
from src.views.pantalla_juego import PantallaJuego
from src.views.pantalla_resultado import PantallaResultado
from src.views.pantalla_anadir import PantallaAnadir
from src.views.pantalla_editar import PantallaEditar
from src.controllers.juego_controller import JuegoController
from src.controllers.anadir_controller import AnadirController
from src.controllers.editar_controller import EditarController
from src.utils.file_manager import crear_directorio_imagenes
import os

class AppController:
    def __init__(self, root):
        self.root = root
        self.root.title("Flora - Juego de Plantas")
        self.root.geometry("800x600")
        self.root.configure(bg="#e8d7bd")
        self.root.state('zoomed')

        logo_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "img.png")
        if os.path.exists(logo_path):
            try:
                self.root.iconphoto(True, tk.PhotoImage(file=logo_path))
            except:
                pass

        crear_directorio_imagenes()

        self.repository = PlantaRepository()

        main_container = tk.Frame(root, bg="#e8d7bd")
        main_container.pack(expand=True, fill='both')

        self.vista_inicio = PantallaInicio(main_container, self)
        self.vista_modos = PantallaModos(main_container, self)
        self.vista_resultado = PantallaResultado(main_container, self)

        self.vista_juego = PantallaJuego(main_container, self)
        self.vista_anadir = PantallaAnadir(main_container, self)
        self.vista_editar = PantallaEditar(main_container, self)

        self.juego_controller = JuegoController(
            self.repository,
            self.vista_juego,
            self.vista_resultado,
            self.cambiar_vista
        )

        self.vista_juego.controller = self.juego_controller

        self.anadir_controller = AnadirController(
            self.repository,
            self.vista_anadir,
            self.cambiar_vista
        )

        self.vista_anadir.controller = self.anadir_controller

        self.editar_controller = EditarController(
            self.repository,
            self.vista_editar,
            self.cambiar_vista
        )

        self.vista_editar.controller = self.editar_controller

        self.vistas = {
            "inicio": self.vista_inicio,
            "modos": self.vista_modos,
            "juego": self.vista_juego,
            "resultado": self.vista_resultado,
            "anadir": self.vista_anadir,
            "editar": self.vista_editar
        }

        self.cambiar_vista("inicio")

    def cambiar_vista(self, nombre):
        for vista in self.vistas.values():
            vista.ocultar()

        if nombre in self.vistas:
            self.vistas[nombre].mostrar()

    def iniciar_partida_rapida(self):
        self.juego_controller.iniciar_juego(10)

    def iniciar_partida_ultimas(self):
        # Obtener las últimas 10 plantas añadidas
        plantas = self.repository.obtener_todas()
        ultimas_10 = plantas[-10:] if len(plantas) >= 10 else plantas
        self.juego_controller.iniciar_juego_con_plantas(ultimas_10)

    def iniciar_partida_completa(self):
        cantidad = self.repository.cantidad()
        self.juego_controller.iniciar_juego(cantidad)

    def iniciar_partida_rapida_nombres(self):
        self.juego_controller.iniciar_juego_solo_nombres(10)

    def iniciar_partida_todas_nombres(self):
        cantidad = self.repository.cantidad()
        self.juego_controller.iniciar_juego_solo_nombres(cantidad)

    def iniciar_partida_ultimas_nombres(self):
        # Obtener las últimas 10 plantas añadidas para modo solo nombres
        plantas = self.repository.obtener_todas()
        ultimas_10 = plantas[-10:] if len(plantas) >= 10 else plantas
        self.juego_controller.iniciar_juego_solo_nombres_con_plantas(ultimas_10)

    def mostrar_anadir(self):
        self.vista_anadir.limpiar_campos()
        self.cambiar_vista("anadir")

    def mostrar_editar(self):
        if self.editar_controller.mostrar_editar():
            self.cambiar_vista("editar")

    def volver_inicio(self):
        self.cambiar_vista("inicio")

    def salir(self):
        self.root.quit()

    def mostrar_modos(self):
        self.cambiar_vista("modos")
