import os
import json
from tqdm import tqdm

DATA_PATH = '/mnt/data/aihub/road_infra'
DATA_TRAIN = os.path.join(DATA_PATH, 'Training')
DATA_VAL = os.path.join(DATA_PATH, 'Validation')
HIGHWAY_NONCITY = '1_1'
NATIONAL_NONCITY = '2_1'
LOCAL_NONCITY = '3_1'
NATIONAL_CITY = '2_2'
LOCAL_CITY = '3_2'

def get_image_path():
    image_path = dict()
    image_path['train_highway_noncity'] = os.path.join(DATA_TRAIN, 'images', f'TS_{HIGHWAY_NONCITY}')
    image_path['train_national_noncity'] = os.path.join(DATA_TRAIN, 'images', f'TS_{NATIONAL_NONCITY}')
    image_path['train_local_noncity'] = os.path.join(DATA_TRAIN, 'images', f'TS_{LOCAL_NONCITY}')
    image_path['train_national_city'] = os.path.join(DATA_TRAIN, 'images', f'TS_{NATIONAL_CITY}')
    image_path['train_local_city'] = os.path.join(DATA_TRAIN, 'images', f'TS_{LOCAL_CITY}')

    image_path['val_highway_noncity'] = os.path.join(DATA_VAL, 'images', f'VS_{HIGHWAY_NONCITY}')
    image_path['val_national_noncity'] = os.path.join(DATA_VAL, 'images', f'VS_{NATIONAL_NONCITY}')
    image_path['val_local_noncity'] = os.path.join(DATA_VAL, 'images', f'VS_{LOCAL_NONCITY}')
    image_path['val_national_city'] = os.path.join(DATA_VAL, 'images', f'VS_{NATIONAL_CITY}')
    image_path['val_local_city'] = os.path.join(DATA_VAL, 'images', f'VS_{LOCAL_CITY}')

    return image_path

def get_label_path():
    label_path = dict()
    label_path['train_highway_noncity'] = os.path.join(DATA_TRAIN, 'labels', f'TL_{HIGHWAY_NONCITY}')
    label_path['train_national_noncity'] = os.path.join(DATA_TRAIN, 'labels', f'TL_{NATIONAL_NONCITY}')
    label_path['train_local_noncity'] = os.path.join(DATA_TRAIN, 'labels', f'TL_{LOCAL_NONCITY}')
    label_path['train_national_city'] = os.path.join(DATA_TRAIN, 'labels', f'TL_{NATIONAL_CITY}')
    label_path['train_local_city'] = os.path.join(DATA_TRAIN, 'labels', f'TL_{LOCAL_CITY}')

    label_path['val_highway_noncity'] = os.path.join(DATA_VAL, 'labels', f'VL_{HIGHWAY_NONCITY}')
    label_path['val_national_noncity'] = os.path.join(DATA_VAL, 'labels', f'VL_{NATIONAL_NONCITY}')
    label_path['val_local_noncity'] = os.path.join(DATA_VAL, 'labels', f'VL_{LOCAL_NONCITY}')
    label_path['val_national_city'] = os.path.join(DATA_VAL, 'labels', f'VL_{NATIONAL_CITY}')
    label_path['val_local_city'] = os.path.join(DATA_VAL, 'labels', f'VL_{LOCAL_CITY}')

    return label_path

def count_files(directory):
    return sum(len(files) for _, _, files in os.walk(directory))

def image_distribution():
    print('###')
    print('# Image Distribution')
    print('###')
    image_path = get_image_path()
    count_dict = dict()

    for k in image_path:
        count_dict[k] = count_files(image_path[k])

    highway_noncity = count_dict['train_highway_noncity'] + count_dict['val_highway_noncity']
    national_noncity = count_dict['train_national_noncity'] + count_dict['val_national_noncity']
    local_noncity = count_dict['train_local_noncity'] + count_dict['val_local_noncity']
    national_city = count_dict['train_national_city'] + count_dict['val_national_city']
    local_city = count_dict['train_local_city'] + count_dict['val_local_city']

    noncity = highway_noncity + national_noncity + local_noncity
    city = national_city + local_city

    total = noncity + city

    noncity_percentage = round(noncity / total * 100, 2)
    city_percentage = round(city / total * 100, 2)

    highway_noncity_percentage = round(highway_noncity / total * 100, 2)
    national_noncity_percentage = round(national_noncity / total * 100, 2)
    local_noncity_percentage = round(local_noncity / total * 100, 2)
    national_city_percentage = round(national_noncity / total * 100, 2)
    local_city_percentage = round(local_noncity / total * 100, 2)


    print(f"Total: {total}")
    print()
    print(f"Non-city: {noncity}({noncity_percentage}%)")
    print(f"City: {city}({city_percentage}%)")
    print()
    print(f"Highway Non-city: {highway_noncity}({highway_noncity_percentage}%)")
    print(f"National Non-city: {national_noncity}({national_noncity_percentage}%)")
    print(f"Local Non-city: {local_noncity}({local_noncity_percentage}%)")
    print(f"National City: {national_city}({national_city_percentage}%)")
    print(f"Local City: {local_city}({local_city_percentage}%)")
    print()

