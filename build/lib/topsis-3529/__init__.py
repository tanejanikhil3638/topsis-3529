import sys
from main import topsis

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usages: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        input_file = sys.argv[1]
        weights = sys.argv[2]
        impacts = sys.argv[3]
        result_file = sys.argv[4]
        topsis(input_file, weights, impacts, result_file)