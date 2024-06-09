import cv2
import numpy as np

name_of_img_raw = input("Enter the filename for conversion along with the format, e.g., .jpg: ")
img_raw = cv2.imread(name_of_img_raw)

h = int(input("Required height of the image: "))
w = int(input("Required width of the image: "))

p1_a, p1_b = (input("Coordinates of the top left corner, separated by a comma: ")).split(",")
p2_a, p2_b = (input("Coordinates of the bottom left corner, separated by a comma: ")).split(",")
p3_a, p3_b = (input("Coordinates of the top right corner, separated by a comma: ")).split(",")
p4_a, p4_b = (input("Coordinates of the bottom right corner, separated by a comma: ")).split(",")

print("ГОТОВЧЕНКО! Можеш закрити програму або натиснути ENTER")
print("DONE! You can close the program or press ENTER")
input()

pos1 = np.float32([[p1_a,p1_b],[p2_a,p2_b],[p3_a,p3_b],[p4_a,p4_b]])
pos2 =np.float32([[0,0],[w,0],[0,h],[w,h]])

matrix = cv2.getPerspectiveTransform(pos1, pos2)

img_mod = cv2.warpPerspective(img_raw, matrix, (w,h))

cv2.imwrite("Modified image.jpg", img_mod)