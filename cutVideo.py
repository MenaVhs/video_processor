import cv2 as cv
import numpy as np
import os # operating sys

capture = cv.VideoCapture(os.path.join('RataOscuraAvi.avi'))
h = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
w = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))

# Cropping area
start_row, start_col = int(h * 0.05), int(w * 0.20)
end_row, end_col = int(h * 0.90), int(w * 0.90)

brt = 60  
# Save video
fourcc = cv.VideoWriter_fourcc(*'XVID')
save = cv.VideoWriter('RataSalida.avi', fourcc, 10, (w, h))

# Video captures
while(capture.isOpened()):
    
    ret, frame = capture.read()

    # Cropping an image
    frame = frame[start_row:end_row, start_col:end_col]
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