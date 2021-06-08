import os

import cv2
import pytesseract
from image_format import _extract_data_format
from pytesseract import Output


def analyze_image(image_path , outputfile_path,image_name):

    image = cv2.imread(image_path)
    # configuring parameters for tesseract
    custom_config = r'--oem 3 --psm 6'

    # now feeding image to tesseract
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract  # your path may be different

    details = pytesseract.image_to_data(image, output_type=Output.DICT, config=custom_config, lang='heb')

    total_boxes = len(details['text'])

    for sequence_number in range(total_boxes):

        if int(float(details['conf'][sequence_number])) > 30:

            (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number],details['height'][sequence_number])

            threshold_img = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


    _extract_data_format(details , outputfile_path)

    # save the image boxing in path
    path_to_save = r"C:\Users\moham\PycharmProjects\pythonProject\BoxesImages"
    cv2.imwrite(os.path.join(path_to_save, image_name) , threshold_img)





