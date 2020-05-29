import Filtro_imagens, Filtro_Verde, Camera

URL = 0

def FiltroFauna():
    Camera.captura(URL)
    Filtro_imagens.Fauna()

def FiltroFlora():
    Camera.captura(URL)
    Filtro_Verde.Flora()

if __name__ == "__main__":
    FiltroFauna()
    FiltroFlora()