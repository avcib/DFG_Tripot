# DFG_Tripot Dataset and Friction Data Analysis

This GitHub repository contains the Phyton code associated with the data descriptor (also known as data note) article, entitled "Dataset on surface topographies prepared by micro-milling and their friction coefficients in dry sliding" [1]. It makes use of the "Dataset on surface topographies prepared by micro-milling and their friction coefficients in dry sliding" [2]. The provided code allows the users to process and visualize friction data as a function of scratch cycles in linear tribometer configuration and to calculate the average coefficient of friction (CoF) per cycle.

  Please check the requirements.txt for the dependencies.

  The repository follows the directory structure below:
├── data/
│     └── exported_AP/
│       └── [Experimental data files, e.g., CoF_S13_90_1N.txt]
├── main.py
└── README.md

  To use this code: 
  
  Option A. 1) Close the repository to a local environment, 2) Add your raw experimental data (as .txt or .csv), and 3) Run the script, main.py. 
   
   Option B. 1) Make a copy from the public Google Colab link (https://drive.google.com/drive/folders/1QHJ2wWERrZ26aeoMX7Jf5ze0MeFTS1gi?usp=drive_link), Add your raw experimental data (as .txt or .csv), and 3) Run the script online.
  
[1] Avci, B., Farahani, P., Riemer, O., Karpuschewski, B., & Mehner, A. Dataset on surface topographies prepared by micro-milling and their friction coefficients in dry sliding. _Under review._
	
[2] Avci, B., Farahani, P., Riemer, O., Karpuschewski, B., & Mehner, A. (2026). Dataset on surface topographies prepared by micro-milling and their friction coefficients in dry sliding [Data set]. Zenodo. https://doi.org/10.5281/zenodo.18014400
