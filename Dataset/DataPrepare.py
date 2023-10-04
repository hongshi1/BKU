import cv2
import numpy as np
from PIL import Image
import skimage
import os
import glob
import shutil
import pandas as pd


def get_file_name_without_extension(file_path):
    # file_name = os.path.basename(file_path)  # 获取文件名+扩展名
    file_name_without_extension = os.path.splitext(file_path)[0]  # 提取文件名（不包含扩展名）
    return file_name_without_extension


def get_file_base_name(file_path):
    file_name = os.path.basename(file_path)  # 获取文件名+扩展名
    return file_name


# 将图片添加高斯噪声n次
def adding_Gaussian_noise(path, new_path, time=5):
    origin = skimage.io.imread(path)
    shutil.copy2(path, new_path)
    new_path_without_ext = get_file_name_without_extension(new_path)
    for i in range(time):
        noisy = skimage.util.random_noise(origin, mode="gaussian", var=0.01)
        file_name = new_path_without_ext + "_" + str(i) + ".jpg"
        skimage.io.imsave(file_name, noisy, plugin="pil", check_contrast=False)


def find_xml_files(path):
    xml_files = glob.glob(path + "/*.xml")
    return xml_files


# 只需要找到对应的xml文件的图片就行
def filiter_picture():
    cor_path = "../Data/Part2/cor"
    sag_path = "../Data/Part2/sag"
    if not os.path.exists("../Data/cor"):
        os.mkdir("../Data/cor")
    if not os.path.exists("../Data/sag"):
        os.mkdir("../Data/sag")
    df = pd.read_excel("path/to/your/file.xlsx")
    ACC = df["ACC"]
    TAG = df["撞击（0-正常，1-混合，2-钳夹pincer，3-凸轮cam）"]
    for root, directories, files in os.walk(cor_path):
        print("当前目录:", root)
        folder_name = os.path.basename(root)
        folder_path = "../Data/cor/" + folder_name
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        xml_files = find_xml_files(root)
        # 遍历文件夹内的文件
        for xml in xml_files:
            name = get_file_base_name(xml)
            shutil.copy2(xml, folder_path + "/" + name)
            file_path = get_file_name_without_extension(xml) + ".jpg"
            file_name = os.path.basename(file_path)
            new_file_name = folder_path + "/" + file_name
            adding_Gaussian_noise(file_path, new_file_name, time=5)
            print(new_file_name)

    for root, directories, files in os.walk(sag_path):
        print("当前目录:", root)
        folder_name = os.path.basename(root)
        folder_path = "../Data/sag/" + folder_name
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        xml_files = find_xml_files(root)
        # 遍历文件夹内的文件
        for xml in xml_files:
            name = get_file_base_name(xml)
            shutil.copy2(xml, folder_path + "/" + name)
            file_path = get_file_name_without_extension(xml) + ".jpg"
            file_name = os.path.basename(file_path)
            new_file_name = folder_path + "/" + file_name
            adding_Gaussian_noise(file_path, new_file_name, time=5)
            print(new_file_name)


if __name__ == "__main__":
    filiter_picture()
