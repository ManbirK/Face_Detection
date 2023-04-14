import cv2
boy = cv2.imread("4f.jpg")


grey_boy = cv2.cvtColor(boy, cv2.COLOR_BGR2GRAY)

face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = face_classifier.detectMultiScale(grey_boy)
print(faces)
# [347 37 240 240]

for (x,y,w,h) in faces:
    #cv2.rectangle(image, start_point, end_point, color,thickness)

    cv2.rectangle(boy,(x,y), (x+w, y+h),(255,0,0),2)

    #crop_pic = img[y:y+h, x:x+w]
    #cv2.imwrite("person_face.jpg", crop_pic)

cv2.imshow("My Image", boy)
cv2.waitKey(0)