import csv


import io

# the range of name in the image proccessing need to be :
# for the first column 387 -> 550
# the second column 985 ->1155
def Check_The_range_is_Name(box_left,box_Width):
    current_name_right = box_left + box_Width
    if box_left >= 387 and current_name_right <= 550 :    #check if in the first col
        return True
    if box_left >= 985 and current_name_right <= 1155:  #check if in the second col
        return True
    return False

# the range of previous_name in the image proccessing need to be :
# for the first column 174 -> 385
# the second column 780 ->970
def Check_The_range_is_PreviousName(box_left,box_Width):

    previous_name_right = box_left + box_Width
    if box_left >= 174 and previous_name_right <= 385:  # check if in the first col
        return True
    if box_left >= 780 and previous_name_right <= 970:  # check if in the second col
        return True
    return False

# where we need to print when we read the image
# for the first column 600->720
# the second column < 172

def Check_The_range_is_Print(box_left,box_Width):
    box_right = box_left + box_Width

    if box_left >= 600 and box_right <= 720:  # check if in the first col
        return True
    if box_right  < 172:  # check if in the second col
        return True
    return False


# the middle pixel is 700 left approximate
def analyze_lines(index,details,outputfile_path):
    name = ""
    prev_name = ""
    line = 0
    for i in range(index , len(details['text'])):
        box_left = details['left'][i]
        box_width = details['width'][i]
        box_text = details['text'][i]

        if line !=details['line_num'][i]:
            line = details['line_num'][i]
            name = ""
            prev_name = ""

        if Check_The_range_is_Print(box_left,box_width) and name !="" and prev_name !=" " :
            file = io.open(outputfile_path + ".txt", "a", encoding="utf-8")
            file.write(name + ' *** '+ prev_name + '\n')
            file.close()

            # reset
            name = ""
            prev_name = ""

        elif Check_The_range_is_Name(box_left,box_width):
            name = name +' ' +box_text

        elif Check_The_range_is_PreviousName(box_left, box_width):
            prev_name = prev_name + ' '+ box_text





def _extract_data_format(details , outputfile_path ):

    #details.keys() = dict_keys(['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text'])

    total_boxes = len(details['text'])
    i_box = 0
    line = -1
    for i_box in range(total_boxes):
           text= details['text'][i_box]
           if ((text =='הקודם') or (text == 'הקודס')):
                line = details['line_num'][i_box]
                break;

    i_box = 0
    for i_box in range(total_boxes):
        if line < details['line_num'][i_box]:
            analyze_lines(i_box+1, details, outputfile_path)
            return