empresas = []

def get_empresas(): return empresas

def inserir_empresa(empresa): empresas.append(empresa)

class Empresa:
    def __init__(self, nome, capacidade_logística, segmento):
        self.nome = nome
        self.capacidade_logística = capacidade_logística
        self.segmento = segmento if segmento in ("animal", "carga") else "indefinido"

    def __str__(self):
        formato = '{} {:<19} {} {:<8} {} {:<6} {} {}'
        empresa_formatada = formato.format("|", self.nome, "|", self.capacidade_logística, "|", self.segmento)

        return empresa_formatada
