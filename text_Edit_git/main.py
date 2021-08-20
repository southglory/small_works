# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    folder_dir = 'items/raw'
    file_list = os.listdir(folder_dir)
    for file_name in file_list:
        file_dir = folder_dir+'/'+file_name
        writer = []
        title = []
        paper = []
        with open(file_dir, encoding='utf-8') as file:
            a = file.readline()
            while a:
                print(a)
                idx1 = a.find('"')
                if idx1 == -1:
                    idx1 = a.find('“')
                str1 = a[:idx1-2]
                a2 = a[idx1+1:]
                idx2 = a2.find('"')
                if idx2 == -1:
                    idx2 = a2.find('”')
                str2 = a2[:idx2]
                str3 = a2[idx2+3:].replace('\n','')
                writer.append(str1)
                title.append(str2)
                paper.append(str3)
                a = file.readline()

        output = []
        num = 1
        for s1, s2, s3 in zip(title, paper, writer):
            # print(s1, s2, s3)
            output.append(str(num)+'\t'+s1+'\t'+s2+'\t'+s3+'\n')
            num+=1
        print(output)
        with open('items/parsed/parsed_'+file_name,'w', encoding='utf-8') as file:
            file.writelines(output)

