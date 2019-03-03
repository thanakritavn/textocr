import cv2
import numpy as np
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image


# Path of working folder on Disk
src_path = "C:/Users/quizd/Desktop/python/"
# rc_path = "E:/Lab/Python/Project/OCR/"
def get_string(img_path):
    print ("image path {}".format(img_path))
    # Read image with opencv
    img = cv2.imread(img_path)
    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    noisePath = img_path + "removed_noise.png"
    print ("noisePath: {}".format(noisePath))
    cv2.imwrite(noisePath,img)

    #  Apply threshold to get image with only black and white
    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    thresPath = img_path + "thres.png"
    print( "thresPath : {}".format(thresPath) )
    cv2.imwrite(thresPath, img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(img_path + "thres.png"))

    # Remove template file
    #os.remove(temp)

    return result

output = get_string(src_path +"tst5.png")

print ('--- Start recognize text from image ---')
print (output)

print ("------ Done -------")