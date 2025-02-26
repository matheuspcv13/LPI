empresas = []

def get_empresas(): return empresas

def inserir_empresa(empresa): empresas.append(empresa)

class Empresa:
    def __init__(self, nome, endereco, segmento):
        self.nome = nome
        self.endereco = endereco
        self.segmento = segmento if segmento in ("grãos", "líquidos") else "indefinido"

    def __str__(self):
        formato = '{} {:<19} {} {:<8} {} {:<6} {} {}'
        empresa_formatada = formato.format("|", self.nome, "|", self.endereco, "|", self.segmento)

        return empresa_formatada