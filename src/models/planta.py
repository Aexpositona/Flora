"""
Modelo Planta - Flora Game
========================

Creado por: Alejandro Expósito Navarro
Con ayuda de: GitHub Copilot
Para: Yudi <3

Representa una planta con nombres científico/común e imágenes
"""

import random

class Planta:
    def __init__(self, nombre_cientifico, nombre_comun_ca, nombre_comun_es, imagenes):
        self.nombre_cientifico = nombre_cientifico
        self.nombre_comun_ca = nombre_comun_ca
        self.nombre_comun_es = nombre_comun_es
        self.imagenes = imagenes if isinstance(imagenes, list) else [imagenes]

    def get_nombre_comun(self):
        if self.nombre_comun_ca:
            return self.nombre_comun_ca
        return self.nombre_comun_es

    def get_imagen_aleatoria(self):
        if self.imagenes:
            return random.choice(self.imagenes)
        return None

    def to_dict(self):
        return {
            "nombre_cientifico": self.nombre_cientifico,
            "nombre_comun_ca": self.nombre_comun_ca,
            "nombre_comun_es": self.nombre_comun_es,
            "imagenes": self.imagenes
        }

    @staticmethod
    def from_dict(d):
        imagenes = d.get("imagenes", [d.get("imagen", "")])
        return Planta(d["nombre_cientifico"], d["nombre_comun_ca"], d["nombre_comun_es"], imagenes)

