import json
import os
from src.models.planta import Planta

DATA_FILE = "plantas.json"

class PlantaRepository:
    def __init__(self):
        self.plantas = []
        self.cargar_plantas()

    def cargar_plantas(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.plantas = [Planta.from_dict(d) for d in data]
        else:
            self.plantas = []

    def guardar_plantas(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.plantas], f, ensure_ascii=False)

    def obtener_todas(self):
        return self.plantas

    def agregar(self, planta):
        self.plantas.append(planta)
        self.guardar_plantas()

    def actualizar(self, indice, planta):
        if 0 <= indice < len(self.plantas):
            self.plantas[indice] = planta
            self.guardar_plantas()

    def eliminar(self, indice):
        if 0 <= indice < len(self.plantas):
            del self.plantas[indice]
            self.guardar_plantas()

    def cantidad(self):
        return len(self.plantas)

