import sys
import os
import random

def main():
    os.chdir('/Users/shikha/Documents/code/pythonMisc/functionalCode')
    fpLotto = open('./TattsLotto.csv')
    lstFile = []
    lstMyLotto = [[1,  4,  11,  27,  33,  38],
                [5,  16,  22,  30,  40,  42],
                [7,  13,  26,  30,  37,  41],
                [8,  10,  12,  25,  28,  39],
                [7,  8,  18,  22,  39,  44]]
    for num in lstMyLotto:
        print(num)
    for line in fpLotto:
        lstFile.append(line)

if __name__ == "__main__":
    main()