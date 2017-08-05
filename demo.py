import cv2
import numpy as np
import copy
import os
import time

cap = cv2.VideoCapture(1)
cap.set(cv2.cv.CV_CAP_PROP_FPS, 1) 
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 360)

winName1 = "Live feed"
winName2 = "Processed Image"
winName3 = "edges"

cv2.startWindowThread()
cv2.namedWindow(winName1)
cv2.namedWindow(winName2)
cv2.namedWindow(winName3)

while True:
    try:
        os.system("clear")
        ret, frame = cap.read()
        
        if ret:
            # keep original frame safe
            original = copy.deepcopy(frame)

            # apply median blur to even out the colors
            median = cv2.medianBlur(frame, 15)

            # detect edges
            edges = cv2.Canny(median, 180,180)
            edgesori = copy.deepcopy(edges)

            # find contours and draw its boundry
            cnt, h = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            print "I see %d objects in view\n\n" % (len(cnt))
            #sys.stdout.write("I see %d objects in view\r" % (len(cnt)))

            for c in cnt:
                cv2.drawContours(frame, [c], -1, (0, 0, 0), -1)
                
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.04 * peri, True)
                sides = len(approx)

                # calculating %age diff in edges length
                x,y,w,h = cv2.boundingRect(c)
                diff = ((max(w,h) - min(w,h)) / float(min(w,h))) * 100

                r = 0
                g = 0
                b = 0
                
                total_pixels = 0
                
                try:
                    for i in range(w):
                        for j in range(h):
                            b = b + original[x + i, y + j][0]
                            #print "yaha"
                            g = g + original[x + i, y + j][1]
                            #print "kaha"
                            r = r + original[x + i, y + j][2]
                            #print "phir"
                            total_pixels = total_pixels + 1
                except Exception, e:
                    print " "
                    #print "error in calculating color"
                    #print str(e)

                r = float (r) /  total_pixels
                g = float (g) /  total_pixels
                b = float (b) /  total_pixels

                if r > g and r > b:
                    print "Color red"
                elif g > b and g > r:
                    print "Color green"
                else:
                    print "Color blue"
                
                

                if sides == 7 or sides == 8:
                    #sys.stdout.write("I see a circle\r")
                    print "I see a circle"

                elif sides == 4 and diff < 5:
                    #sys.stdout.write("I see a square\r")
                    print "I see a square"

                elif sides == 4 and diff > 5:
                    #sys.stdout.write("I see a rectangle\r")
                    print "I see a rectangle"

                elif sides == 3:
                    #sys.stdout.write("I see a triangle\r")
                    print "I see a triangle"
                else:
                    #sys.stdout.write("I see a %d sided figure\r" % (sides))
                    print "I see a %d sided figure" % (sides)

                area = cv2.contourArea(c)
                #sys.stdout.write("Relative area : %f\r" % (area))
                print "Relative Area : " + str(area)

                #print "\nFeatures:\n"
                #print "%d, %f" % (sides, area)
                #print "=======================\n\n"
                #sys.stdout.flush()
                print "\n\n"
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
            ret,thresh = cv2.threshold(gray,130,255,1)
            final = cv2.bitwise_not(thresh)
            
            
            
            cv2.imshow(winName1, original)
            cv2.imshow(winName2, final)
            cv2.imshow(winName3, edgesori)
            #print cnt
            #exit()

            
            
        else:
            print "ret returned false when reading frame"
            break
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(1)
    except:
        continue
        
cap.release()
cv2.destroyWindow(winName1)
cv2.destroyWindow(winName2)
cv2.destroyWindow(winName3)
