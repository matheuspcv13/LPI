from util.gerais import imprimir_objetos
from entidades.caminhão import (inserir_caminhão, Caminhão, get_caminhões, selecionar_caminhoes)
from entidades.empresa import (inserir_empresa, Empresa, get_empresas, selecionar_empresas)

def cadastrar_empresas():
    inserir_empresa(Empresa(nome="JSL Logística", estado_origem="MS", segmento="líquidos"))
    inserir_empresa(Empresa(nome="RodoCargo Transportes", estado_origem="ES", segmento="grãos"))
    inserir_empresa(Empresa(nome="Transvale Logística", estado_origem="SP", segmento="líquidos"))
    inserir_empresa(Empresa(nome="Braspress", estado_origem="MS", segmento="grãos"))
    inserir_empresa(Empresa(nome="GOLLOG", estado_origem="MS", segmento="líquidos"))

def cadastrar_caminhões():
    inserir_caminhão(Caminhão(modelo="Volvo FH16", unidade_carga="litros", capacidade_carga=3000))
    inserir_caminhão(Caminhão(modelo="Scania R450", unidade_carga="kilos", capacidade_carga=2800))
    inserir_caminhão(Caminhão(modelo="Actroz", unidade_carga="litros", capacidade_carga=3200))
    inserir_caminhão(Caminhão(modelo="DAF XF", unidade_carga="kilos", capacidade_carga=2900))
    inserir_caminhão(Caminhão(modelo="Iveco Stralis", unidade_carga="litros", capacidade_carga=2700))

if __name__ == '__main__':
    cadastrar_empresas()
    cabeçalho = "Empresas: nome - estado_origem - segmento"
    imprimir_objetos(cabeçalho='\n' + cabeçalho, objetos=get_empresas())

    filtros, empresas_selecionadas = selecionar_empresas(segmento="líquidos")
    imprimir_objetos(cabeçalho, objetos=empresas_selecionadas, filtros=filtros)

    filtros, empresas_selecionadas = selecionar_empresas(segmento="líquidos", estado_origem="MS")
    imprimir_objetos(cabeçalho, objetos=empresas_selecionadas, filtros=filtros)

    filtros, empresas_selecionadas = selecionar_empresas(segmento="líquidos", estado_origem="MS", prefixo_nome="J")
    imprimir_objetos(cabeçalho, objetos=empresas_selecionadas, filtros=filtros)

    cadastrar_caminhões()
    cabeçalho = "Caminhões: modelo - unidade_carga - capacidade_carga"
    imprimir_objetos(cabeçalho='\n' + cabeçalho, objetos=get_caminhões())

    filtros, caminhões_selecionados = selecionar_caminhoes(unidade_carga="litros")
    imprimir_objetos(cabeçalho, objetos=caminhões_selecionados, filtros=filtros)

    filtros, caminhões_selecionados = selecionar_caminhoes(unidade_carga="litros", carga_mínima=2900)
    imprimir_objetos(cabeçalho, objetos=caminhões_selecionados, filtros=filtros)

    filtros, caminhões_selecionados = selecionar_caminhoes(unidade_carga="litros", carga_mínima=2900, modelo="Actroz")
    imprimir_objetos(cabeçalho, objetos=caminhões_selecionados, filtros=filtros)
