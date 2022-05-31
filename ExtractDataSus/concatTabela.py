
import pandas as pd
from .eleven import controleNavegador as driver
from .here2help import tabela as scrap

# 
# # class responsável por concatenar as colunas
class ferramentaTabela:
    # Scrap
    # # Método responsável por concatenar as tabelas e chamar metodos de outras classes.
    """
        link variavel 'variável' 'string' referente ao link do site
        indexLinha 'variável' 'int' referente o index da linha desejada para extração
        indexColuna 'list' 'int' referente as colunas a serem extraidas
        filtroColunaNumero 'list' 'int' refere as colunas que possuem numeros indesejaveis Ex: '2316516515_nome da capital'
    """
    def scrap(link,indexLinha,indexColunas,filtroColunaNumero):
        navegador = driver(link)                                    # envia o link para o metodo da classe do arquivo eleven.py
        listaColuna = scrap.todasOpcoesColuna(navegador.driver_())  #retorna uma lista de string de todas as opções de colunas
        listaLinha = scrap.todasOpcoesLinha(navegador.driver_())    #retorna uma lista de string de todas as opções de linha
        df2 = []    # inicia lista df2
        for anos in range(0,navegador.qtPeriodo()):     # Looping para pecorrer todos os periodos disponíveis.
            navegador.selecionaLinha(indexLinha)        # Método para selecionar a linha desejada
            navegador.selecionaPeriodo(anos)            # Método para selecionar a Periodo desejada
            cont = 0
            df1 = []
            df2 = []
            for index in indexColunas:              # Looping para pecorrer as quantidades de colunas escolhidas
                navegador.selecionaColuna(index)    # Método para selecionar a coluna desejada
                navegador.mostraTabela()            # clicka no botão mostrar tabela
                # 
                # # Parte responsável por gerenciar a concatenação das tabelas
                if cont == 0:
                    df1 = scrap.puxa(index,listaColuna,navegador.driver_(),listaLinha[indexLinha],filtroColunaNumero) # Puxa as informações disponíveis nas tabelas
                    df1 = df1.drop(index = 0)
                else:
                    df2= scrap.puxa(index,listaColuna,navegador.driver_(),listaLinha[indexLinha],filtroColunaNumero) # Puxa as informações disponíveis nas tabelas
                    df2 = df2.drop(columns=['ano'])
                    df1 = df1.merge(df2, how='left', on= listaLinha[indexLinha] )
                cont = cont + 1
                navegador.back()
            if anos == 0 :
                tabelaFinal = df1
            else:
                tabelaFinal = pd.concat([tabelaFinal,df1],ignore_index=True)
        return tabelaFinal.fillna(0) # Retorna tabela
    
    # 
    # # Método utilizado para salvar em DataFrame extensão .csv
    """
        df referente a tabela >>> DataFrame
        nomeDataFrame referente ao nome do DataFrame irá ser salvo
    """
    def salvar(df,nomeDataFrame):
        df.to_csv( nomeDataFrame+'.csv', index=False)
