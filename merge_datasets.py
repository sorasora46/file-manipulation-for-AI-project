import os
import shutil
import yaml

# Define the merged dataset directory
merged_dataset_dir = 'merged_dataset'
os.makedirs(merged_dataset_dir, exist_ok=True)

os.makedirs(merged_dataset_dir + '/test', exist_ok=True)
os.makedirs(merged_dataset_dir + '/test/images', exist_ok=True)
os.makedirs(merged_dataset_dir + '/test/labels', exist_ok=True)

os.makedirs(merged_dataset_dir + '/train', exist_ok=True)
os.makedirs(merged_dataset_dir + '/train/images', exist_ok=True)
os.makedirs(merged_dataset_dir + '/train/labels', exist_ok=True)

os.makedirs(merged_dataset_dir + '/valid', exist_ok=True)
os.makedirs(merged_dataset_dir + '/valid/images', exist_ok=True)
os.makedirs(merged_dataset_dir + '/valid/labels', exist_ok=True)

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += str(ele) + " "
    return str1.strip()

dataset_folders = []
for dir, _, _ in os.walk('.'):
    if dir.endswith('.yolov8'):
        dataset_folders.append(dir)

class_names = []

# copy images in test, train, valid to merge folder
for dataset in dataset_folders: # dataset folder
    data_yaml_path = os.path.join('.', dataset, 'data.yaml')

    data_file = open(data_yaml_path, 'r')
    data = yaml.load(data_file, Loader=yaml.FullLoader)
    names = data['names']
    data_file.close()

    for name in names:
        class_names.append(name)

    init_index = len(class_names)

    for split in ['test', 'train', 'valid']: # split folders in dataset
        split_path = os.path.join(dataset, split)
        image_folder_path = os.path.join(split_path, 'images')
        label_folder_path = os.path.join(split_path, 'labels')

        for image in os.listdir(image_folder_path): # images in each split
            new_image_path = os.path.join('.', merged_dataset_dir, split, 'images')
            new_label_path = os.path.join('.', merged_dataset_dir, split, 'labels')

            image_name = image[:len(image) - 4]
            image_path = os.path.join(image_folder_path, image)
            label_path = os.path.join(label_folder_path, image_name + '.txt')

            label_file = open(label_path, 'r') 
            label_string = label_file.read()
            label_file.close()

            annotation_arr = label_string.split('\n')

            annotation = []

            old_index = 0

            new_label_file = open(os.path.join(new_label_path, image_name + '.txt'), 'w')

            if len(annotation_arr) > 1:
                old_index = int(annotation_arr[0].split(' ')[0])
                new_index = old_index + init_index


                for i in range(len(annotation_arr)):
                    annotation_arr[i].split(' ')[0] = str(new_index)
                    annotation.append(annotation_arr[i].split(' '))
                    new_label_file.write(listToString(annotation) + '\n')
                

            else:
                annotation = annotation_arr[0].split(' ')
                if annotation[0] == '':
                    continue

                old_index = int(annotation[0])
                new_index = old_index + init_index

                annotation[0] = new_index

                new_label_file.write(listToString(annotation) + '\n')

            new_label_file.close()
            shutil.copy(image_path, new_image_path) # check by count file number after merged

new_data_file = open(os.path.join('.', merged_dataset_dir, 'data.yaml'), 'w')

new_data_file.write('train: ../train/images\n')
new_data_file.write('val: ../valid/images\n')
new_data_file.write('test: ../test/images\n')

new_data_file.write('\n')

new_data_file.write('nc: ' + str(len(class_names)) + '\n')
new_data_file.write('names: ' + str(class_names) + '\n')

new_data_file.close()