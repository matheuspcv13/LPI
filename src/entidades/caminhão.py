caminhões = []

def get_caminhões(): return caminhões

def inserir_caminhão(caminhão): caminhões.append(caminhão)

class Caminhão:
    def __init__(self, modelo, unidade_carga, capacidade_carga):
        self.modelo = modelo
        self.unidade_carga = unidade_carga if unidade_carga in ("litros", "kilos") else "indefinida"
        self.capacidade_carga = capacidade_carga

    def __str__(self):
        formato = '{} {:<19} {} {:<8} {} {:<6} {} {}'
        caminhão_formatado = formato.format("|", self.modelo, "|", self.unidade_carga, "|", str(self.capacidade_carga))

        return caminhão_formatado
