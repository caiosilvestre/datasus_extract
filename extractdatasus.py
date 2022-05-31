from ExtractDataSus.concatTabela import ferramentaTabela as tabela
#[3,4,5,8,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
tabela.salvar(tabela.scrap('http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sinannet/cnv/hepabr.def',1,[3,4,5,8],[5,8]),'Dataframe')

"""
    
    tabel.salvar(tabela.scrap('link da extração',index da linha,[list das colunas],[list para filtrar colunas com numeros]),nomeDataFrame)

"""