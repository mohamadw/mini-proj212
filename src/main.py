

from PIL import Image
from folder_file_functions import _make_dir
from pytesseract import pytesseract
from pdf2image import convert_from_path
from preproccessing_image import analyze_image
import os
import io

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
# Defining paths to tesseract.exe
# and the image we would be
#convert pdf files in the inputfiles dir to images in outputfiles
def pdf_to_images(_poppler_path):

    inputfiles_path = r"C:\Users\moham\PycharmProjects\pythonProject\inputfiles"
    Coverted_Files_path = r"C:\Users\moham\PycharmProjects\pythonProject\Coverted_Files"

    files = os.listdir(inputfiles_path)

    #for every inputfile (pdf)
    for f in files:
        # the path of pdf file withou
        pdf_file_path =   os.path.join(inputfiles_path,f )

        # the path of output folder that we want ot created for this file
        output_folder_path = os.path.join(Coverted_Files_path,f[:-4] ) #-4 to delete the ".pdf" from name that we want to create
        _make_dir(output_folder_path)

        images = convert_from_path(pdf_path=pdf_file_path,
                               poppler_path=_poppler_path)

        for i in range(len(images)):
            # Save the converted pages as images in the output folder
            output_omage_name = 'page' + str(i) + '.jpg'
            images[i].save(os.path.join(output_folder_path,output_omage_name ), 'JPEG')

def extract_text_from_images():
    Coverted_Files_path = r"C:\Users\moham\PycharmProjects\pythonProject\Coverted_Files"
    OutputFiles_path = r"C:\Users\moham\PycharmProjects\pythonProject\OutputFiles"
    _make_dir(OutputFiles_path)

    folders_converted = os.listdir(Coverted_Files_path)

    for dir in folders_converted:
        dir_path =os.path.join(Coverted_Files_path,dir )

        output_filename = os.path.join(OutputFiles_path,dir )


        images = os.listdir(dir_path)

        for image in images:
            analyze_image(os.path.join(dir_path,image ), output_filename , image)



#
# def extract_text_from_image(image_path,output_path):
#
#     path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
# # Opening the image & storing it in an image object
#     img = Image.open(image_path)
#
# # Providing the tesseract executable
# # location to pytesseract library
#     pytesseract.tesseract_cmd = path_to_tesseract
#
# # Passing the image object to image_to_string() function
# # This function will extract the text from the image
#
#     text = pytesseract.image_to_string(img, lang="heb")
#
#
#     file = io.open(output_path+".txt", "a", encoding="utf-8")
#     file.write(text[:-1])
#     file.close()
#



if __name__ == '__main__':

    _make_dir(r"C:\Users\moham\PycharmProjects\pythonProject\BoxesImages")

    poppler_path = r"C:\Users\moham\Downloads\Release-21.03.0\poppler-21.03.0\Library\bin"
    pdf_to_images(poppler_path)
    extract_text_from_images()




