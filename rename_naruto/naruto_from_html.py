import os
f = open(r'C:\Users\saket\Desktop\python files\rename\narutofiles\Naruto_episode_names.txt', encoding="utf-8")
episodes = f.read()
lis = episodes.split('\n')

old_names = []
quality = []
old_no = []

path = r"D:\naruto shippudin"+'\\'

for old_name in os.listdir(path):
    print(old_name)
    old_names.append(old_name)
    name_splitted = (old_name.split('.'))
    old_name = name_splitted[1]
    old_no.append(old_name)
    size = name_splitted[2]
    quality.append(size)


n = 0
for no in old_no:
    new_name = lis[int(no)-1]
    old_path = path+old_names[n]
    new_path = path+'EP.'+no+' '+new_name+' '+quality[n]+'.mp4'
    print(old_path, new_path)
    try:
        os.rename(old_path, new_path)
    except:
        pass
    n += 1
