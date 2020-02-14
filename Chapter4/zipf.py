#!/usr/local/bin/python3
# Paul Evans (10evans@cua.edu)
# 13 February 2020
import math
import matplotlib.pyplot as pp

def main():
    rank = [i for i in range(1, 21)]
    frequency = [1861, 1666, 1638, 1132, 784, 768, 691, 681, 677, 661, 631, 534, 530, 518, 510, 473, 418, 379, 372, 357]
    pp.bar(rank, frequency)
    pp.xticks([1, 5, 10, 15, 20])
    pp.xlabel('Rank')
    pp.ylabel('Word count')
    pp.title('Zipf distribution for 20 most frequent words in $\it{dicta}$')
    pp.savefig('PNGs/Zipf.png')
    pp.show()

if __name__ == '__main__':
    main()
