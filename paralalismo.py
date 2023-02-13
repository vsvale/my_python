import random
import time
import threading
import datetime

numeros = [] #lista compartilhada entre as Threads
global gerar_arquivo
gerar_arquivo = False #Flag para gerar arquivo

def geranumeros(quantidade):#gerar quantidade de numeros aleatorios que serão salvos em um arquivo
  global gerar_arquivo
  while(True):#rodar infinitamente
    if not gerar_arquivo:#não gerar arquivo enquanto gera os numeros
      for i in range(quantidade):
        numeros.append(random.random())
      gerar_arquivo = True#passa true para gerar o arquivo
      time.sleep(10)

def escrevearqv(numeros):
  global gerar_arquivo
  while(True):#rodar infinitamente
    if len(numeros)>0 and gerar_arquivo:#lista de numeros não esta vazia e o gerar arquivo esta True podemos gerar arquivo
      nome_arquivo = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.txt'#Mais proximo que consegui nesse momento de YYYYMMDDHHMMssSS
      logs = open(nome_arquivo,'w')
      for number in numeros:#grava todos os numeros gerados até então     
        logs.writelines(str(number)+'\n')
      logs.close()
      gerar_arquivo= False#passa falso para poder gerar mais numeros
      time.sleep(10)