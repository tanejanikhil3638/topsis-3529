import pandas as pd
import numpy as np


def normalize_data(matrix):
    norm_factor = (matrix ** 2).sum(axis=0) ** 0.5
    # Check for zero before performing normalization
    norm_matrix = matrix / np.where(norm_factor == 0, 1, norm_factor)
    return norm_matrix

def cal_topsis_score(matrix, weights, impacts):
    normalize_matrix = normalize_data(matrix)
    print("normalize_matrix:", normalize_matrix)

    weighted_normalize_matrix = normalize_matrix * weights
    print("weighted_normalize_matrix:", weighted_normalize_matrix)

    ideal_best = [weighted_normalize_matrix[:, i].max() if impacts[i] == '+' else weighted_normalize_matrix[:, i].min() for i in range(len(weights))]
    print("ideal_best:", ideal_best)

    ideal_worst = [weighted_normalize_matrix[:, i].min() if impacts[i] == '+' else weighted_normalize_matrix[:, i].max() for i in range(len(weights))]
    print("ideal_worst:", ideal_worst)

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    distance_best = ((weighted_normalize_matrix - ideal_best) ** 2).sum(axis=1) ** 0.5
    distance_worst = ((weighted_normalize_matrix - ideal_worst) ** 2).sum(axis=1) ** 0.5

    performance_score = distance_worst / (distance_best + distance_worst)

    return performance_score

def rank_objects(score):
    # return pd.Series(score).rank(ascending=False, na_option='bottom')
    order = np.argsort(score, kind='quicksort')[::-1]
    ranks = np.empty_like(order)
    ranks[order] = np.arange(1, len(score) + 1)
    return ranks
    
def topsis(input_file, weights, impacts, result_file):
    try:
        #input
        data = pd.read_csv(input_file,index_col=0)
        # no. of colums
        if(data.shape[1]<3):
            raise ValueError("Input file must contain at least 3 columns. ")
        
        # numeric values error
        if(not data.applymap(lambda x: isinstance(x, (int,float))).all().all()):
            raise ValueError("Input file must contain numeric values only. ")
        
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')

        # size is same?
        if len(weights) != len(impacts) or len(weights) != data.shape[1]:
            raise ValueError("Number of weights, impacts, and columns must be the same.")
        
        if not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be either + or -.")

        topsis_score = cal_topsis_score(data.values[:, 0:], weights, impacts)
        data['Topsis Score'] = topsis_score
        data['Rank'] = rank_objects(topsis_score)

        print(data['Rank'])
        print(topsis_score)
        
        # Save result to CSV file
        data.to_csv(result_file)
        print("Topsis completed successfully. Result saved to", result_file)
        
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as e:
        print("Error:", str(e))
