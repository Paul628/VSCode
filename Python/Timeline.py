import ctypes
import string
import sys
import os, math, time
from natsort import natsorted
import shutil
import glob


os.system('cls' if os.name == 'nt' else 'clear')
print("")
print("")
ctypes.windll.kernel32.SetConsoleTitleW("TIMELINE CHECKER")

path = input('Scene folder:  ').replace('"','')

anim_path = input('Output folder:  ').replace('"','')

if not os.path.exists(anim_path):
    os.makedirs(anim_path)

print(f"\nSearching .png files...\n")

files = glob.glob(path + '/**/*.png', recursive=True)
total_files = len(files)-1

print(f"\n({total_files}) .png files founded.\n")
count = -1
tl_count = 0


for current_file in files :
    if os.path.isfile(current_file):
        with open(current_file, 'rt', encoding="ansi") as fp:
            for index, line in enumerate(fp):
                if line.count("Timeline") >= 2:
                    tl_count += 1
                    file_name = os.path.split(current_file)
                    print('\nTimeline scene found: '+file_name[1]+'\n')
                    fp.close()
                    shutil.move(current_file, anim_path+'\\'+file_name[1])
                    break
    count +=1
    print(f"\n({count}/{total_files}) Timeline scene count: [{tl_count}]\n")

print("\n╭⋟────────────────────────────────────────────────────────────────╮")
print(f'\n                 Total timeline scenes found: [{tl_count}/{total_files}]\n')
print("╰────────────────────────────────────────────────────────────────⋞╯\n\n")