import os

path = r'D:\..Naruto Shippuden'
sub_path = r'D:\..Naruto Shippuden\finished watching\subs'
old_sub_list = []


for sub_name in os.listdir(sub_path):
    old_sub_list.append(sub_name)    


for file_name in os.listdir(path):
    # print(file_name)
    try:
        no = file_name.split('.')[1].split(' ')[0]
    except:
        pass
    new_sub = sub_path+"\\"+file_name.strip('mp4')+'ass'
    try:
        old_sub_loc = sub_path+"\\"+old_sub_list[int(no)]
    except:
        pass
    print(old_sub_loc, new_sub)
    try:
        os.rename(old_sub_loc, new_sub)
    except FileNotFoundError:
        pass
    except FileExistsError:
        pass
