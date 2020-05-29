from PIL import Image
from PIL.Image import FLIP_TOP_BOTTOM
import Rosto, Camera


def Fauna2():
    Foto_rosto = "Processadas/FiltroImagens.jpg"
    ##Reconhecimento de face p/ posicionar filtro
    x, y, w, h = Rosto.Face_detec(Foto_rosto)

    img1 = Image.open(Foto_rosto)

    ##Filtro RA
    img2 = Image.open('Filtro/ft1.png')
    img3 = Image.open('Filtro/ft2.png')


    #img1 = img1.resize((900,1200))
    size_x, size_y = img1.size
    print("Tamanho da imagem: X= {} --- Y= {}".format(size_x, size_y))

    #print("X= {} --- Y= {} --- W= {} --- H= {}" .format(x, y, (x+w), (y+h)))
    x1,y1 = (x+w), (y+h)

    ######## DEFININDO TAMANHO DO FILTRO COM BASE NO TAMANHO DA FACE
            ### NINHO
    x2 = int(round(( x1 * 50) /100))
    y2 = int(round(( y1 * 30) /100))
    print("X= {} --- Y+ {}".format(x2, y2))
    img2 = img2.resize((x2, y2))
            ### Passaro Arara azul
    x3 = int(round(( x1 * 50) /100))
    y3 = int(round(( y1 * 40) /100))
    img3 = img3.resize((x3, y3))

    ############# POSICIONAMENTO DAS IMAGEM
            ### NINHO
    x4 = int(round(( x * -10) /100))
    y4 = int(round(( y * 45) /100))
    print("X= {} --- Y= {}".format(x, y))
    img1.paste(img2, (x+x4, y-y4), img2)

            ### PASSARO
    x5 = int(round(( x * -15) /100))
    y5 = int(round(( y * 90) /100))
    img1.paste(img3, (x+x5, y-y5), img3)



    img6 = Image.open('Filtro/pass.png')
    ## DEFININDO TAMANHO DO FILTRO
    x1 = int(round(( x1 * 30) /100))
    y1 = int(round(( y1 * 30) /100))
    print("X= {} --- Y+ {}".format(x1, y1))
    img6 = img6.resize((x1, y1))

    ##################### INSERINDO FILTRO Passaros
    img1.paste(img6, (x-280, y-480), img6)

    img6 = img6.transpose ( FLIP_TOP_BOTTOM )
    img6 = img6.rotate(160, expand=1)
    img1.paste(img6, (x-180, y-480), img6)

    img6 = img6.rotate(25, expand=1)
    img1.paste(img6, (x+370, h-440), img6)

    img1.paste(img6, (x-250, y-200), img6)
    img1.paste(img6, (x+370, h+150), img6)


    img1.save('Processadas/Fauna.jpg')
