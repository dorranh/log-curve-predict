# log-curve-predict

## Digital Geosciences Hackathon 2019 Entry

### Summary

__Topic:__ Predicting missing log data

__Our Workflow:__
1.) Extract synthetic well log data from reference model (RHOB, DTCO, DTSM)
2.) Clean input dataset 
3.) Train a variety of models using pymc3 and sklearn
4.) Evaluate and compare model accuracy/performance
  
__Conclusion:__
Our model produces comparable predictions with rock physics based estimations (Marmousi2 Model, 2004). Our focus on estimating missing Vs logs; however, this approach can be extended to estimating any other kinds of missing logs using different input log types.

__Next Steps:__
1) Train on real-world data
2) Crosscheck rock phyiscs against ML models
3) Depth trend analysis
4) Application of petrophysics, rock physics and geomechaincs prediction and model building
5) Well log data quick look and analysis
6) Improvement with the application of DL

### Installation
All required libraries are specified in the project's requirements.txt file. If you have python installed, they can be installed via: 
  > $ pip install -r requirements.txt

### Running the Models

#### Notebooks

This repo is mainly comprised of notebooks in the notebook/ directory. To run these notebooks, you should have jupyter or jupyter lab installed:

https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html

#### Data

A csv file of synthetic well log data, all_synthetic_well_logs.zip, is provided via git-lfs. You'll need to download (if it wasn't pulled when you cloned the repo) and unzip this file to run the example notebooks.


### Contributors:
  * Nicholas Shea
  * Giuseppe Amendola
  * Dorran Howell
  * Aline Robin
  * Mubeen Muhtar
  * Tanner Acquisto


