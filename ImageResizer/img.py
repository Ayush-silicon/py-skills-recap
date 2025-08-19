# write a Python script to resize images using open cv2 and PIL
import cv2

#Configurable Parameters

scale_percent = 50  # percent of original size
source_image_path = 'Ash.jpg'  # path to the source image
destination_image_path = 'Ash_resized.png'  # path to save the resized image    

src = cv2.imread('Ash.jpg', cv2.IMREAD_UNCHANGED)

n_width = int(src.shape[1] * scale_percent / 100)     
n_height = int(src.shape[0] * scale_percent / 100)

# resize image
resized = cv2.resize(src, (n_width, n_height) )

#cv2.imshow('Resized Image', resized)
cv2.imwrite('Ash_resized.jpg', resized)
cv2.waitKey(0)

