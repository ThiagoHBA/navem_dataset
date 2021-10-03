import numpy as np
import json
import os
import re

index = []
accx = []
accy = []
accz = []
times = []

imu_json = {'dados': []}

def array_sensores(path, txt,index, AccX, AccY, AccZ,tempos):
    arquivo = open(path + txt, 'r')
    lista_dados = arquivo.readlines()

    for i in range(len(lista_dados)):
        linha_amostras = str(lista_dados[i])
        dados_split = linha_amostras.split(":")
        
        if(len(linha_amostras) > 1):
            index.append(float(dados_split[0]))
            AccX.append(float(dados_split[1]))
            AccY.append(float(dados_split[2]))
            AccZ.append(float(dados_split[3]))
            tempos.append(float(dados_split[4]))

    arquivo.close()

    
def escrever_json(path, jso, lista):
    arquivo = path + jso
    pasta = os.path.dirname(os.path.abspath(__file__))
    with open(pasta+'/'+arquivo, 'w') as f:
      json.dump(lista, f, indent = 4)
      

def preparar_json(a,b,c,d,e):
    for i in range(len(a)):
        dado = {
        'index': a[i],
        'AccX': b[i],
        'AccY': c[i],
        'AccZ': d[i],
        'time_sec': e[i],
        }
        imu_json['dados'].append(dado)

num = 3
path_origem = "./Exps_14.08.2021/Exp" + str(num) + "/"
file_name_origem = "exp" + str(num) + ".txt"
path_destino = "./Exp" + str(num) + "/"
json_name = "accelerations.json"

array_sensores(path_origem, file_name_origem,index, accx,accy,accz,times)
preparar_json(index,accx,accy,accz,times)
escrever_json(path_origem, json_name, imu_json)
