import pytesseract as pt
import cv2
from PIL import Image
import numpy as np
import re
def getDataFromImg(fileName):
    pt.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    file = '../uploadedImages/' + fileName
    img = np.array(Image.open(file))

    all_courses = []

    fname = "Revanth"
    lname = "Senthil"
    email = "senthilr@purdue.edu"

    def show_img(image):
        cv2.imshow('image', image)
        cv2.waitKey()

    def get_filtered_image(image):
        norm_img = np.zeros((image.shape[0], image.shape[1]))
        image = cv2.normalize(image, norm_img, 0, 255, cv2.NORM_MINMAX)
        image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)[1]
        image = cv2.GaussianBlur(image, (1, 1), 0)

        return image

    def resized(image, percent):
        wid = int(image.shape[1] * percent / 100)
        hei = int(image.shape[0] * percent / 100)

        return cv2.resize(image, (wid, hei))

    def box_detect(img):

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        thresh_inv = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

        # Blur the image
        blur = cv2.GaussianBlur(thresh_inv,(1,1),0)

        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

        # find contours
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        mask = np.ones(img.shape[:2], dtype="uint8") * 255
        for c in contours:
            # get the bounding rect
            x, y, w, h = cv2.boundingRect(c)
            if w*h>1000:
                cv2.rectangle(mask, (x, y), (x+w, y+h), (0, 0, 255), -1)

        res_final = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

        cv2.imshow("boxes", mask)
        cv2.imshow("final image", res_final)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def vertical_lines(image):
        img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        img_thr = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 128, 255, cv2.THRESH_BINARY_INV)[1]

        thr_y = 50
        y_sum = np.count_nonzero(img_thr, axis=0)
        peaks = np.where(y_sum > thr_y)[0]

        thr_x = 100
        temp = np.diff(peaks).squeeze()
        idx = np.where(temp > thr_x)[0]
        peaks = np.concatenate(([0], peaks[idx+1]), axis=0) + 1

        for i in np.arange(peaks.shape[0] - 1):
            cv2.imwrite('../assets/output/sub_image_' + str(i) + '.png', img[:, peaks[i]:peaks[i+1]])
        
        return (i + 1)


    def extract_info(text):
        # Initialize lists to store extracted information
        courses = []
        unique_ids = []
        class_times = []
        # locations = []
        
        # Use regex to find course information
        course_pattern = r'[A-Z]{2,4} \d{5}-\d{3}'
        course_matches = re.finditer(course_pattern, text)
        for match in course_matches:
            courses.append(match.group())
            
        # Use regex to find unique ID information
        unique_id_pattern = r'\d{5} Class'
        unique_id_matches = re.finditer(unique_id_pattern, text)
        for match in unique_id_matches:
            unique_ids.append(match.group())
            
        # Use regex to find class time and location information
        class_time_pattern = r'\d{,2}[:\-;]*\d{,2} *[ap]m-\d{1,2}:\d{2} [ap]m'
        # location_pattern = r'[A-Z]{1,5} \d{1,4}'
        class_time_matches = re.finditer(class_time_pattern, text)
        # location_matches = re.finditer(location_pattern, text)
        for class_time in class_time_matches:
            class_times.append(class_time.group())
            # locations.append(location.group())
            
        # return courses, unique_ids, class_times
        return unique_ids


    text = ""

    divi = 5

    shape = list(np.shape(img))
    X = shape[0] // divi
    Y = shape[1] // divi
    x_val = 0
    di = 0

    x_lim = X

    # for d in range(0, divi):
        # x_val = 0


    filtered = get_filtered_image(img)
    filtered = resized(filtered, 70)
    # show_img(filtered)
    # box_detect(filtered)
    total = vertical_lines(filtered)


    # text_outs = []
    uniq = []

    for out in range(total):
        text = pt.image_to_string(get_filtered_image(cv2.imread(f'../assets/sub_image_{out}.png')))

        # text_outs.append(extract_info(text))
        for val in extract_info(text):
            if val not in uniq:
                uniq.append(val)

    student =   {
        'fname' : fname, 'lname' : lname, 
        'email' : email, 
        'classes' : [{'classnum' : x.split()[0], 'needBuddy' : 'False'} for x in uniq]
                }
    return student
# with open('app.json', 'w') as f:
#     json.dump({"students":arrayData}, f)


"""
while x_lim < shape[0]:
    sub_img = img[x_val : x_lim, :]

    sub_img = get_filtered_img(sub_img)
    show_img(sub_img)

    text += pt.image_to_string(sub_img)

    x_val += X // 10
    x_lim += X // 10
    
"""


# print(np.shape(img))

# cv2.imshow('1', img)


# cv2.waitKey()


# file = 'assets/schedule_2.png'

# img = cv2.imread(file, 0)
# thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)[1]

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# result = 255 - opening
# cv2.imshow('thresh', thresh)
# cv2.imshow('opening', opening)
# cv2.imshow('result', result)

# text = pt.image_to_string(result)

# cv2.waitKey()