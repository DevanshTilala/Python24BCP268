import shutil,os

if os.path.exists("C:\\Users\\lab\\Desktop\\24BCP268\\practice"):
    print("Path already exists")
else:
    os.mkdir('C:\\Users\\lab\\Desktop\\24BCP268\\practice')
    print("Made new directory")

shutil.copyfile('C:\\Users\\lab\\Desktop\\24BCP309 PYTHON SERIES\\ADD.py','C:\\Users\\lab\\Desktop\\24BCP268\\practice\\ADD.py')
