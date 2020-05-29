from PIL import Image, ImageFilter, ImageOps
from matplotlib import pyplot as plt
import Camera, Fauna2

def Fauna():

    # Abrindo uma imagem
    img = Image.open("Foto/Imagem.jpg")


    #Quebra em canais
    #Faz um gausiano em cada canal
    #Aumenta o brilho em azul e verde, diminui em vermelho
    #junta tudo
    r,g,b = img.split()

    #Gaussiano
    k = [1,2,1,2,4,2,1,2,1]
    filtro = ImageFilter.Kernel((3,3),k)
    r = r.filter(filtro)
    g = g.filter(filtro)
    b = b.filter(filtro)

    #Equalizando a imagem
    r = ImageOps.equalize(r)
    g = ImageOps.equalize(g)
    b = ImageOps.equalize(b)

    #Brilho
    ref=[]
    lut=[]
    for i in range(256):
        ref.append(i)
        val = i+50
        if val>255: val=255
        if val<0: val=0
        lut.append(val)

    g = g.point(lut)
    b = b.point(lut)

    #Brilho
    ref=[]
    lut=[]
    for i in range(256):
        ref.append(i)
        val = i-50
        if val>255: val=255
        if val<0: val=0
        lut.append(val)

    r = r.point(lut)

    img = Image.merge('RGB', (r, g, b))
    img.save("Processadas/FiltroImagens.jpg")

    Fauna2.Fauna2()
