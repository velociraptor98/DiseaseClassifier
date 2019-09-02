## Introduction:
The idea of the project is to provide clinical pathologists an interface through which they can classify the genes which cause mutations during cancer.
This project is made with the view of reducing the effort and time taken by the doctors spent on classifying genes based on reports.
The purpose of the project is to reduce the effort taken by pathologists to manually classify the genes which causes mutations based on evidence from text based clinical literature.
It also helps people with HIV to know whether their conditions is Improving or not.

## Dataset
https://www.kaggle.com/c/hivprogression/data
https://www.kaggle.com/c/msk-redefining-cancer-treatment/overview

## Steps to run-
1. Ensure data.zip is extracted
2. Run app2.py
3. Example Inputs 
	1. Cancer gene input
	   gene- FAM58A
	   variation- Truncating Mutations
	   text- report text 
	2. HIV progression - 
	    VL-t0- 4.3
	    CD4-t0- 145
	    Output- Class 0
		
## Requirements-
python 3.7
Flask==1.0.2
Keras==2.2.4
numpy==1.15.4
matplotlib==3.0.2
pandas==0.23.4
scikit-learn==0.20.1
sklearn==0.0
tensorflow==1.13.1

## Bugs

There is a bug in passing data that can crash the resultCancer.html.
