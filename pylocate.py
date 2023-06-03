import os
print('absolute path')
def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

name = input('enter file name : ')
file_dir = input('enter file dir : ')
#file_dir = os.path.abspath(name)
print(find_files(name,file_dir))
