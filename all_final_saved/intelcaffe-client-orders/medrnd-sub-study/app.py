import os
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from datetime import datetime
from shutil import copyfile

'''
Category Mapping:
 RIPC == Generic Count
 Sham == Controlled Count
 
'''

PROJECT_ROOT = os.path.dirname (os.path.realpath (__file__))

app = Flask (__name__)
CORS (app)


class Todo (object):
    def __init__(self, name: str, controlled: int, generic: int):
        self.name = name
        self.controlled = controlled
        self.generic = generic


# Utility
def ConvertListToDict(a):
    it = iter (a)
    res_dct = dict (zip (it, it))
    return res_dct


def replace_line(file_name, line_num, text):
    lines = open (file_name, 'r').readlines ()
    lines[line_num] = text
    out = open (file_name, 'w')
    out.writelines (lines)
    out.close ()


def get_todolist():
    # getting all db data - stat
    with open ('total_count.txt') as f:
        content = f.readlines ()
    content = [line.split ('\n')[0] for line in content]

    ## GET PREV STAT
    total_patient = int (content[5].split (' ')[1])
    # print (total_patient)

    controlled_HFrEF = int (content[1].split (' ')[1])
    controlled_CKD = int (content[2].split (' ')[1])
    controlled_ANEMIA = int (content[3].split (' ')[1])
    controlled_DM = int (content[4].split (' ')[1])
    controlled_MALE = int (content[6].split (' ')[1])
    controlled_White = int (content[7].split (' ')[1])

    generic_HFrEF = int (content[1].split (' ')[2])
    generic_CKD = int (content[2].split (' ')[2])
    generic_ANEMIA = int (content[3].split (' ')[2])
    generic_DM = int (content[4].split (' ')[2])
    generic_MALE = int (content[6].split (' ')[2])
    generic_White = int (content[7].split (' ')[2])

    HFrEF_data = Todo (name='HFrEF', controlled=controlled_HFrEF, generic=generic_HFrEF)
    CKD_data = Todo (name='CKD', controlled=controlled_CKD, generic=generic_CKD)
    ANEMIA_data = Todo (name='ANEMIA', controlled=controlled_ANEMIA, generic=generic_ANEMIA)
    DM_data = Todo (name='DM', controlled=controlled_DM, generic=generic_DM)
    MALE_data = Todo (name='MALE', controlled=controlled_MALE, generic=generic_MALE)
    White_data = Todo (name='White People', controlled=controlled_White, generic=generic_White)

    todo_list = [HFrEF_data, CKD_data, ANEMIA_data, DM_data, MALE_data, White_data]
    return todo_list, total_patient


