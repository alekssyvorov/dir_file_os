import os

# path = r"C:\Users\Evgeniy\Desktop\tasks\task1"
# lst_dir = []
# lst_file = []
# for path, dirnames, filenames in os.walk(path):
#     print(f"Directories {dirnames}\nCount {len(dirnames)}")
#     print(f"File names {filenames}\nCount file {len(filenames)}")
#     break
#
# path = r"C:\Users\Evgeniy\Desktop\tasks\task2"
# for _, _, filenames in os.walk(path):
#     print(filenames)
#
# temp = []
# for i in filenames:
#     new = i[i.rfind("_")+1:i.rfind('.')] + "_" + i[:i.find("_")] + i[i.rfind('.'):]
#     os.replace(path+'\\'+i, path+"\\"+new)


path = r"C:\Users\Evgeniy\Desktop\tasks\task3"
for _, _, filenames in os.walk(path):
    print(filenames)
for i in filenames:
    if i.endswith(".png"):
        os.remove(path+"\\"+i)
print(filenames)