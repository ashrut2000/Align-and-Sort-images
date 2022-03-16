import cv2
import numpy as np
img=cv2.imread("qn.jpg") #reading image
cv2.imshow("original image",img) #displaying original image
#assigning the boundary coordinates of each image in a numpy array, from top left to bottom right respectively.
coordinates_1=np.float32([[238,235],[407,281],[228,280],[394,324]]) 
coordinates_2=np.float32([[536,268],[698,225],[557,342],[718,300]])
coordinates_3=np.float32([[190,541],[354,450],[228,604],[388,512]])
coordinates_4=np.float32([[587,456],[764,559],[524,568],[697,668]])
#calculating width and height of each rectangle as per the coordinate points
width_1 = int(np.linalg.norm(coordinates_1[0]-coordinates_1[1]))
height_1 = int(np.linalg.norm(coordinates_1[0] - coordinates_1[2]))
width_2 = int(np.linalg.norm(coordinates_2[0] - coordinates_2[1]))
height_2 = int(np.linalg.norm(coordinates_2[0] - coordinates_2[2]))
width_3 = int(np.linalg.norm(coordinates_3[0] - coordinates_3[1]))
height_3 = int(np.linalg.norm(coordinates_3[0] - coordinates_3[2]))
width_4 = int(np.linalg.norm(coordinates_4[0] - coordinates_4[1]))
height_4 = int(np.linalg.norm(coordinates_4[0] - coordinates_4[2]))
#coordinates of the image after transformation
coordinates_transform_1 = np.float32([[0, 0], [width_1, 0], [0, height_1], [width_1, height_1]])
coordinates_transform_2 = np.float32([[0, 0], [width_2, 0], [0, height_2], [width_2, height_2]])
coordinates_transform_3 = np.float32([[0, 0], [width_3, 0], [0, height_3], [width_3, height_3]])
coordinates_transform_4 = np.float32([[0, 0], [width_4, 0], [0, height_4], [width_4, height_4]])
#getperspective transform returns the transformation matrix for each case. 
matrix_1 = cv2.getPerspectiveTransform(coordinates_1, coordinates_transform_1)
matrix_2 = cv2.getPerspectiveTransform(coordinates_2, coordinates_transform_2)
matrix_3 = cv2.getPerspectiveTransform(coordinates_3, coordinates_transform_3)
matrix_4 = cv2.getPerspectiveTransform(coordinates_4, coordinates_transform_4)
#function that applies the perspective transformation to each image
output_1 = cv2.warpPerspective(img, matrix_1, (width_1, height_1))
output_2 = cv2.warpPerspective(img, matrix_2, (width_2, height_2))
output_3 = cv2.warpPerspective(img, matrix_3, (width_3, height_3))
output_4 = cv2.warpPerspective(img, matrix_4, (width_4, height_4))
cv2.imshow("aligned image 1", output_1)
cv2.imshow("aligned image 2", output_2)
cv2.imshow("aligned image 3", output_3)
cv2.imshow("aligned image 4", output_4)
cv2.waitKey(0)