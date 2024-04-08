from PIL import ImageGrab
import cv2
import numpy as np

def click_event(event, x, y, flags, params): 
    global cr_img # VERY ILLEGAL but whatever
  
    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 
  
        # displaying the coordinates 
        # on the Shell 
        # print(x, ' ', y) 
        params[1].append((x, y))

  
        # displaying the coordinates 
        # on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(params[0], str(x) + ',' +
                    str(y), (x,y), font, 
                    1, (255, 0, 0), 2) 
        cv2.imshow("screen", params[0])

        if len(params[1]) == 2:
            cr_img = params[0][params[1][0][1]:params[1][1][1], params[1][0][0]:params[1][1][0]] # y-axis first for some reason
            cv2.destroyAllWindows()
            

def getScreenshot():
    screenshot = ImageGrab.grab()
    rect_coord = []
    # screenshot.show()

    cv_img = np.array(screenshot)
    cv_img = cv_img[:, :, ::-1].copy()

    cv2.namedWindow('screen')
    cv2.setMouseCallback('screen', click_event, [cv_img, rect_coord])

    cv2.imshow("screen", cv_img)
    while cv2.getWindowProperty('screen', cv2.WND_PROP_VISIBLE) > 0:

        if cv2.waitKey(0) == 27:
            cv2.destroyAllWindows()

    return cr_img
