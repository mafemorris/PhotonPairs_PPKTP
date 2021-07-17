import numpy as np
import matplotlib.pylab as plt
import os
import pandas as pd
import glob
from PIL import Image
#plt.rcParams.update({
#    "text.usetex": True,
#    "font.family": "serif",
#    "font.serif": ["Garamond"],
#})

#Auxiliary functions
def center_data(data,xprop0,xprop1,yprop0,yprop1):
    xlim = [int(data.shape[1]*xprop0), int(data.shape[1]*xprop1)]
    ylim = [int(data.shape[0]*yprop0), int(data.shape[0]*yprop1)]
    return data[ylim[0]:ylim[1],xlim[0]:xlim[1]]

def threshold(data,thresh,reset,debajo,reset2):
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i,j] > thresh:
                data[i,j] = reset
            if data[i,j] < debajo:
                data[i,j] = reset2 

#Cargar datos

thresh = 1225
reset = 1230
debajo = 1125
reset2 = 1074

#Limits
xprop0 = 0.2
xprop1 = .9
yprop0 = 0
yprop1 = 0.8


def ec(name):
    data = np.loadtxt('40mW 2/anillos/a1/{}C.TXT'.format(name))

    plt.figure()
    #Centering the data
    threshold(data,thresh,reset,debajo,reset2)
    data = center_data(data,xprop0,xprop1,yprop0,yprop1)

    x = np.linspace(0,1,data.shape[1])
    y = np.linspace(0,1,data.shape[0])

    ax = plt.gca()
    plt.contourf(x, y, data, 100)
    plt.colorbar(label='Intensity (arb. unit)')
    ax.set_aspect(1)
    plt.axis('off')
    plt.title(r'T={}$^o$C'.format(name))
    plt.savefig('40mW 2/anillos/a1/{}C.png'.format(name),dpi=600,bbox_inches='tight')

def video(dur):
    fp_in = "*C.png"
    fp_out = "image.gif"

    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
    img.save(fp=fp_out, format='GIF', append_images=imgs,
            save_all=True, duration=dur, loop=0)

for i in [43]:
    ec(i)

#video(300)

