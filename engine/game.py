from pathlib import Path
import json


class Game:
    def __init__(self, level_data):
        self.level_data = level_data

    @property
    def title(self):
        return self.level_data.get("title", "NEUROQUEST")

    @property
    def objective(self):
        return self.level_data.get("objective", "Restaurer le réseau")

    @property
    def graph(self):
        return self.level_data.get("graph", {})

    @property
    def start(self):
        return self.level_data.get("start", "A")

    @property
    def goal(self):
        return self.level_data.get("goal", "F")

    @property
    def dialogues(self):
        return self.level_data.get("dialogues", [])
