import os
import csv


def make_csv(data, new_csv_path):
    with open(new_csv_path, 'a', encoding='utf-8-sig', newline='') as new_csv:
        write_csv = csv.writer(new_csv)
        write_csv.writerow(data)
    new_csv.close()


def read_submission_csv(tmp_list, csv_path):
    with open(csv_path, 'r', encoding='utf-8-sig') as read_csv:
        read = csv.reader(read_csv)
        for i in read:
            tmp_list.append(i[1])
        return tmp_list


def save_similarity_csv(data, new_csv_path):
    with open(new_csv_path, 'a', encoding='utf-8-sig', newline='') as new_csv:
        write_csv = csv.writer(new_csv)
        write_csv.writerow(data)
    new_csv.close()


def load_img_path(img_path, url):
    try:
        file_list = os.listdir(img_path + url)
        # for i in file_list:
        #     if i[-3:-1] != 'jpg':
        #         file_list.remove(i)
        # print("get img file name", file_list)
        return file_list
    except FileNotFoundError:
        # print("Get_img_path : FileNotFoundError")
        return "0"


