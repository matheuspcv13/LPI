empresas = []

def get_empresas(): return empresas

def inserir_empresa(empresa): empresas.append(empresa)

def selecionar_empresas(prefixo_nome = None, estado_origem = None, segmento = None):
    filtros = '\nFiltros -- '
    if segmento is not None: filtros += 'segmento: ' + segmento
    if estado_origem is not None: filtros += ' - estado_origem: ' + estado_origem
    if prefixo_nome is not None: filtros += ' - prefixo_nome: ' + prefixo_nome

    empresas_selecionadas = []
    for empresa in empresas:
        if prefixo_nome and not empresa.nome.startswith(prefixo_nome): continue
        if estado_origem is not None and estado_origem != empresa.estado_origem: continue
        if segmento is not None and empresa.segmento != segmento: continue
        empresas_selecionadas.append(empresa)

    return filtros,empresas_selecionadas

class Empresa:
    def __init__(self, nome, estado_origem, segmento):
        self.nome = nome
        self.estado_origem = estado_origem
        self.segmento = segmento if segmento in ("grãos", "líquidos") else "indefinido"

    def __str__(self):
        formato = '{} {:<21} {} {} {} {}'
        empresa_formatada = formato.format("|", self.nome, "|", self.estado_origem, "|", self.segmento)
        return empresa_formatada