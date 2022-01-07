# AbnormalityDetection
#To find the abnormal point of the Cyclone Preheater using Statistical techniques
## Python Libraries
- Pandas
- Scipy

## Preprocessing the Dataset
### The dataset consists of 6 features.
- Cyclone_Inlet_Gas_Temp   – Temperature of Hot gas entering the cyclone
- Cyclone_Gas_Outlet_Temp  – Temperature of Hot gas leaving the cyclone
- Cyclone_Outlet_Gas_draft – Draft (pressure) of gas at outlet of cyclone
- Cyclone_cone_draft       – Draft (pressure) of gas at cone section of cyclone
- Cyclone_Inlet_Draft      – Draft (pressure) of gas at inlet of cyclone
- Cyclone_Material_Temp    – Temperature of the material at the outlet of the cyclone.

### About Preprocessing
The unobserved values in the features are removed and the dataset is partitioned with respect to the features. 

## Abnormality Detection
The objective is to detect the abnormal data points in the features.The preprocessed CSV files are intruded inside the Abnormality_Detection.py file
and the abnormal data points are returned.
 
## Methodology
This problem is approached by using zscore analysis, which will detect the abnormal data points with respect to the input threshold given for all the feature variables.
Note: Threshold value is the number of deviations from the mean value. 

## File Structure
Intern_Project
|
+---main.py
+---Preprocessor.py
+---Abnormality_Detection.py

## Working
### Preprocessor.py
- The missing values in the dataset is been handled.
- The dataset is partitioned based on each feature.
- CSV files are generated for each feature

### Abnormality_Detection.py
- The threshold value is taken as input from the user.
- All the features are scaled according to z_score normalization.
- Abnormalities are detected from the scaled features with respect the threshold value.

### main.py
- Preprocessor and dectector objects are called in the main.py file

# Software Requirements
- Python version 3.9.0 or above
- Pandas 
- Scipy

# How to run the Code
```
$ python main.py
```


