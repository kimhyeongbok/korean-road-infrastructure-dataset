import os
import json

from tqdm import tqdm
from PIL import Image, ImageDraw

DATA_PATH = '/mnt/data/aihub/road_infra'
TRAIN_DIR = 'Training'
VAL_DIR = 'Validation'
IMAGE_DIR = 'images'
LABEL_DIR = 'labels'
YOLOTXT_DIR = 'yolotxt'
SUB_DIR = ['1-1', '2-1', '2-2', '3-1', '3-2']
class_dict = {
        0: "기둥",
        1: "가로재",
        2: "시선유도표지",
        3: "갈매기표지",
        4: "표지병",
        5: "장애물 표적표지",
        6: "구조물 도색 및 빗금표지",
        7: "시선유도봉",
        8: "조명시설",
        9: "도로반사경",
        10: "과속방지턱",
        11: "중앙분리대",
        12: "방호울타리",
        13: "충격흡수시설",
        14: "낙석방지망",
        15: "낙석방지울타리",
        16: "낙석방지 옹벽",
        17: "식생공법",
        18: "교량",
        19: "터널",
        20: "지하차도",
        21: "고가차도",
        22: "입체교차로",
        23: "지하보도",
        24: "육교",
        25: "정거장",
        26: "교통신호기",
        27: "도로 표지",
        28: "안전 표지",
        29: "도로명판",
        30: "긴급연락시설",
        31: "CCTV",
        32: "도로전광표시",
        33: "도로이정표",
}
class_dict_inv = {v: k for k, v in class_dict.items()}
#print(class_dict_inv)

target = VAL_DIR
for sd in SUB_DIR:
    label_dir = os.path.join(DATA_PATH,target,LABEL_DIR,sd)
    json_list = os.listdir(label_dir)
    for j in tqdm(json_list, desc=sd):
        json_path = os.path.join(label_dir, j) 
        with open(json_path) as f:
            label = json.load(f)

        if len(label['images']) > 1:
            print("Label file has multiple images.")
            continue
        img_name = label['images'][0]['file_name']
        img_width = label['images'][0]['width']
        img_height = label['images'][0]['height']

        img_path = os.path.join(DATA_PATH,target,IMAGE_DIR,sd,img_name)
        if not os.path.exists(img_path):
            print("Image not found:", img_path)
            continue
        yolotxt_path = img_path.rsplit('.', 1)[0].replace(IMAGE_DIR, YOLOTXT_DIR, 1)+".txt"
        yolotxt_dir = os.path.dirname(yolotxt_path)

        #debug_img = Image.open(image_path).convert("RGB")
        #draw = ImageDraw.Draw(debug_img)

        lines = ''
        for anno in label['annotations']:
            obj_catid = anno['category_id']
            obj_box = anno['bbox']
            obj_seg = anno['segmentation']
            obj_name = anno['name']

            if obj_name != class_dict[int(obj_catid-1)]:
                print('Class ID not matched')
                continue

            if len(obj_box) != 0:
                x, y, w, h = obj_box
                #draw.rectangle(((x, y), (x+w, y+h)), fill="black")
                #draw.text((x, y), obj_name)
                #debug_img.save('debug_img.jpg', "JPEG")

                xc = (x + w / 2) / img_width
                yc = (y + h / 2) / img_height
                bw = w / img_width
                bh = h / img_height
                yolobox = ["%.6f"%float(x) for x in (xc,yc,bw,bh)]

                line = f"{obj_catid-1} {' '.join(yolobox)}\n"
                lines += line

        os.makedirs(yolotxt_dir, exist_ok=True)
        with open(yolotxt_path,'w') as f:
            f.write(lines)

        
