import os
import shutil

species_dir = 'species'
species_path = os.path.join('.', species_dir)

targets_dir = 'targets'
targets_path = os.path.join('.', targets_dir)
os.makedirs(targets_path, exist_ok=True)

species_file_count = dict()

# list species with a lot of pictures
for dir, _, file in os.walk(species_path):
    if dir == species_path:
        continue

    path_arr = dir.split('/')
    species = path_arr[2]
    image_count = len([img for img in os.listdir(dir) if os.path.isfile(os.path.join(dir, img))])

    species_file_count[species] = image_count


sorted_species_file_count = dict(sorted(species_file_count.items(), key=lambda x:x[1], reverse=True))

# f = open('target_species.txt', 'w')

high_img_count = 0
for key in sorted_species_file_count:
    value = sorted_species_file_count[key]

    if value >= 230 and value <= 600:
    # if value >= 200:
        species_dir = os.path.join(species_path, key)
        # print(species_dir)

        target_species_path = os.path.join(targets_path, key)
        os.makedirs(target_species_path, exist_ok=True)

        high_img_count += 1
        # print(key, value)
        print(key)

        # !!! FILE OPERATION !!!
        # write to txt file
        # f.write(key + '\n')

        for dir, _, file in os.walk(species_dir):
            for img in file:
                image_path = os.path.join(dir, img)
                # !!! FILE OPERATION !!!
                # shutil.copy(image_path, target_species_path)
# f.close()

print('count: ', high_img_count)
