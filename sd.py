# coding: utf-8
import os


# 将file_dir目录下的old_type类型的文件改成new_type类型的文件
def file_rename(old_type, new_type, file_dir):
    old_files = find_file(old_type, file_dir)
    for old_file in old_files:  # 遍历所有文件
        filename = os.path.splitext(old_file)[0]  # 文件名
        # filetype=os.path.splitext(old_file)[1]#文件扩展名
        new_file = os.path.join(filename + new_type)  # 新的文件路径
        os.rename(old_file, new_file)  # 重命名
        print("1")


# 找某个文件类型的文件
def find_file(file_type, file_dir):
    file_set = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == file_type:
                file_set.append(os.path.join(root, file))

    return file_set

if __name__ == '__main__':
    # 下面是需要修改的代码
    file_dir = r"C:\Users\way\Desktop\ss"
    with open("./tt.txt", 'r', encoding='utf-8') as f:
        i = f.readline()
        print(i)
        file_rename('.pdf', 'i.pdf', file_dir)


