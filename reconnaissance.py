import cv2
import numpy as np
import os
import cx_Oracle 
import datetime

conn = cx_Oracle.connect('SYSTEM/lghazwa2020@localhost')
names=[]
name=[]
a=[]
b=[]
i=0
names.append('none')
a.append('none')
b.append('none')
cursor =conn.cursor()
cursor1=conn.cursor()
cursor3=conn.cursor()

cursor3.execute("DELETE FROM absence")
conn.commit()

cursor.execute("SELECT first_name||' '||last_name as a FROM etudiant ORDER BY no")

result = cursor.fetchall()
for x in result:
    names.append(x[0])




recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#initialiser le compteur
id = 0


# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Initialisez et démarrez la capture vidéo en temps réel
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(10), int(10)),
       )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id,match = recognizer.predict(gray[y:y+h,x:x+w])

        #Vérifiez si la confiance est moins eux 100 ==>  0  est match parfait
        if (match<=55):
            id = names[id]

            if (a[i]!=id):
                a.append(id)
                i=i+1
                 
                 
        else:
            id ='uknown' 
        
 

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)


    cv2.imshow('camera',img)
  


    k = cv2.waitKey(10) & 0xff # appuyer sur echape pour quiter
    if k == 27:
        break

absc=[]
absc=list(set(names)-set(a))
s=0
conn2 = cx_Oracle.connect('SYSTEM/lghazwa2020@localhost')
cursor2=conn2.cursor()
z=datetime.datetime.now()
dt=z.strftime("%d/%m/%Y  %H:%M")

for x in absc:
   cursor2.execute("insert into absence(nom_prenom,dateabs) values(:v, :h)",(x,dt))
   conn2.commit()
   s=s+1

cursor2.close()

# faire de nettoyage
print("\n [INFO] Exit")
cam.release()
cv2.destroyAllWindows()
