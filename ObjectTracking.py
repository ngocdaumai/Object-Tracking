import cv2

capture = cv2.VideoCapture(0)

tracker = cv2.TrackerMIL_create()
# tracker = cv2.TrackerKCF_create()
# tracker = cv2.TrackerTLD_create()
# tracker = cv2.TrackerMedianFlow_create()
# tracker = cv2.TrackerCSRT_create()
# tracker = cv2.TrackerMOSSE_create()

_, image = capture.read()
boundingBox = cv2.selectROI("ObjectTracking", image, False)
tracker.init(image, boundingBox)

def drawingBox(image,boundingBox):
    x, y, w, h = int(boundingBox[0]), int(boundingBox[1]), int(boundingBox[2]), int(boundingBox[3])
    cv2.rectangle(image, (x, y), ((x + w), (y + h)), (0, 0, 255), 3, 3 )
    cv2.putText(image, "Tracking", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

while True:
    timer = cv2.getTickCount()
    _, image = capture.read()
    _, boundingBox = tracker.update(image)

    if _:
        drawingBox(image, boundingBox)
    else:
        cv2.putText(image, "DisAppear", (50, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    fps = cv2.getTickFrequency()/ (cv2.getTickCount()-timer)
    cv2.putText(image,str(int(fps)), (20, 20), cv2.FONT_ITALIC, 0.2, (0, 0, 225), 2)
    cv2.imshow("ObjectTracking", image)
    if cv2.waitKey(1)==ord("s"):
        break
cv2.release()
cv2.destroyAllWindows()