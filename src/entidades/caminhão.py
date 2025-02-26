caminhões = []

def get_caminhões(): return caminhões


def inserir_caminhão(caminhão): caminhões.append(caminhão)


class Caminhão:
    def __init__(self, modelo, capacidade_carga, articulado):
        self.modelo = modelo
        self.capacidade_carga = capacidade_carga
        self.articulado = articulado

    def __str__(self):
        formato = '{} {:<19} {} {:<8} {} {:<6} {} {}'
        caminhão_formatado = formato.format("|", self.modelo, "|", self.capacidade_carga, "|", self.articulado)

        return caminhão_formatado
