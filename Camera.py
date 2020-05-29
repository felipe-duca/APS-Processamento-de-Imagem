import cv2

def captura(URL):
    captura = cv2.VideoCapture(URL)
    while (1):
        ret, frame = captura.read()
        cv2.imshow("Video", frame)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            cv2.imwrite("Foto/Imagem.jpg", frame)
            break

    captura.release()
    cv2.destroyAllWindows()