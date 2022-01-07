from Preprocessor import Preprocessing
from time import sleep
from Abnormality_Detection import Detector
#Preprocessing the dataset

preprocess=Preprocessing()
preprocess.Handling_Unobsevables()

sleep(5)

abnormals=Detector()
abnormals.Output()