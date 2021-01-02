import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image1.jpg')

print("Enter 1 if you want to see through the items which are in red and the remaining in black.")
print("Enter 2 if you want to see through the items which are in red and the remaining as same.")
print("Enter 3 if you want to see  the items which are in red as white and the remaining in black.")
print("Enter 4 if you want to see through the items which are not in red and the remaining in black.")
c = int(input("Enter your choice: "))
if c == 1 or c == 2 or c == 3 or c == 4:
    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            #hsv defines colors based on human eyes, so we use hsv instead of rgb
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convertung rgb to hsv
            #cv2.imshow("hsv",hsv)
            red = np.uint8([[[0,0,255]]])
            hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
            #print(hsv_red)

            l_red = np.array([0,100,100])
            u_red = np.array([10,255,255])
            #all the objects in red is shown highlighted(i.e. white)
            mask = cv2.inRange(hsv, l_red, u_red)
            if c== 3:
                cv2.imshow("mask",mask)
                #shows the background when red color appeard on screen
            part1 = cv2.bitwise_and(back, back, mask=mask)
            if c == 2:
                cv2.imshow("part1",part1)
            #shows things highlighted which are not red

            mask = cv2.bitwise_not(mask)


            part2 = cv2.bitwise_and(frame, frame, mask=mask)
            #shows everything in red and things other than red are shown in black.
            if c == 4:
                cv2.imshow("part2",part2)
            if c==1:
                cv2.imshow("cloak",part1 + part2)

            if cv2.waitKey(5) == ord('q'):
                break
#else:
    #print("Invalid!!")
cap.release()
cv2.destroyAllWindows()
