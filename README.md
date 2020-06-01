# log-curve-predict

## Digital Geosciences Hackathon 2019 Entry

### Summary

__Topic:__ Predicting missing well log curves

__Our Workflow:__
1) Extract synthetic well log data from Marmousi2 reference model (RHOB, DTC, DTS)
2) Clean input dataset 
3) Train a variety of models using pymc3 and sklearn: Linear regression, Gradient Boosting Regressor and Bayesian Regression Solution with MCMC
4) Evaluate and compare model accuracy/performance
  
__Conclusion:__
Our study focuses on estimating missing DTS logs from RHOB and DTC; however, this approach can be extended to estimating any other kinds of missing logs using different input log types. Our best model -obtained with the gradient boosting regressor- produces comparable predictions with rock physics based estimations used in Marmousi2. 

__Next Steps:__
1) Depth trend analysis
2) Improvement with the application of DL
3) Train on real-world data
	a) Well log data quick look and analysis
	b) Crosscheck rock physics against ML models
4) Application of petrophysics, rock physics and geomechaincs prediction and model building

### Installation
All required libraries are specified in the project's requirements.txt file. If you have python installed, they can be installed via: 
  > $ pip install -r requirements.txt

### Running the Models

#### Notebooks

This repo is mainly comprised of notebooks in the notebook/ directory. To run these notebooks, you should have jupyter or jupyter lab installed:

https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html

#### Data

A csv file of synthetic well log data, [all_synthetic_well_logs.zip](all_synthetic_well_logs.zip) in the data/ directory, is provided via git-lfs. You'll need to download (if it wasn't pulled when you cloned the repo) and unzip this file to run the example notebooks.

### Contributors:
  * Nicholas Shea
  * Giuseppe Amendola
  * Dorran Howell
  * Aline Robin
  * Mubeen Muhtar
  * Tanner Acquisto


