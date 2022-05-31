from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#
# # class responsável por controlar o navegador
class controleNavegador:
    #
    # # Construtor responsável por acessar o link desejado
    def __init__(self,link):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.navegador = webdriver.Chrome(chrome_options=options)
        self.navegador.get(link)
    #
    # # Método responsável por selecionara a linha desejada
    def selecionaLinha(self,index):
        selectLinha = self.navegador.find_element(By.ID,'L') # captura o elemento 
        objLinha = Select(selectLinha)                       #Permite a interação com o códiogo como objeto select
        objLinha.select_by_index(index)                      # Seleciona as opções pelo index
    #
    # # Método responsável por selecionara a coluna desejada
    def selecionaColuna(self,index):
        selectColuna = self.navegador.find_element(By.ID,'C')# captura o elemento
        objColuna = Select(selectColuna)                     #Permite a interação com o códiogo como objeto select
        objColuna.select_by_index(index)                     # Seleciona as opções pelo index
    #
    # # Método responsável por selecionar o período desejado 
    def selecionaPeriodo(self,index):
        selectPeriodo = self.navegador.find_element(By.ID,'A') #Encontra o elemento
        objPeriodo = Select(selectPeriodo)                     #Permite a interação com o códiogo como objeto select
        objPeriodo.deselect_all()                              
        objPeriodo.select_by_index(index)                      # Seleciona os index]
    # 
    # # Método responsável por retorna a quantidade de périodos disponíveis.
    def qtPeriodo(self):
        index = 0                                              #inicia a variável index
        selectPeriodo = self.navegador.find_element(By.ID,'A') # Encontra o elemento
        objPeriodo = Select(selectPeriodo)                     # Permite a interação com o códiogo como objeto select
        for cont in objPeriodo.options:                        # Contador do index
            index += 1
        return index
    #
    # # Método que mostra a tabela desejada
    def mostraTabela(self):
        mostrar = self.navegador.find_element(By.XPATH,'/html/body/div/div/center/div/form/div[4]/div[2]/div[2]/input[1]') #procura o elemento especificado
        mostrar.click()
    # 
    # # Método retorna o driver
    def driver_(self):
        return self.navegador 
    def back(self):
        self.navegador.back()