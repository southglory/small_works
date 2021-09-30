import os, shutil

dir_path = os.getcwd()
file_list = os.listdir(dir_path)
file_list.remove('fire.exe')
print(file_list)
for file in file_list:
    file_path = os.path.join(dir_path, file)
    if os.path.isdir(file_path):
        dir_path2 =file_path
        print(dir_path2)
        shutil.rmtree(dir_path2)
        ash_path = os.path.join(dir_path, file + '_ASH')
        os.mkdir(ash_path)
    else:

        name, ext = os.path.splitext(file)
        ash_path = os.path.join(dir_path, name+'_ASH' + ext)
        f = open(ash_path, 'w')
        f.close()
        os.remove(file_path)