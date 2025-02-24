# KRID : A Large-Scale Nationwide Korean Road Infrastructure Dataset for Comprehensive Road Facility Recognition

[![Paper](https://img.shields.io/badge/Paper-UnderReview-black?style=for-the-badge&logo=adobeacrobatreader)](https://drive.google.com/file/d/1BAdLggaiQaVZGeg28dY7paguXNcEV-lX/view?usp=drive_link)
[![Download](https://img.shields.io/badge/Download-Sample(480MB)-blue?style=for-the-badge&logo=databricks)](https://drive.google.com/file/d/1BAdLggaiQaVZGeg28dY7paguXNcEV-lX/view?usp=drive_link)
[![Download](https://img.shields.io/badge/Download-Full-blue?style=for-the-badge&logo=github)](https://forms.gle/HFojMyLaLR9CSA6Q7)


This repository provides a comprehensive dataset of road infrastructure across various regions of South Korea. Below, you can find details on how to access sample data, cite the dataset, and read our accompanying paper. _**"Large-Scale Nationwide Korean Road Infrastructure Dataset for Comprehensive Road Facility Recognition"**_


![Road Infrastructure Image](img/main.png)

---

## Abstract
Comprehensive datasets are crucial for developing advanced AI solutions in road infrastructure. However, most existing resources provide only a narrow focus on vehicles or a limited set of object categories. To address this gap, we present the Korean Road Infrastructure Dataset (KRID), a large-scale collection specifically designed for real-world maintenance and safety applications. Covering highways, national roads, and local roads across both urban and rural areas, KRID encompasses 34 distinct facility types—from common elements (e.g., traffic signals and delineator posts) to specialized structures (e.g., tunnels and guardrails). Each instance is annotated using bounding boxes or polygon segmentation, following stringent quality-control protocols and privacy measures. To demonstrate the utility of the dataset, we conducted object detection and segmentation experiments with standard YOLO-based models, focusing on tasks such as guardrail damage detection and traffic sign recognition. These preliminary tests confirm KRID’s suitability for complex, safety-critical scenarios in intelligent transportation systems. Our main contributions include the following: (1) an extensive range of infrastructure classes beyond conventional “driving perception” datasets, (2) high-resolution, privacy-compliant annotations covering diverse road conditions, and (3) open-access availability via AI Hub and GitHub. By addressing critical infrastructure elements often overlooked in previous datasets, KRID paves the way for AI-driven maintenance workflows, hazard detection, and broader innovations in road safety.

---

## Introduction
We collected over two million high-resolution (3328×1872) frames using nine survey vehicles equipped with camera and GPS sensors. From these, 200,000 frames were refined and annotated with:
- Coverage of **highways, national roads, and local roads** in both **city and non-city** areas
![Coverage of Road](img/map.png)
![Region Distribution](img/Region_Distribution.png)
- **34 distinct facility types** (e.g., traffic signals, guardrails, tunnels, etc.)
![Road Facility](img/Road_Facility.png)
- **2,676,583 labeled instances** (bounding boxes and polygon annotations)

The dataset supports tasks such as object detection and segmentation, aiming to advance road safety asset management, intelligent transportation systems, and autonomous driving research.

---

## Sample Dataset Download
We have provided a **480MB** sample dataset for quick exploration.

- **[Download Sample Dataset (Google Drive)](https://drive.google.com/file/d/1BAdLggaiQaVZGeg28dY7paguXNcEV-lX/view?usp=drive_link)**

This sample includes a subset of images and annotations (bounding boxes + polygons), along with a JSON file. 

---

## Paper
For more details on our methodology, data acquisition, annotation guidelines, and benchmark experiments, please refer to our paper:

- **[View Full Paper (PDF)](Now Under Review)**

Topics covered:
- Data collection procedure (vehicles, cameras, GPS time sync)
- Annotation quality control and labeling guidelines
- Example deep learning experiments with YOLO v4 (bounding box) and YOLO v5 (segmentation)
- Results, analysis, and future directions

---
## Full Data Download Request
In order to access our dataset, you must first agree to the terms and conditions by completing a brief survey provided [here](https://forms.gle/HFojMyLaLR9CSA6Q7). You will receive the download link shortly after the approval process is completed.

---

## License
This dataset is released under the Creative Commons Attribution-NonCommercial-ShareAlike **(CC-BY-NC-SA)** license. 
This means you are free to share and adapt this dataset, under the following conditions:
- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- NonCommercial: You may not use the material for commercial purposes.
- ShareAlike: If you remix, transform, or build upon the dataset, you must distribute your contributions under the same license as the original.

For more detailed information on what is permitted and what is not, please refer to the official Creative Commons license summary.

---

## Citation
(Our paper is currently under review) 
If you use this dataset or any subset in your research, please cite:
```
@misc{kim2025road,
  title   = {Large-Scale Nationwide Korean Road Infrastructure Dataset 
             for Comprehensive Road Facility Recognition},
  author  = {Kim, Hyeongbok and Kim, Eunbi and Ahn, Sanghoon and Kim, Beomjin 
             and Kim, Sung Jin and Sung, Tae Kyung and Zhao, Lingling 
             and Su, Xiaohong and Dong, Gilmu},
  year    = {2025},
}
