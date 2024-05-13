import cv2 as cv
import os # operating sys

capture = cv.VideoCapture(os.path.join('LoroA.avi'))

# Setup video writer

# Capture Properties
# print("Altura: ", capture.get(cv.CAP_PROP_FRAME_HEIGHT))
# print("Anchura: ", capture.get(cv.CAP_PROP_FRAME_WIDTH))
# print("Frames: ", capture.get(cv.CAP_PROP_FRAME_COUNT))
# print("FPS : ", capture.get(cv.CAP_PROP_FPS))

h = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
w = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))

# Save video
fourcc = cv.VideoWriter_fourcc(*'XVID')
save = cv.VideoWriter('RataSalida.avi', fourcc, 10, (w, h))

# Video captures

while(capture.isOpened()):
    
    ret, frame = capture.read()

    # Video transform
    grayVideo = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    t, dst = cv.threshold(grayVideo, 7, 255, cv.THRESH_BINARY)

    save.write(dst)
    cv.imshow('Rata DST', dst)

    if cv.waitKey(30) & 0xFF == ord('s'): # s = stop
        break
    if not ret:
        save.release()
        break

capture.release()

cv.destroyAllWindows