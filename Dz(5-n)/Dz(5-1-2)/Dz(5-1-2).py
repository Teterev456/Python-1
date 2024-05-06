import os
import datetime

fileName = input("Введите название файла: ")
now_date = datetime.date.today()
dir_main = os.getcwd()
os.mkdir(f"{now_date}")
file = open(f"{fileName}.txt", 'w+')
file.close()
os.rename(f"{dir_main}/{fileName}.txt", f"{dir_main}/{now_date}/{fileName}.txt")
os.mkdir(f"{dir_main}/{now_date}/dir_2")
os.rename(f"{dir_main}/{now_date}/{fileName}.txt", f"{dir_main}/{now_date}/dir_2/{fileName}.txt")
