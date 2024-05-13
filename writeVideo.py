import cv2 as cv
import os # operating sys

capture = cv.VideoCapture(os.path.join('RataOscuraAvi.avi'))
h = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
w = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
brt = 60  
# Save video
fourcc = cv.VideoWriter_fourcc(*'XVID')
save = cv.VideoWriter('RataSalida.avi', fourcc, 10, (w, h))

# Video captures
while(capture.isOpened()):
    
    ret, frame = capture.read()

    # Brillo
    frame[frame < 255-brt] += brt 
    
    # Video transform
    grayVideo = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    t, dst = cv.threshold(grayVideo, 61, 255, cv.THRESH_BINARY)

    cv.imshow('Rata DST', dst)
    
    # save.write(dst)

    if cv.waitKey(5) & 0xFF == ord('s') or not ret: # s = stop
        break


save.realise()
capture.realise()
cv.destroyAllWindows