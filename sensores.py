import os
import json
import math
import numpy as np
from numpy.linalg import inv
import math
from functools import reduce
from matplotlib import pyplot as plt
import scipy.integrate as integrate
import statistics


class Dados:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        
    def obter_acc(self, sensitivityConstant):
        accX = np.array([]).astype(float)
        accY = np.array([]).astype(float)
        accZ = np.array([]).astype(float)
        accCount = np.array([]).astype(float)
        
        for acc in self.jsonData["dados"]:
            accX = np.append(accX, self.__obter_userAccelerometer(acc["AccX"], sensitivityConstant))
            accY = np.append(accY ,self.__obter_userAccelerometer(acc["AccY"], sensitivityConstant))
            accZ = np.append(accZ ,self.__obter_userAccelerometer(acc["AccZ"], sensitivityConstant))
            
        for i in range(len(accX)):  
            accCount = np.append(accCount, np.array([accX[i],accY[i],accZ[i]]))

        return accX, accY, accZ, accCount

    def __obter_userAccelerometer(self, acc, sensitivityConstant):
        gravityForce = 9.80665
        return (acc / sensitivityConstant) * gravityForce
    
        
    def obter_gyr(self):
        gyroX = np.array([]).astype(float)
        gyroY = np.array([]).astype(float)
        gyroZ = np.array([]).astype(float)

        for gyr in self.jsonData["dados"]:
            gyroX = np.append(gyroX, gyr["GyrX"])
            gyroY = np.append(gyroY, gyr["GyrY"])
            gyroZ = np.append(gyroZ, gyr["GyrZ"])

        return gyroX, gyroY, gyroZ

    def obter_tempos(self):
        tempos = np.array([]).astype(float)
        for time in self.jsonData["dados"]:
            tempos = np.append(tempos, time["time_sec"])

        return tempos

    
    def obter_rpy(self):
        roll = np.array([]).astype(float)
        pitch = np.array([]).astype(float)
        yaw = np.array([]).astype(float)
        
        for rpy in self.jsonData["dados"]:
            roll = np.append(roll, rpy["Roll"])
            pitch = np.append(pitch, rpy["Pitch"])
            yaw = np.append(yaw, rpy["Yaw"])

        return roll, pitch, yaw

    def obter_aaWorld(self):
        aaWorldX = np.array([]).astype(float)
        aaWorldY = np.array([]).astype(float)
        aaWorldZ = np.array([]).astype(float)
        
        for aaW in self.jsonData["dados"]:
            aaWorldX = np.append(aaWorldX, aaW["aaWorldX"])
            aaWorldY = np.append(aaWorldY, aaW["aaWorldY"])
            aaWorldZ = np.append(aaWorldZ, aaW["aaWorldZ"])

        return aaWorldX, aaWorldY, aaWorldZ
            
    def product(lista): 
        return reduce(lambda acumulado, atual: acumulado * atual, lista)

    def lagrange(x, fx):                                                              
        L = lambda num, xi: Dados.product((num - xj) / (xi - xj) for xj in x if xj != xi)
        return lambda num: sum([yi * L(num, xi) for xi, yi in zip(x, fx)])
        
    def integration_simpson(a, b, f, delta_t, nb_ech):
        h = (b-a)/np.double(nb_ech)
        z = np.double(f(a)+f(b))

        for i in range(1,nb_ech,2) :
            z += 4 * f(a+(i*h))
        for i in range(2, nb_ech-1, 2):
            z += 2 * f(a+(i*h))

        val_int =  z*(h/3)
        val_int *= delta_t

        return val_int


    def integration_trapeze(a, b, delta_t):
        f_a = a
        f_b = b
        val_int = (f_a+f_b)/2.
        val_int *= delta_t

        return val_int

    def obter_velocidade_geral(self, acc, t):
        vel = []
        vel.append(0)
        contador = 0

        for j in range(len(t) - 1):
            delta_t = t[j+1] - t[j]
            velocidade_inst = Dados.integration_trapeze(acc[j],acc[j+1], delta_t)
            vel.append(vel[j] + velocidade_inst)
            contador += 1
        return vel
    
