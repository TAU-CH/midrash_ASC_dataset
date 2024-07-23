# midrash_ASC_dataset
Ashkenazi Square Clustering (ASC) dataset contains handwritten Hebrew document images that are required to be clustered according to their paleographic features. Essentially, we are aware of two groups, German and French scripts ([Olszowy-Schlanger, 2017](https://www.nli.org.il/en/articles/RAMBI990006168700705171/NLI)). However, no labels are provided. The problem is entirely unsupervised, and the output needs to be evidence-based, providing the user with the reasons that lead to a specific clustering.
The dataset comprises document images from 59 different manuscripts provided by Judith Olszowy-Schlanger. 

# Description of each file and folder included in this repository.

- **cropped_text_regions**: This folder contains cropped text region images sourced from 59 manuscripts. Each manuscript contributes one to four pages, and the images are named sequentially following the "manuscriptname_pagename" convention.

- **map_sequential_name_to_metadata.txt**: This text file provides a mapping between the sequential names of the images and their metadata. The structure is formatted as "manuscriptname pagename date region city".

- **metadata.xlsx**: Prepared by paleographer Daria Vasyutinsky, this Excel file contains detailed metadata for each image. The metadata compilation follows guidelines established by Judith Olszowy-Schlanger.

- **textline_detection_coco.json**: This COCO JSON file includes bounding box coordinates  the text lines within the cropped text regions.

- **crop_textlines.py**: This Python crops the text lines from the text regions and save them into folders named with the name of the text region they are cropped from.





