# HPClas: A new computational approach for identifying halophilic proteins based on Machine Learning

## Introduction



![image.png](attachment:af4c7f4f-7851-494e-a913-61e721a39a40.png)

## Code details

* Users can run the HPClas.py to identify the Halophilic proteins. 

* featureGenerator.py is implemented for feature generation. 

The features descriptors including Amino Acid Composition (AAC), the Composition of K-Spaced Amino Acid Pairs (CKSAAP), Di-Peptide Composition (DPC), Tri-Peptide composition (TPC), and Dipeptide Deviation from Expected Mean (DDE),the Composition(CTDC), Transition(CTDT), Distribution(CTDD), Conjoint Triad (CTriad), Grouped amino acid composition(GAAC), Grouped Di-Peptide Composition(GDPC).

* predicton.py can be used for the final prediction based on the generated features.

## Dependency
* python 3.9
* catboost 1.0.6
* scikit_learn 1.2.1

## Dataset
* train_P.fasta: postives samples for training 
* train_N.fasta: negative samples for training
* indep_test_P.fasta: postives samples for testing 
* indep_test_N.fasta: negative samples for testing
* Experimental_validation_set.fasta: samples validated by wet experiments


**The customized file should be consistant with the example files(input/example.fasta)

## Installation Guide

*  Install from Github 
```python
git clone https://github.com/xxx
cd HPClas

```

## Usage

* Run the default dataset
```
python HPClas.py --type benchmark
```
* Make the prediction for customize data and threshold
```
python HPClas.py --type predict --fasta_file <Fasta_file>  --output_name <output_name> --threshold <threshold>
```

* output results format
|    |mean|pred|
| :-----------:  | :-----------: | :-----------: |
|index|pred_prob|final score|
