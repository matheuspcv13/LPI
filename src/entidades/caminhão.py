caminhões = []

def get_caminhões(): return caminhões

def inserir_caminhão(caminhão): caminhões.append(caminhão)

def selecionar_caminhoes(modelo=None, unidade_carga=None, carga_máxima=None):
    filtros = '\nFiltros -- '
    if unidade_carga is not None: filtros += 'unidade_carga: ' + unidade_carga
    if carga_máxima is not None: filtros += ' - carga_máxima: ' + str(carga_máxima)
    if modelo is not None: filtros += ' - modelo: ' + modelo + ' '

    caminhoes_selecionados = []
    for caminhão in caminhões:
        if modelo is not None and modelo != caminhão.modelo: continue
        if unidade_carga is not None and unidade_carga != caminhão.unidade_carga: continue
        if carga_máxima is not None and carga_máxima < caminhão.capacidade_carga: continue
        caminhoes_selecionados.append(caminhão)

    return filtros,caminhoes_selecionados

class Caminhão:
    def __init__(self, modelo, unidade_carga, capacidade_carga):
        self.modelo = modelo
        self.unidade_carga = unidade_carga if unidade_carga in ("litros", "kilos") else "indefinida"
        self.capacidade_carga = capacidade_carga

    def __str__(self):
        formato = '{} {:<14} {} {:<6} {} {}'
        caminhão_formatado = formato.format("|", self.modelo, "|", self.unidade_carga, "|", str(self.capacidade_carga))

        return caminhão_formatado
