import os
import shutil

set_species = set()

snake_pic_dir = 'SnakeCLEF2023-medium_size'
snakeclef_path = os.path.join('SnakeCLEF2023-train-medium_size', snake_pic_dir)

species_dir = 'species'
os.makedirs(species_dir, exist_ok=True)

# right = 0
# wrong = 0

# get all species'names from each year folder
# 1784 species in total
for dir, _, file in os.walk(os.path.join('.', snakeclef_path)):
    path_arr = dir.split('/')
    last_item = len(path_arr) - 1 # index of species name in directory path

    species = path_arr[last_item] # get species name from path

    if (not species.isnumeric()) and (not species == snake_pic_dir): # check if it is year folder or SnakCLEF folder
        species_path = os.path.join(species_dir, species)

        if not species in set_species:
            set_species.add(species)
            os.makedirs(species_path, exist_ok=True)
        
        for img in file:
            image_path = os.path.join(dir, img)
            shutil.copy(image_path, species_path)
            # img_arr = image_path.split('/')
            # print('image_path: ', img_arr[len(img_arr) - 2])
            # print('species_path: ', species)
            # print('\n')
            # if img_arr[len(img_arr) - 2] == species:
            #     right += 1
            # else:
            #     wrong += 1

# print('right: ', right)
# print('wrong: ', wrong)