@app.route ("/delete/", methods=["GET", "POST"])
def delete():
    with open ('total_count.txt') as f:
        content = f.readlines ()

    ## some vars
    total_patient = int (content[5].split (' ')[1])
    time_stamp = datetime.now ()

    ## GET PREV STAT
    controlled_HFrEF = int (content[1].split (' ')[1])
    controlled_CKD = int (content[2].split (' ')[1])
    controlled_ANEMIA = int (content[3].split (' ')[1])
    controlled_DM = int (content[4].split (' ')[1])
    controlled_MALE = int (content[6].split (' ')[1])
    controlled_White = int (content[7].split (' ')[1])

    generic_HFrEF = int (content[1].split (' ')[2])
    generic_CKD = int (content[2].split (' ')[2])
    generic_ANEMIA = int (content[3].split (' ')[2])
    generic_DM = int (content[4].split (' ')[2])
    generic_MALE = int (content[6].split (' ')[2])
    generic_White = int (content[7].split (' ')[2])

    ## del
    last_record = 'no-data'
    content_record = []
    with open ('record.txt') as f2:
        content_record = f2.readlines ()
    if len (content_record) > 0:
        last_record = content_record[-1].strip ('\n').replace (':', '').split (' ')
    else:
        todo_list, total_patient = get_todolist ()
        return render_template ("index.html", total_patient=total_patient, todo_list=todo_list, category_list=[])

    last_record = last_record[2:]
    last_record_map = ConvertListToDict (last_record)

    if 'category' not in last_record_map:
        todo_list, total_patient = get_todolist ()
        return render_template ("index.html", total_patient=total_patient, todo_list=todo_list, category_list=[])

    print (last_record_map)

    if last_record_map['category'] == 'RIPC':
        generic_DM = generic_DM - int (last_record_map['DM'])
        generic_HFrEF = generic_HFrEF - int (last_record_map['HFrEF'])
        generic_CKD = generic_CKD - int (last_record_map['CKD'])
        generic_ANEMIA = generic_ANEMIA - int (last_record_map['ANEMIA'])
        generic_MALE = generic_MALE - int (last_record_map.get ('MALE', 0))
        generic_White = generic_White - int (last_record_map.get ('White', 0))

    elif last_record_map['category'] == 'Sham':
        controlled_DM = controlled_DM - int (last_record_map['DM'])
        controlled_HFrEF = controlled_HFrEF - int (last_record_map['HFrEF'])
        controlled_CKD = controlled_CKD - int (last_record_map['CKD'])
        controlled_ANEMIA = controlled_ANEMIA - int (last_record_map['ANEMIA'])
        controlled_MALE = controlled_MALE - int (last_record_map.get ('MALE', 0))
        controlled_White = controlled_White - int (last_record_map.get ('White', 0))

    # return str(last_record_map), 200
    # write
    replace_line (file_name='total_count.txt', line_num=1, text='HFrEF ' + str (controlled_HFrEF) + ' ' + str (generic_HFrEF) + '\n')
    replace_line (file_name='total_count.txt', line_num=2, text='CKD ' + str (controlled_CKD) + ' ' + str (generic_CKD) + '\n')
    replace_line (file_name='total_count.txt', line_num=3, text='ANEMIA ' + str (controlled_ANEMIA) + ' ' + str (generic_ANEMIA) + '\n')
    replace_line (file_name='total_count.txt', line_num=4, text='DM ' + str (controlled_DM) + ' ' + str (generic_DM) + '\n')
    total_patient -= 1
    replace_line (file_name='total_count.txt', line_num=5, text='total_patient ' + str (total_patient) + '\n')
    replace_line (file_name='total_count.txt', line_num=6, text='MALE ' + str (controlled_MALE) + ' ' + str (generic_MALE) + '\n')
    replace_line (file_name='total_count.txt', line_num=7, text='White ' + str (controlled_White) + ' ' + str (generic_White) + '\n')

    copyfile ('record.txt', 'record_saved.txt')

    open ("record.txt", "w").close ()  # deleting old content

    for line in content_record[:-1]:
        print (line.strip ('\n'), file=open ('record.txt', 'a'))

    todo_list, total_patient = get_todolist ()
    return render_template ("delete.html", total_patient=total_patient, todo_list=todo_list, category_list=[])


