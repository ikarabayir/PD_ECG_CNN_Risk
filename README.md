# ECG-AI_PD_Risk_Prediction
Externally Validated Artificial Intelligence Model to Identify Parkinson’s Disease at Prodromal Phase

# Requirements

* Python 3.7.7
* scikit-learn              0.22.1
* scipy                     1.5.2
* tensorflow                1.15.0         
* tensorflow-base           1.15.0          
* tensorflow-estimator      1.15.1            
* keras                     2.2.4             
* keras-applications        1.0.8           
* keras-base                2.2.4


# Getting Started
1. Required Python versions and libraries are listed above. 
2. Get the code $ git clone the repo and install the dependencies
3. For 10 year predicted risk scores and labels, execute the code below in the local repo directory
4. Please make sure that your input ECG follows the format provided here. e.g. 12-Lead, 10 seconds, at 500Hz. following the lead order of: I, II, III, aVR, aVL, aVF, V1, V2, V3, V4, V5, V6

python Github-ECG-AI_PD_Risk_Prediction.py sample_ECG.npy

The py file would provide risk scores and labels to your local directory as csv files.

# Citation

If you find this code useful, please cite the following paper:

Externally Validated Artificial Intelligence Model to Identify Parkinson’s Disease at Prodromal Phase
Ibrahim karabayir, fatma gunturkun, Samuel goldman, rishikesan kamaleswaran, Robert l davis, kalea colletta, Katherine bobay, webb ross, helen Petrovitch, kamal masaki, Carolina tanner, oguz akbilgic*


*Corresponding Author

# Contact

For any feedback, or bug report, please don't hesitate to the author, [Dr. Ibrahim Karabayir](mailto:ikarabayir34@gmail.edu?subject=[AI_PD_ECGModel])
