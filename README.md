# Large-Scale Nationwide Korean Road Infrastructure Dataset for Comprehensive Road Facility Recognition for Comprehensive Road Facility Recognition

[![Paper](https://img.shields.io/badge/Paper-UnderReview-blue?style=for-the-badge&logo=adobeacrobatreader)](https://drive.google.com/file/d/1BAdLggaiQaVZGeg28dY7paguXNcEV-lX/view?usp=drive_link)
[![Download](https://img.shields.io/badge/Download-Sample(480MB)-blue?style=for-the-badge&logo=databricks)](https://drive.google.com/file/d/1BAdLggaiQaVZGeg28dY7paguXNcEV-lX/view?usp=drive_link)
[![Code](https://img.shields.io/badge/Code-GitHub-black?style=for-the-badge&logo=github)](YOUR_CODE_LINK)


This repository provides a comprehensive dataset of road infrastructure across various regions of South Korea. 
Below, you can find details on how to access sample data, cite the dataset, and read our accompanying paper.



---

## Introduction
We collected over two million high-resolution (3328×1872) frames using nine survey vehicles equipped with camera and GPS sensors. From these, 200,000 frames were refined and annotated with:
- **34 distinct facility types** (e.g., traffic signals, guardrails, tunnels, etc.)
- **2,676,583 labeled instances** (bounding boxes and polygon annotations)
- Coverage of **highways, national roads, and local roads** in both **city and non-city** areas

The dataset supports tasks such as object detection and segmentation, aiming to advance road safety asset management, intelligent transportation systems, and autonomous driving research.

---

## Sample Dataset Download
We have provided a **480MB** sample dataset for quick exploration.

- **[Download Sample Dataset (Google Drive)](https://drive.google.com/file/d/1BAdLggaiQaVZGeg28dY7paguXNcEV-lX/view?usp=drive_link)**

This sample includes a subset of images and annotations (bounding boxes + polygons), along with a JSON file in a COCO-like format.  
**De-identification** is applied to ensure privacy (faces, license plates, etc. are blurred).

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


License
This dataset is released under CC-BY-NC-SA license.

Citation
If you use this dataset or any subset in your research, please cite:
@misc{kim2025road,
  title   = {Large-Scale Nationwide Korean Road Infrastructure Dataset 
             for Comprehensive Road Facility Recognition},
  author  = {Kim, Hyeongbok and Kim, Eunbi and Ahn, Sanghoon and Kim, Beomjin 
             and Kim, Sung Jin and Sung, Tae Kyung and Zhao, Lingling 
             and Su, Xiaohong and Dong, Gilmu},
  year    = {2025},
}
