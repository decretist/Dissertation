#!/usr/local/bin/python3
#
# Paul Evans (10evans@cua.edu)
# 13-20 February 2020
#
import math
import matplotlib.pyplot as pp
import statistics

def regression_slope(data_points):
    n = len(data_points)
    x_values, y_values = zip(*data_points)
    x_bar = statistics.mean(x_values)
    y_bar = statistics.mean(y_values)
    xy_sum = 0
    x_squared_sum = 0
    for i in range(n):
        xy_sum += x_values[i] * y_values[i]
        x_squared_sum += x_values[i] ** 2
    return (xy_sum - n * x_bar * y_bar) / (x_squared_sum - n * x_bar ** 2)

def plot_regression(data_points):
    x_values, y_values = zip(*data_points)
    x_bar = statistics.mean(x_values)
    y_bar = statistics.mean(y_values)
    slope = regression_slope(data_points)
    x_values = [0, max(x_values)]
    y_values = []
    for x in x_values:
        y_values.append(y_bar + slope * (x - x_bar))
    pp.plot(x_values, y_values)
    return slope

def plot_data_bar(data_points):
    x_values, y_values = zip(*data_points)
    pp.bar(x_values, y_values)
    pp.xticks([5, 10, 15, 20])
    pp.xlabel('rank')
    pp.ylabel('word count')

def plot_actual_data_bar(word_pair_dict):
    words = list(word_pair_dict.keys())
    xy_values = list(word_pair_dict.values())
    x_values, y_values = zip(*xy_values)
    pp.figure(figsize=[6.4, 6.4]) # default = [6.4, 4.8]
    pp.bar(x_values, y_values)
    pp.axis([0,21,0,2000])
    pp.xticks(x_values, words, rotation='vertical')
    pp.ylabel('word count')

def plot_data_scatter(data_points):
    x_values, y_values = zip(*data_points)
    pp.scatter(x_values, y_values)
    pp.xlabel('$log_{e}$ rank')
    pp.ylabel('$log_{e}$ word count')

def logify(data_points):
    x_tmp, y_tmp = zip(*data_points)
    x_values = list(x_tmp)
    y_values = list(y_tmp)
    x_log = [math.log(x) for x in x_values]
    y_log = [math.log(y) for y in y_values]
    return list(zip(x_log, y_log))

def main():
    scale = 1861 # scaling factor
    #
    # theoretical Zipf distribution for 20 most frequent words (MFWs)
    # (bar plot)
    #
    x_values = [x for x in range(1, 21)]
    y_values = [(1 / x) * scale for x in x_values]
    plot_data_bar(list(zip(x_values, y_values)))
    pp.title('theoretical Zipf distribution for 20 MFWs')
    pp.savefig('../PNGs/Figure_Z_theoretical_bar.png')
    pp.show()
    #
    # theoretical Zipf distribution for 20 MFWs
    # (log-log scatter plot)
    #
    plot_data_scatter(logify(list(zip(x_values, y_values))))
    slope = plot_regression(logify(list(zip(x_values, y_values))))
    pp.title(f'theoretical Zipf distribution for 20 MFWs\n(log-log, slope = {slope:.4f})')
    pp.savefig('../PNGs/Figure_Z_theoretical_log-log_scatter.png')
    pp.show()
    #
    # rank-frequency data for 20 MFWs from R1 and R2 dicta
    #
    words = ['in', 'non', 'et', 'est', 'quod', 'de', 'unde', 'ad', 'qui', 'sed', 'uel', 'ut', 'cum', 'autem', 'si', 'a', 'ex', 'sunt', 'uero', 'enim']
    pairs = [(1, 1861), (2, 1666), (3, 1638), (4, 1132), (5, 784), (6, 768), (7, 691), (8, 681), (9, 677), (10, 661), (11, 631), (12, 534), (13, 530), (14, 518), (15, 510), (16, 473), (17, 418), (18, 379), (19, 372), (20, 357)]
    #
    # actual distribution for 20 MFWs from R1 and R2 dicta
    # (bar plot)
    #
    plot_actual_data_bar(dict(zip(words, pairs)))
    pp.title('actual distribution for 20 MFWs from R1 and R2 $\it{dicta}$')
    pp.savefig('../PNGs/Figure_Z_actual_bar.png')
    pp.show()
    #
    # actual distribution for 20 MFWs from R1 and R2 dicta
    # (log-log scatter plot)
    #
    plot_data_scatter(logify(pairs))
    slope = plot_regression(logify(pairs))
    pp.title('actual distribution for 20 MFWs from R1 and R2 $\it{dicta}$\n(log-log, slope = ' + f'{slope:.4f})')
    pp.savefig('../PNGs/Figure_Z_actual_log-log_scatter.png')
    pp.show()
    #
    # theoretical 1/N^0.5923 distribution for 20 MFWs
    # (bar plot)
    #
    x_values = [x for x in range(1, 21)]
    y_values = [(1 / pow(x, -slope)) * scale for x in x_values]
    plot_data_bar(list(zip(x_values, y_values)))
    pp.title('theoretical $1/N^{0.5923}$ distribution for 20 MFWs')
    pp.show()
    #
    # theoretical 1/N^0.5923 distribution for 20 MFWs
    # (log-log scatter plot)
    #
    plot_data_scatter(logify(list(zip(x_values, y_values))))
    slope = plot_regression(logify(list(zip(x_values, y_values))))
    pp.title('theoretical $1/N^{0.5923}$ distribution for 20 MFWs\n(log-log, slope = ' + f'{slope:.4f})')
    pp.show()

if __name__ == "__main__":
    main()

