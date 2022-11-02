import importlib
import os
import sys
import pandas as pd
import shutil
import hmac
import hashlib, os
import random, string


file_path = None


class GenericFileHelper:
    # file related
    @classmethod
    def create_file(cls, file_path):
        f = open (file_path, 'a+')
        f.close ()

    @classmethod
    def remove_file(cls, file_path):
        if os.path.exists (file_path):
            os.remove (file_path)

    @classmethod
    def read_file_lines(cls, file_path):
        with open (file_path) as f:
            lines = f.readlines ()
        return lines

    @classmethod
    def append_file(cls, file_path, lines_to_append=[], append_beginning_of_file=True):
        with open (file_path, 'r') as f:
            old_lines = f.readlines ()
        for new_line in lines_to_append:
            flag = True
            for old_line in old_lines:
                if new_line in old_line:
                    flag = False
                    break

            if flag:
                if append_beginning_of_file:
                    old_lines.insert (0, new_line)
                else:
                    old_lines.append (new_line)

        a_file = open (file_path, "w")
        a_file.writelines (old_lines)
        a_file.close ()

    @classmethod
    def large_text_file_reader(file_name):
        try:
            for _line in open (file_name, "r"):
                yield _line.strip ()
        except Exception as e:
            print (e, file=open ('log_large_text_file_reader.txt', 'a'))
            yield (f'error')


class GenericTextProcessing:
    pass


class GenericDictHelper:
    @classmethod
    def get_all_key_value(cls, dictionary: dict):
        ls = []
        for key, value in dictionary.items ():
            ls.append ((key, value))
        return ls


class GenericETLHelper:
    @classmethod
    def collect_columns_from_tsv_or_csv_file(cls, file_path='a.tsv', input_column_separator="\t", colms_to_colllect=[0, 2]):
        '''For csv use coma'''
        dataset = pd.read_csv (file_path, sep=input_column_separator)
        df = pd.DataFrame (dataset)
        df = df[df.columns[colms_to_colllect]]
        ls = df.values.tolist ()
        return ls


class GenericPythonHelper:
    @classmethod
    def format_pyhton_file(cls, file_path):
        os.system (f'autopep8 -i {file_path} ')

    @classmethod
    def import_module_from_file(cls, file_path='django_prepare_project_0.8.py', module_name='django_prepare_project'):
        # After calling this f() Use module in code like ==>  from django_prepare_project import DebugHelper
        spec = importlib.util.spec_from_file_location (module_name, file_path)
        module = importlib.util.module_from_spec (spec)
        spec.loader.exec_module (module)
        sys.modules[module_name] = module


def statistics_of_data_collection(gender='all', age_group='all', rootdir='collected_wavs'):
    '''
    Use like statistics_of_data_collection(gender='F', age_group='01') etc. to get different statistics of collected data.
    :param gender: 'all' for both, else M/F (male/female).
    :param age_group: 'all' for all age group. Age group:code map: 0-15: 01, 15-25: 02, 25-35: 03, 35-45: 04, 45-100: 05
    :return: prints stats
    '''
    L = []
    total = 0
    for folder in os.listdir(rootdir):
        d = os.path.join(rootdir, folder)
        if os.path.isdir(d):
            if age_group == folder[5:] or age_group == 'all':
                if gender == folder[0] or gender == 'all':
                    L.append((folder, len([name for name in os.listdir(d)])))

    # print("Stat for Gender:", gender, " and Age_group: ", age_group, " (sorted in ascending format)\n")

    L.sort(key=lambda x: x[1])
    # for elem in L:
    #     print(elem[0], elem[1])
    #     total += elem[1]
    # print("\nTotal: ", total)
    return L


def get_text_meta_data(asr_text_data_path):
    texts_map = {}
    all_textlineIDs = []
    with open(asr_text_data_path) as f:
        all_textlineIDs_text = f.readlines()

    for x in all_textlineIDs_text:
        split_line = x.strip().split(' ', 1)
        line_ID, lineText = split_line[0], split_line[1]
        texts_map[line_ID] = lineText
        all_textlineIDs.append(line_ID)

    return all_textlineIDs, texts_map


def create_sha256_signature(key, message):
    byte_key = bytes(key, 'UTF-8')
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest()


def json_field_validation(json_dict, expected_keys=[]):
    if all(key in json_dict for key in expected_keys):
        return True
    else:
        return False


def get_unique_random_ID(key=24):
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=key))
    return x


def random_line(afile):
    lines = open(afile).read().splitlines()
    return random.choice(lines)


def add_new_text(textFilePath, startIndex, outputNewTextFile):
    '''
    textFilePath contains new lines. Each line contains one new line.
    :param textFilePath:
    :param startIndex:
    :return:
    '''
    with open(textFilePath) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    for idx, x in enumerate(content, start=startIndex):
        # txt = x.split(' ', 1)
        print('1' + str(idx).zfill(7), x.strip(), outputNewTextFile)
