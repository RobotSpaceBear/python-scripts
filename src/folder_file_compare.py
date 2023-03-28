import os

dir1_path = "H:\\folder1"
dir2_path = "G:\\folder2"

dir1_files_array = []
dir2_files_array = []
dir1_files_not_in_dir2 = []

#print("Files in " + dir1_path)
for path in os.listdir(dir1_path):
  dir1_files_array.append(path)
  #print(path)

#print("Files in " + dir2_path)
for path in os.listdir(dir2_path):
  dir2_files_array.append(path)
  #print(path)

#print(dir1_files_array)

files_dir_1_not_in_dir2 = set(dir1_files_array) - set(dir2_files_array)
print("Files in "+dir1_path+" not in " + dir2_path)
print("\n".join(sorted(files_dir_1_not_in_dir2)))

print("===============")
files_dir_2_not_in_dir1 = set(dir2_files_array) - set(dir1_files_array)
print("Files in "+dir2_path+" not in " + dir1_path)
print("\n".join(sorted(files_dir_2_not_in_dir1)))



print("Done!")