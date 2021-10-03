import os
import json
from sensores import Dados
from graphs_util import GraphsUtil

def main():
    pasta = "./MPU6050/Exps_24.08.2021/Exp1/"
    arquivo = "accelerations.json"
    sensor = json.load(open(pasta + arquivo,"r"))

    '''Extrai aceleração em m/s²'''
    dados = Dados(sensor)
    accX, accY, accZ, accCount = dados.obter_acc(16384)

    '''Obtem e processa os dados para milisegundos'''
    tempos = dados.obter_tempos()
    tempos = tempos - tempos[0]
    tempos = tempos/1000000

    '''Calcula velocidade a partir dos dados de aceleração e tempo'''
    velX = dados.obter_velocidade_geral(accX, tempos)
    velY = dados.obter_velocidade_geral(accY, tempos)
    velZ = dados.obter_velocidade_geral(accZ, tempos)

    '''Mostra os gráficos dos dados'''
    graphs = GraphsUtil(velX, velY, velZ, tempos, "Velocidade")
    graphs.plot3AxisData()

if __name__ == "__main__":
    main()    
        
    
