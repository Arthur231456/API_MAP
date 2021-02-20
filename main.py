import requests
DATA_DIR = "data"


class Window:
    def __init__(self):
        self.ll = "55,55"
        self.spn = "1,1"
        self.img = f"{DATA_DIR}/map.png"

    def change_scale(self):
        pass