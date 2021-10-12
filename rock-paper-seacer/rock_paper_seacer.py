import random

import cv2
import hand_detector as hd
"""
vedio_capture = cv2.VideoCapture(0)

#we need only right hand to playing
hand_detector = hd.hand_detector(max_hands=1)
tip_ids = [4, 8, 12, 16, 20]

while -1:
    _, img = vedio_capture.read()
    
    # Draw the hand landmark.
    img = hand_detector.detect_hand(img, draw_points=False)
    # Get the 20 landmark points as a array.
    hand_array = hand_detector.get_landmark_array(img,draw_tip=True)
    # draw the rectangle line.
    if len(hand_array) != 0:
        hand_img = hand_detector.draw_rectangle_hand(img, hand_array,crop_hand=True)
        h,w, c = hand_img.shape
        img[0:h, 0:w] = hand_img
    cv2.imshow("Hand Tracked image", img)

#     if len(hand_array) != 0 :
#         # generate the list of open fingers.
#         open_fingers = []

#         # check tump is open or not.
#         print(hand_array)
#         if hand_array[tip_ids[0]][1] < hand_array[tip_ids[0] - 1][1]:
#             open_fingers.append(0)
#         else: open_fingers.append(1)

#         # other 4 fingers.
#         for id in range(1,5):
#             if hand_array[tip_ids[id]][2] > hand_array[tip_ids[id] - 2][2]:
#                 open_fingers.append(0)
#             else: open_fingers.append(1)

#         print(open_fingers)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    

vedio_capture.release()
cv2.destroyAllWindows()




"""

#get the basic info
folder_name = ['rock', 'paper', 'scissors']
folder_number = int(input("Enter the folder number/image class number 0)rock 1)paper 2)scissors"))
num_images = int(input("Enter the number of images needed for each class"))

#we need only right hand to playing
hand_detector = hd.hand_detector(max_hands=1)

video_capture = cv2.VideoCapture(0)
folder_path = "/home/pavithra/learning/projects/rock-paper-seacer/dataset/{folder_name}/".format(folder_name=folder_name[folder_number])
img_count = 1
while 1:
    ret, img = video_capture.read()

    # Draw the hand landmark.
    img = hand_detector.detect_hand(img, draw_points=False)
    # Get the 20 landmark points as a array.
    hand_array = hand_detector.get_landmark_array(img,draw_tip=False)
    if len(hand_array) != 0:
        #get the cropeed hand image.
        hand_img = hand_detector.draw_rectangle_hand(img, hand_array,crop_hand=True)
        img_path = folder_path + folder_name[folder_number] + '_' + str(img_count) + '.jpg'
        # print(img_path)
        cv2.imwrite(img_path, hand_img)
        img_count += 1
    cv2.imshow("Live screen", img)
    

    if (img_count == num_images) or (cv2.waitKey(1) & 0xFF == ord('q')):
        break

video_capture.release()
cv2.destroyAllWindows()