def object_distribution():
    print('###')
    print('# Object Distribution')
    print('###')
    label_path = get_label_path()
    class_dict = dict()
    region_dict = dict()
    roadtype_dict = dict()
    regiontype_dict = dict()
    state_dict = dict()

    for k in label_path:
        json_list = os.listdir(label_path[k])
        for i in tqdm(json_list, k):
            with open(os.path.join(label_path[k], i)) as f:
                label = json.load(f)

            for anno in label['annotations']:
                obj_name = anno['name']
                obj_region = anno['region1']
                obj_roadtype = anno['roadtype']
                obj_regiontype = anno['regiontype']
                obj_state = anno['state']

                if obj_name not in class_dict:
                    class_dict[obj_name] = 0
                if obj_region not in region_dict:
                    region_dict[obj_region] = 0
                if obj_roadtype not in roadtype_dict:
                    roadtype_dict[obj_roadtype] = 0
                if obj_regiontype not in regiontype_dict:
                    regiontype_dict[obj_regiontype] = 0
                if obj_state not in state_dict:
                    state_dict[obj_state] = 0

                class_dict[obj_name] += 1
                region_dict[obj_region] += 1
                roadtype_dict[obj_roadtype] += 1
                regiontype_dict[obj_regiontype] += 1
                state_dict[obj_state] += 1

    print('Class:')
    for k, v in class_dict.items():
        print(f'{k}: {v}')
    print()
    print('Region:')
    for k, v in region_dict.items():
        print(f'{k}: {v}')
    print()
    print('Road Type:')
    for k, v in roadtype_dict.items():
        print(f'{k}: {v}')
    print()
    print('Region Type:')
    for k, v in regiontype_dict.items():
        print(f'{k}: {v}')
    print()
    print('State:')
    for k, v in state_dict.items():
        print(f'{k}: {v}')
    print()

def count_by_each_split():
    print('###')
    print('# Data split')
    print('###')
    image_path = get_image_path()
    image_split_dict = { 'train': dict(), 'val': dict(), 'test': dict()}

    for k in image_path:
        if k.startswith('train'):
            image_split_dict['train'][k] = count_files(image_path[k])
        elif k.startswith('val'):
            image_split_dict['val'][k] = count_files(image_path[k])
        else:
            image_split_dict['test'][k] = count_files(image_path[k])
    print('Images(Train):')
    for k, v in image_split_dict['train'].items():
        print(f'{k}: {v}')
    print()
    print('Images(Validation):')
    for k, v in image_split_dict['val'].items():
        print(f'{k}: {v}')
    print()
    print('Images(Test):')
    for k, v in image_split_dict['val'].items():
        print(f'{k}: {v}')
    print()

    label_path = get_label_path()
    label_split_dict = { 
            'train': {'bbox': 0, 'seg': 0}, 
            'val': {'bbox': 0, 'seg': 0},
            'test': {'bbox': 0, 'seg': 0},
        }

    for k in label_path:
        json_list = os.listdir(label_path[k])
        for i in tqdm(json_list, k):
            with open(os.path.join(label_path[k], i)) as f:
                label = json.load(f)

            for anno in label['annotations']:
                obj_bbox = anno['bbox']
                obj_seg = anno['segmentation']

                if k.startswith('train'):
                    label_split_dict['train']['bbox'] += 1 if len(obj_bbox) > 0 else 0
                    label_split_dict['train']['seg'] += 1 if len(obj_seg) > 0 else 0 
                elif k.startswith('val'):
                    label_split_dict['val']['bbox'] += 1 if len(obj_bbox) > 0 else 0
                    label_split_dict['val']['seg'] += 1 if len(obj_seg) > 0 else 0
                else:
                    label_split_dict['test']['bbox'] += 1 if len(obj_bbox) > 0 else 0
                    label_split_dict['test']['seg'] += 1 if len(obj_seg) > 0 else 0
    print('Objects(Train):')
    for k, v in label_split_dict['train'].items():
        print(f'{k}: {v}')
    print()
    print('Objects(Validation):')
    for k, v in label_split_dict['val'].items():
        print(f'{k}: {v}')
    print()
    print('Objects(Test):')
    for k, v in label_split_dict['val'].items():
        print(f'{k}: {v}')
    print()


# Road Type and Proportional Coverage
# Distribution of Roads
image_distribution()

# Class/Region Distribution
# Road/Region Type Distribution
# Facility Status Distribution
object_distribution()

# Train/Validation Data Split for BBox/Segentation
count_by_each_split()

