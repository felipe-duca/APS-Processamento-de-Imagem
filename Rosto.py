import cv2

cascPath = "haarcascade_frontalface_default.xml"


faceCascade = cv2.CascadeClassifier(cascPath)

def Face_detec(URL):

    #image = cv2.imread("Foto/foto.png")
    image = cv2.imread(URL)

    #image = cv2.imread("ft12.png")


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detecta as faces
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    print("Detectou-se {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return x, y, w, h