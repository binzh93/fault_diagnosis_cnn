# -*- coding: utf-8 -*-
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image 


############################
# test and show the cropped image
############################
def pil_show_cropped_img(imgname, isCaseW=False):

    img = Image.open(imgname)  #open img
    plt.figure("time-frequence-figure")
    plt.subplot(1,2,1), plt.title('origin')
    plt.imshow(img),plt.axis('off')

    if isCaseW:
        box=(135,63,923,748)    # TODO   need change
    else:
        box=(135,63,923,748)
    roi=img.crop(box)

    plt.subplot(1,2,2), plt.title('center_cropped')
    plt.imshow(roi),plt.axis('off')
    plt.show()


############################
# double dir
############################
def pil_cropped_center_img(root_dir, save_dir, isCaseW=False):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for name in os.listdir(root_dir):
        if name == ".DS_Store":
            continue
        if not os.path.exists(os.path.join(save_dir, name)):
            os.mkdir(os.path.join(save_dir, name))
        img_dir = os.path.join(root_dir, name)
        for imgname in os.listdir(img_dir):
            if imgname == ".DS_Store":
                continue
            src = os.path.join(img_dir, imgname)
            dst = os.path.join(os.path.join(save_dir, name), imgname)
            img = Image.open(src)
            if isCaseW:
                box=(135,63,923,748)  # TODO  need change
            else:
                box=(135,63,923,748)
            roi=img.crop(box)
            roi.save(dst)

           


if __name__ == "__main__":
    isTest = False
    if isTest:
        imgname = "/Users/zhubin/Documents/githubfile/rolling_b_jiangnan/pic/ib_2500/ib_516.jpg"
        pil_show_cropped_img(imgname)
    else:
        isCaseW = False
        root_dir = "/Users/zhubin/Documents/githubfile/rolling_b_jiangnan/pic"
        save_dir = "jiangnan_data_2500/"
        pil_cropped_center_img(root_dir, save_dir, isCaseW)