@app.route ("/", methods=["GET", "POST"])
def add():
    HFrEF = request.form.get ("HFrEF")
    CKD = request.form.get ("CKD")
    ANEMIA = request.form.get ("ANEMIA")
    DM = request.form.get ("DM")
    MALE = request.form.get ("MALE")
    White = request.form.get ("White")

    if MALE == 'MALE':
        MALE = 1
    else:
        MALE = 0

    if White == 'White':
        White = 1
    else:
        White = 0

    if HFrEF == 'HFrEF':
        HFrEF = 1
    else:
        HFrEF = 0

    if CKD == 'CKD':
        CKD = 1
    else:
        CKD = 0

    if ANEMIA == 'ANEMIA':
        ANEMIA = 1
    else:
        ANEMIA = 0

    if DM == 'DM':
        DM = 1
    else:
        DM = 0

    # print (DM, ANEMIA, CKD, HFrEF, MALE, White)

    if DM == 0 and ANEMIA == 0 and CKD == 0 and HFrEF == 0 and MALE == 0 and White == 0:
        todo_list, total_patient = get_todolist ()
        return render_template ("index.html", total_patient=total_patient, todo_list=todo_list, category_list=[])

    with open ('total_count.txt') as f:
        content = f.readlines ()

    ## some vars
    total_patient = int (content[5].split (' ')[1])
    time_stamp = datetime.now ()

    ## GET PREV STAT
    controlled_HFrEF = int (content[1].split (' ')[1])
    controlled_CKD = int (content[2].split (' ')[1])
    controlled_ANEMIA = int (content[3].split (' ')[1])
    controlled_DM = int (content[4].split (' ')[1])
    controlled_MALE = int (content[6].split (' ')[1])
    controlled_White = int (content[7].split (' ')[1])

    generic_HFrEF = int (content[1].split (' ')[2])
    generic_CKD = int (content[2].split (' ')[2])
    generic_ANEMIA = int (content[3].split (' ')[2])
    generic_DM = int (content[4].split (' ')[2])
    generic_MALE = int (content[6].split (' ')[2])
    generic_White = int (content[7].split (' ')[2])

    ########################

    total_diff_if_controlled = 0  # total_diff_if_controlled for new patient
    # if medicine applied , calc diff
    if HFrEF:
        total_diff_if_controlled += 1 + controlled_HFrEF - generic_HFrEF

    if CKD:
        total_diff_if_controlled += 1 + controlled_CKD - generic_CKD

    if ANEMIA:
        total_diff_if_controlled += 1 + controlled_ANEMIA - generic_ANEMIA

    if DM:
        total_diff_if_controlled += 1 + controlled_DM - generic_DM

    if MALE:
        total_diff_if_controlled += 1 + controlled_MALE - generic_MALE

    if White:
        total_diff_if_controlled += 1 + controlled_White - generic_White

    ########################

    total_diff_if_generic = 0  # total_diff_if_controlled for new patient
    # if medicine applied , calc diff
    if HFrEF:
        total_diff_if_generic += 1 - controlled_HFrEF + generic_HFrEF

    if CKD:
        total_diff_if_generic += 1 - controlled_CKD + generic_CKD

    if ANEMIA:
        total_diff_if_generic += 1 - controlled_ANEMIA + generic_ANEMIA

    if DM:
        total_diff_if_generic += 1 - controlled_DM + generic_DM

    if MALE:
        total_diff_if_generic += 1 - controlled_MALE + generic_MALE

    if White:
        total_diff_if_generic += 1 - controlled_White + generic_White

    category = 'none'

    if total_diff_if_controlled <= total_diff_if_generic:
        category = 'Sham'

        if HFrEF:
            controlled_HFrEF += 1

        if CKD:
            controlled_CKD += 1

        if ANEMIA:
            controlled_ANEMIA += 1

        if DM:
            controlled_DM += 1

        if MALE:
            controlled_MALE += 1

        if White:
            controlled_White += 1

    else:
        category = 'RIPC'

        if HFrEF:
            generic_HFrEF += 1

        if CKD:
            generic_CKD += 1

        if ANEMIA:
            generic_ANEMIA += 1

        if DM:
            generic_DM += 1

        if MALE:
            generic_MALE += 1

        if White:
            generic_White += 1

    # write
    replace_line (file_name='total_count.txt', line_num=1, text='HFrEF ' + str (controlled_HFrEF) + ' ' + str (generic_HFrEF) + '\n')
    replace_line (file_name='total_count.txt', line_num=2, text='CKD ' + str (controlled_CKD) + ' ' + str (generic_CKD) + '\n')
    replace_line (file_name='total_count.txt', line_num=3, text='ANEMIA ' + str (controlled_ANEMIA) + ' ' + str (generic_ANEMIA) + '\n')
    replace_line (file_name='total_count.txt', line_num=4, text='DM ' + str (controlled_DM) + ' ' + str (generic_DM) + '\n')
    total_patient += 1
    replace_line (file_name='total_count.txt', line_num=5, text='total_patient ' + str (total_patient) + '\n')
    replace_line (file_name='total_count.txt', line_num=6, text='MALE ' + str (controlled_MALE) + ' ' + str (generic_MALE) + '\n')
    replace_line (file_name='total_count.txt', line_num=7, text='White ' + str (controlled_White) + ' ' + str (generic_White) + '\n')

    decision_category = category

    print (str (time_stamp), 'HFrEF: ' + str (HFrEF), \
           'CKD: ' + str (CKD), \
           'ANEMIA: ' + str (ANEMIA), \
           'DM: ' + str (DM), \
           'category: ' + category, \
           'MALE: ' + str (MALE), \
           'White: ' + str (White), \
           file=open ('record.txt', 'a'))

    todo_list, total_patient = get_todolist ()
    category_list = [category]
    return render_template ("index.html", total_patient=total_patient, todo_list=todo_list, category_list=category_list)


if __name__ == "__main__":
    # open ("record.txt", "w").close ()
    # open ("total_count.txt", "w").close ()
    # copyfile ('clean_db.txt', 'total_count.txt')
    app.run (host='127.0.0.1', port=8693, debug=True)
