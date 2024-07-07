import cv2

# Load an image from file
image = cv2.imread(r'C:\Users\mayan\Downloads\Coding-Raja-Technologies-Internship-main\Coding-Raja-Technologies-Internship-main\misfit cover art.jpg')

# Apply Gaussian blur to the image
blurred_image = cv2.GaussianBlur(image, (31, 31), 0)

# Save the blurred image to a file
cv2.imwrite('blurred_image.jpg', blurred_image)

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()