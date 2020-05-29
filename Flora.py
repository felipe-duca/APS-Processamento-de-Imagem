import Rosto
from PIL import Image

def Flora():
    Moldura = "Filtro/quad.png"
    #######  Reconhecimento
    Foto_rosto = "Processadas/FiltroVerde.jpg"
    x, y, w, h = Rosto.Face_detec(Foto_rosto)



    img1 = Image.open(Foto_rosto)

    size_x, size_y = img1.size

    ## POSICIONAMENTO DA MOLDURA
    img2 = Image.open(Moldura)
    img2 = img2.resize((size_x, size_y))
    img1.paste(img2, (0, 0), img2)

    img1.save("Processadas/Flora.jpg")

