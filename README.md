# TOPSIS Implementation

## Overview

This Python script provides an implementation of the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) for decision-making. The TOPSIS method is a multi-criteria decision analysis technique that evaluates a set of alternatives based on their similarity to the ideal solution.

## Usage

### Requirements

- Python 
- pandas
- numpy

### Installation

Install the required dependencies using the following command:

```bash
pip install pandas numpy
```


### How to Run

To use this script, run it from the command line with the following parameters:

```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
```
`<InputDataFile>`: The CSV file containing the input data.
`<Weights>`: Comma-separated weights for each criterion.
`<Impacts>`: Comma-separated impact values for each criterion. Use '+' for positive impact and '-' for negative impact.
`<ResultFileName>`: The desired name for the output CSV file that will contain the TOPSIS results.


Example
```bash
python topsis.py input_data.csv 1,1,1,+ + + - result.csv
```

### Input Format

The input data file must be a CSV file with numeric values only. The first column is considered as the identifier, and subsequent columns are criteria for evaluation.

### Ouput Format

The script generates a CSV file with additional columns for TOPSIS score and ranking. The result file provides insights into the decision-making process based on the specified weights and impacts.

### Error Handling

The script includes basic error handling for common issues, such as file not found, insufficient columns, and non-numeric values in the input data.

### Notes

Ensure that the input file contains at least 3 columns.
Weights and impacts must be provided as comma-separated values.
The number of weights, impacts, and columns in the input data must be the same.

### Contributors
Nikhil Taneja


