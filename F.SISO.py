# MISO MMH 20241217

from cycler import K
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt



def calculo_nse(Q_o, Q_si):  # Q_o : Q observado Q_si: Q simulado
    obs = np.array(Q_o)
    sim = np.array(Q_si)
    numerador = np.sum((obs - sim)**2)
    denominador = np.sum((obs - np.mean(obs))**2)
    nse = 1 - (numerador / denominador)
    return nse

resultados = pd.DataFrame(columns=['b0','a1', 'delta1','NSE','1-NSE'])


# Leer datos desde el archivo plano

ruta_csv = 'C:/Users/frubiano/Desktop/f.parcial.csv'  # Ruta Archivo 
datos = pd.read_csv(ruta_csv)

P1 = datos['P1'].values  # Columna 1 del CSV

Qobs = datos['Qobs'].values  # Columna 3 del CSV
Qsim = [0] * len(P1)  # Inicializar Qsim

for i in range(10000):
    b0 = random.uniform(0.04, 0.05)  # Coeficiente b01
    a1 = random.uniform(-0.98,-0.95 )  # Coeficiente a1
    delta1 = int(random.uniform(16, 18))  # Retardo para P1
    

    # Datos de entrada

    
    

    # Calcular Qsim(k)
    for k in range(len(P1)):
        if k >= delta1 :  # Verifica índices válidos
                if k==1:
                     Qsim[k] = (b0 * P1[k - delta1] -
                       a1 * Qobs[k - 1])
                     
                elif k>1:
                     Qsim[k] = (b0 * P1[k - delta1] -
                       a1 * Qsim[k - 1])                   
        else:
            Qsim[k] = 0  # Valor por defecto para índices no válidos
        

    nse = calculo_nse(Qobs, Qsim)


    # Imprimir resultados
    #print("Resultados de Q(k):", Qsim)
    resultados.loc[i, 'b0'] = b0
    
    resultados.loc[i, 'a1'] = a1
    resultados.loc[i, 'delta1'] = delta1
    
    resultados.loc[i, 'NSE'] = nse
    resultados.loc[i, '1-NSE'] = 1-nse

#nse = calculo_nse(Qobs, Qsim)  # Llamar a la función para NSE
#print(f"El coeficiente NSE es: {nse}")

resultados.to_excel('/Users/frubiano/Desktop/ResultadoSISO.xlsx',index=False)

