import cv2

# read image
# img=cv2.imread('E:/photo/2.jpg')
# cv2.imshow('frame',img)
# cv2.waitKey(0)

capture = cv2.VideoCapture(0)
while True:
    a, frame = capture.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(20) & 0xFF == 27:
        break
capture.release()
cv2.destroyAllWindows()
