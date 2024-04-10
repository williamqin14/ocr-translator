# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from PIL import ImageGrab
import cv2
import numpy as np

cr_img = None
window_visible = True

def click_event(event, x, y, flags, params):
    global cr_img
    global window_visible

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
            window_visible = False
            print('window is false')
            cv2.destroyAllWindows()



def getScreenshot():
    global window_visible
    screenshot = ImageGrab.grab()
    rect_coord = []
    # screenshot.show()

    cv_img = np.array(screenshot)
    # cv_img = cv_img[:, :, ::-1].copy()
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY) # convert to grayscale to deal with crossplatform issues

    cv2.namedWindow('screen') # cv creates an empty window
    cv2.setMouseCallback('screen', click_event, [cv_img, rect_coord])
    cv2.imshow("screen", cv_img) # cv displays image in window
    cv2.waitKey(1000) # needed for sync

    while window_visible:
        if cv2.waitKey(1) == 27:
            break

    window_visible = True

    cv2.destroyAllWindows()

    print('screenshot successful')
    # print(cr_img)
    cv2.imwrite('output.png', cr_img)
