from bs4 import BeautifulSoup
import pandas as pd
import re
# filtro para titulos das colunas
pattern = r'[0-9]'

class tabela:
    def todasOpcoesColuna(driver):
        site = BeautifulSoup(driver.page_source,'lxml')
        lista=[]
        li = []
        index = -1
        for titulos in site.find(id='C'):
            li = []
            celula = titulos.get_text().replace("\n","").replace('    ','').replace(" ","_").lower()
            li.append(celula)
            lista.extend(li)
            index += 1
        lista.pop(0)
        return lista
    
    def todasOpcoesLinha(driver):
        site = BeautifulSoup(driver.page_source,'lxml')
        lista=[]
        li = []
        index = -1
        for titulos in site.find(id='L'):
            li = []
            celula = titulos.get_text().replace("\n","").replace('    ','').replace(" ","_").lower()
            li.append(celula)
            lista.extend(li)
            index += 1
        lista.pop(0)
        return lista

    def puxa(indexColuna,lista,driver,colunaMerge,filtroColunaNumero):
        site = BeautifulSoup(driver.page_source,'lxml') # Puxa HTML do Site
        tabela=[]         # tabela >>> Armazena os valores das linhas
        celulas=[]        # declaração das listas, celulas >>> Separar os valores em suas respectivas linhas
        tituloColuna = []
        colunaValidada = 0
        tituloColuna.append('ano')
        for titulos in site.find_all("th"): # For para filtrar e apenas capturar os textos dentro da tag 
            if titulos.get_text().replace("\n","").replace('    ','').replace(" ","_").lower() == colunaMerge:
                tituloColuna.append(titulos.get_text().replace("\n","").replace(" ","_").lower())
#            elif 5 == indexColuna or 8 == indexColuna:
#                tituloColuna.append(lista[indexColuna]+re.sub(pattern, '', titulos.get_text().replace("\n","").replace('    ','').replace(" ","_").lower()))
            else:
                for index in filtroColunaNumero:
                    if indexColuna == index:
                        colunaValidada = 1
                        tituloColuna.append(lista[indexColuna]+re.sub(pattern, '', titulos.get_text().replace("\n","").replace('    ','').replace(" ","_").lower()))
                        break
                    else:
                        colunaValidada = 0
                if colunaValidada == 0:
                    tituloColuna.append(lista[indexColuna]+' '+titulos.get_text().replace("\n","").replace(" ","_").lower())
        celulas=[]
        for linhas in site.select('tbody > tr[align=right]'):
            celulas.append(anoTipoTabela('ano',driver))
            for linha in linhas.find_all("td"):
                celulas.append(linha.get_text().replace("\n","").replace(" ","").replace("-","0"))
            tabela.append(celulas)
            celulas=[]
        df = pd.DataFrame(tabela, columns = tituloColuna)
        return df

# 
# # Função com objetivo de retornar os titulos para serem acrescentados nas colunas das tabelas
def anoTipoTabela(opcao,driver):
    site = BeautifulSoup(driver.page_source,'lxml')
    titulos = site.find('thead')          #Procura a Tag 'thead' e captura
    periodos= titulos.find('td')          #dentro da Tag 'thead' encontre o 'td'
    titulos=[]                            #Zera a variável 'titulos' e atribui uma lista zerada a ela
    for titulo in periodos:               #For utilizado para pecorrer os titulos
        titulos.append(titulo.get_text()) #adiciona os titulos a lista titulos
    if opcao == 'ano':
        return titulos[7].replace(' ','') #captura o ano da tabela
    elif opcao == 'tipo':
        return titulos[3]                 #captura o tipo da tabela