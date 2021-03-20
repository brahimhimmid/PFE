import cx_Oracle 
import cv2
import os
import glob

cam = cv2.VideoCapture(0)
cam.set(3, 640) # définir la largeur de la vidéo
cam.set(4, 480) # définir la hauteur vidéo
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input('\n entrer id et cliquer sur <entree>==>  ')
first_name=input('\n  entrer le prenom de l etudiant et cliquer sur  <entree> ==>  ')
last_name=input('\n  entrer le nom de l etudiant et cliquer sur  <entree> ==>  ')
print("\n [INFO]  Regardez la camera et attendez...")


try:
    conn1 = cx_Oracle.connect('SYSTEM/lghazwa2020@localhost')
    cursor1=conn1.cursor()        
    stmt=("insert into etudiant values(:id, :first, :last)")
    cursor1.execute(stmt,(face_id,first_name,last_name))
    conn1.commit()
    cursor1.close()
    conn1.close()
except cx_Oracle.DatabaseError as e:
    print(e)


# Initialiser le nombre individuel de visage de perssonne
count = 0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        # enregistre l'image
        cv2.imwrite(str(face_id) + '.' +  str(count) + ".jpg", gray[y:y+h,x:x+w])
        try:
            conn = cx_Oracle.connect('SYSTEM/lghazwa2020@localhost')
            cursor=conn.cursor()
            with open(str(face_id) + '.' +str(count) +".jpg", 'rb') as f:
                data=f.read()
                stm=("insert into images values(:nm, :con, :img)")
                cursor.execute(stm,(face_id, count, data))
                conn.commit()

        except cx_Oracle.DatabaseError as e:
             print(e)
    
    cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff # appuyer sur echap pour quiter
    if k == 27 :
        break
    elif count >= 50: # Prenez 30 image de visage et arrêtez la vidéo
         break
# Faire  de nettoyage de data
for zippath in glob.iglob(os.path.join('*.jpg')):
    os.remove(zippath)
              
print("\n [INFO] Etudient ajoute ")
cam.release()
cv2.destroyAllWindows() 