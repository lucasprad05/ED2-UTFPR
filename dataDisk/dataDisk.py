#Data Disk
#Lucas Prado & Erik Noda
#Data Structures 2

import sys

class Game:#-------------------------------------------------------------------------------------------
    def __init__(self, titulo=None, produtora=None, genero=None, plataforma=None, ano=None, classificacao=None, preco=None, midia=None, tamanho=None):
        self.titulo = titulo
        self.produtora = produtora
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao 
        self.preco = preco
        self.midia = midia 
        self.tamanho = tamanho

    def setNome(self,nome):
        self.nome = nome

    def getNome(self):
        return (self.nome)

#TAMANHOS FIXOS-------------------------------------------------------------------------------------------
def escritaTamanhosFixos(entrada,saida, game):
    linha = entrada.readline()
    titulo,produtora,genero,plataforma,ano, classificacao, preco, midia, tamanho = linha.split("|")
    game = Game(titulo,produtora,genero,plataforma,ano, classificacao, preco, midia, tamanho)

    #Titulo
    espacosTitulo = 50 - len(game.titulo)
    saida.write("%s" % game.titulo)
    for i in range (espacosTitulo):
        saida.write(" ")
    saida.write("|")

    #Produtora
    espacosProdutora = 40 - len(game.produtora)
    saida.write("%s" % game.produtora)
    for i in range (espacosProdutora):
        saida.write(" ")
    saida.write("|")
    
    #Genero
    espacosGenero = 25 - len(game.genero)
    saida.write("%s" % game.genero)
    for i in range (espacosGenero):
        saida.write(" ")
    saida.write("|")

    #Plataforma
    espacosPlataforma = 15 - len(game.plataforma)
    saida.write("%s" % game.plataforma)
    for i in range (espacosPlataforma):
        saida.write(" ")
    saida.write("|")

    #Ano
    espacosAno = 4 - len(game.ano)
    saida.write("%s" % game.ano)
    for i in range (espacosAno):
        saida.write(" ")
    saida.write("|")

    #Classificacao
    espacosClassificacao = 12 - len(game.classificacao)
    saida.write("%s" % game.classificacao)
    for i in range (espacosClassificacao):
        saida.write(" ")
    saida.write("|")

    #Preco
    espacosPreco = 7 - len(game.preco)
    saida.write("%s" % game.preco)
    for i in range (espacosPreco):
        saida.write(" ")
    saida.write("|")

    #Midia
    espacosMidia = 8 - len(game.midia)
    saida.write("%s" % game.midia)
    for i in range (espacosMidia):
        saida.write(" ")
    saida.write("|")

    #Tamanho
    espacosTamanho = 7 - len(game.tamanho)
    saida.write("%s" % game.tamanho)
    

#QTDECAMPOS--------------------------------------------------------------------------------------------
def escritaQtdeCampos(entrada,saida, game, tamanho):
    linha = entrada.readline()
    titulo,produtora,genero,plataforma,ano, classificacao, preco, midia, tamanho = linha.split("|")
    game = Game(titulo,produtora,genero,plataforma,ano, classificacao, preco, midia, tamanho)

    saida.write("%s|" % game.titulo)
    saida.write("%s|" % game.produtora)
    saida.write("%s|" % game.genero)
    saida.write("%s|" % game.plataforma)
    saida.write("%s|" % game.ano)
    saida.write("%s|" % game.classificacao)
    saida.write("%s|" % game.preco)
    saida.write("%s|" % game.midia)
    saida.write("%s" % game.tamanho)


#QTDEBytesComeco--------------------------------------------------------------------------------------------
def escritaQtdeBytesComeço(entrada,saida, game):
    linha = entrada.readline()
    titulo,produtora,genero,plataforma,ano, classificacao, preco, midia, tamanho = linha.split("|")
    game = Game(titulo,produtora,genero,plataforma,ano, classificacao, preco, midia, tamanho)

    tamanho = len(linha)
    saida.write("%d" % tamanho)
    saida.write("%s" %game.titulo)
    saida.write("|")
    saida.write("%s" %game.produtora)
    saida.write("|")
    saida.write("%s" %game.genero)
    saida.write("|")
    saida.write("%s" %game.plataforma)
    saida.write("|")
    saida.write("%s" %game.ano)
    saida.write("|")
    saida.write("%s" %game.classificacao)
    saida.write("|")
    saida.write("%s" %game.preco)
    saida.write("|")
    saida.write("%s" %game.midia)
    saida.write("|")
    saida.write("%s" %game.tamanho)
    
   
#QTDEBytesComeco--------------------------------------------------------------------------------------------
def escritaDelimitador(entrada,saida, game):
    linha = entrada.readline()
    titulo,produtora,genero,plataforma,ano, classificacao, preco, midia, tamanho = linha.split("|")
    game = Game(titulo,produtora,genero,plataforma,ano, classificacao, preco, midia, tamanho)
    tamanho = len(linha)
    saida.write("%s" %game.titulo)
    saida.write("|")
    saida.write("%s" %game.produtora)
    saida.write("|")
    saida.write("%s" %game.genero)
    saida.write("|")
    saida.write("%s" %game.plataforma)
    saida.write("|")
    saida.write("%s" %game.ano)
    saida.write("|")
    saida.write("%s" %game.classificacao)
    saida.write("|")
    saida.write("%s" %game.preco)
    saida.write("|")
    saida.write("%s" %game.midia)
    saida.write("|")
    saida.write("%s#" %game.tamanho)
        
    

# MAIN -------------------------------------------------------------------------------------------------
opcao = input("Método?\n")

#TAMANHOS FIXOS
if opcao == "1":
    entrada = open('games.txt','r')
    saida = open('saida.txt','w')

    for i in range (23):
        g= Game()
        escritaTamanhosFixos(entrada,saida,g)
    entrada.close()
    saida.close()

#NUMERO CAMPOS
if opcao == "2":
    entrada = open('games.txt','r')
    saida = open('saida.txt','w')
    for i in range (23):
        g= Game()
        escritaQtdeCampos(entrada,saida,g,9)
    entrada.close()
    saida.close()

#QtdeBytesComeco
if opcao == "3":
    entrada = open('games.txt','r')
    saida = open('saida.txt','w')
    for i in range (23):
        g= Game()
        escritaQtdeBytesComeço(entrada,saida,g)
    entrada.close()
    saida.close()

#escritaDelimitador
if opcao == "4":
    entrada = open('games.txt','r')
    saida = open('saida.txt','w')
    for i in range (23):
        g= Game()
        escritaDelimitador(entrada,saida,g)
    entrada.close()
    saida.close()