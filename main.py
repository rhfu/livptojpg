# _*_ coding: utf-8 _*_
# _*_ author: anwenzen _*_

import os
import re
import sys
import shutil

if __name__ == "__main__":
    livpDir = "livp/"
    distDir = "dist/"
    if not os.path.isdir(distDir):
        os.mkdir(distDir)
    names = os.listdir(livpDir)
    for i in names:
        if not i.endswith('livp'):
            continue
        fileName = i.replace('.livp', '')
        zipFile = livpDir + fileName + '.zip'
        os.rename(livpDir + i, zipFile) # livp 重命名为 zip
        shutil.unpack_archive(zipFile, livpDir + fileName, "zip")
        jpgDir = livpDir + fileName + "/"
        jpgs = os.listdir(jpgDir)
        for j in jpgs:
            if j.endswith('jpg') or j.endswith('jpeg'):
                print("提取jpeg文件成功 - " + j)
                shutil.copy(jpgDir + "/" + j, distDir)
                shutil.rmtree(jpgDir)
                os.remove(zipFile)  # 删除zip文件
	