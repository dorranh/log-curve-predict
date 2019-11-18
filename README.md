# log-curve-predict

## Digital Geosciences Hackathon 2019 Entry

### Contributors:
  * Nicholas Shea
  * Giuseppe Amendola
  * Dorran Howell
  * Aline Robin
  * Mubeen Muhtar
  * Tanner Acquisto

### Installation
All required libraries are specified in the project's requirements.txt file. If you have python installed, they can be installed via: 
  > $ pip install -r requirements.txt

### Running the Models

#### Notebooks

This repo is mainly comprised of notebooks in the notebook/ directory. To run these notebooks, you should have jupyter or jupyter lab installed:

https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html

#### Data

A csv file of synthetic well log data, all_synthetic_well_logs.zip, is provided via git-lfs. You'll need to download (if it wasn't pulled when you cloned the repo) and unzip this file to run the example notebooks.


### Summary

TOPIC: Predicting missing log data

WORFLOW
1- EXTRACTING (RHOB,DTCO,DTSM) SYNTHETIC DATA
2- DATA FORMATING 
3- (80% DATA - TRAINING) BUILD MACHINE LEARNING MODELS
4- (20% DATA - TESTING) ACCURACY MEASUREMENT
  
Conclusion:
Our model produces comparable predictions with rock physics based estimations (Marmousi2 Model, 2004). Our focus on estimating missing Vs logs; however, this approach can be extended to estimating any other kinds of missing logs using different input log types.

Wayforward:
1) Real industry data training required
1.1) Crosscheck rock phyiscs against ML
1.2) Depth trend analysis
2) Application of petrophysics, rock physics and geomechaincs prediction and model building
3) Well log data quick look and analysis
4) Improvement with the application of DL
