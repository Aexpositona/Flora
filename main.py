#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flora Game - Juego Educativo de Plantas
=====================================

Desarrollado por: Alejandro Expósito Navarro
Con ayuda de: GitHub Copilot
Dedicado para: Yudi <3

Descripción: Aplicación educativa para aprender botánica de forma interactiva
Fecha: Noviembre 2024
Licencia: MIT - Proyecto educativo opensource

¡Aprender plantas nunca fue tan divertido!
"""

import tkinter as tk
from src.controllers.app_controller import AppController

def main():
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()

if __name__ == "__main__":
    main()

