import shutil
import os

source_dir = './Data/txt_files'  
target_dir = './Data/csv_files'  
files_to_move = ['city_weather_data.csv', 'list_of_country.csv']

if not os.path.exists(target_dir):
    os.makedirs(target_dir)


for file_name in files_to_move:
    source_file = os.path.join(source_dir, file_name)  
    target_file = os.path.join(target_dir, file_name)  

    
    if os.path.exists(source_file):
        shutil.move(source_file, target_file)
        print(f"{file_name} {target_dir}")
    else:
        
        print(f"{file_name}  {source_dir}.")

for file_name in files_to_move:
    target_file = os.path.join(target_dir, file_name)
    if os.path.exists(target_file):
        print(f"{file_name} successful {target_dir}")
    else:
        print(f"{file_name} successful {target_dir}")
