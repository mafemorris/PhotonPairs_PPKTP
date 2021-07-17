import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import os
from pylab import rcParams

rcParams['figure.figsize'] = 12, 5

xls = pd.ExcelFile('15-05/405.1408 sin filtros.xlsx')
a = pd.read_excel(xls, 'Hoja 1')
tau_fit = a['tau (s) - HBT Measurement']
g2_fit = a['g^(2)(tau) - HBT Measurement']
tau_none = a['tau (s) - none Fit']
g2_none = a['g^(2)(tau) - none Fit']



def fix(lista):
    for i in range(len(lista)):
        if type(lista[i]) == int:
            pass
        elif 'n' in lista[i]: 
            lista[i] = float(lista[i].replace('n',"e-9").replace(',','.')) 
        elif 'k' in lista[i]: 
            lista[i] = float(lista[i].replace('k',"e3").replace(',','.')) 
        elif 'p' in lista[i]:
            lista[i] = float(lista[i].replace('p',"e-12").replace(',','.'))
        elif 'm' in lista[i]:
            lista[i] = float(lista[i].replace('m',"e-3").replace(',','.'))
        else:
            lista[i] = float(lista[i].replace(',','.'))
    lista = np.array(lista)
    return lista


fix(g2_fit)
fix(tau_fit)
fix(tau_none)
#fix(g2_none)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(tau_fit*10**9,g2_fit*10**-3)
tamaL = 15
tamaN = 12
ax.set_xlabel(r'$\tau$', fontsize=tamaL)
ax.set_ylabel(r'$g^{(2)}(\tau)$', fontsize=tamaL)
ax.set_xticklabels(['{}ns'.format(i) for i in list(np.arange(-20, 20, 5))])
ax.set_yticklabels(['{}k'.format(i) for i in list(np.arange(-0.5, 4.3, 0.5))])
plt.xticks(fontsize=tamaN)
plt.yticks(fontsize=tamaN)
plt.savefig('15-05/sf.png')

