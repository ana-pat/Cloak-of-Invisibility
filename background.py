import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()
    if ret:
        #this command opens the camera.
        cv2.imshow("image",back)
        #when your camera is ON if u press 'q' on your keyboard then a picture in clicked and is saved in your folder by the commands below.
        if cv2.waitKey(5) == ord('q'):
            #this command saves the image in your folder with name image.
            cv2.imwrite('image.jpg',back)
            break

cap.release()
cv2.destroyAllWindows()
