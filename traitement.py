from PIL import Image
import numpy as np
import cv2
import cx_Oracle
import io 
import PIL

id=[]
faceSamples=[]
try:
    a=[]
    s=[]
    conn = cx_Oracle.connect('SYSTEM/lghazwa2020@localhost')
    cursor=conn.cursor()
    cursor1=conn.cursor()
    cursor.execute("""select image from images ORDER BY no,counter""")
    cursor1.execute("""select no from images ORDER BY no""")
    rows = cursor.fetchall()
    ids=cursor1.fetchall()
    for x in rows:
        data=x[0]
        file=io.BytesIO(data.read())
        img1=Image.open(file)
        op=np.array(img1,'uint8')
        a.append(op)
    conn.commit()
    
    for y in ids:
        s.append(y)

    conn.close()

except cx_Oracle.DatabaseError as e:
    print(e)

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
i=0
for x in a: 
   PIL_img=a[i] # le convertir en gris
   img_numpy =np.array(PIL_img,'uint8')
   faces = detector.detectMultiScale(img_numpy)
   for (x,y,w,h) in faces:
          faceSamples.append(img_numpy[y:y+h,x:x+w])
          id.append(s[i])

   i=i+1

recognizer.train(faceSamples,np.array(id))
recognizer.write('trainer.yml') 

print("\n [INFO] {0} visage(s) traite. Exiting Program".format(len(np.unique(id))))