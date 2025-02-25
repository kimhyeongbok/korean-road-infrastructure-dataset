## KRID Baseline Code and Examples

This directory features a collection of baseline implementations and dataset statistics for KRID. The goal of this baseline code is to offer a reproducible starting point for researchers working with this dataset.

### Dataset Statistics

It is useful to understand the dataset distribution. We provide a script to compute key statistics, including:
* Number of samples
* Image distributions
* Object distributions
* etc.

Run the following command to generate dataset statistics:
```bash
# Before run this python file, Set some paths in the file to yours
python3 statistic.py
```

### Training Baseline
We provide a simple baseline source code and config to convert KRID to YOLO format for training and evaluation. 

To convert the dataset to YOLO format, run:
```bash
# Before run this python file, Set some paths in the file to yours
python3 convert_to_yolo.py
```