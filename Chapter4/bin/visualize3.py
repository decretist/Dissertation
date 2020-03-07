#!/usr/local/bin/python3
#
# Paul Evans (10evans@cua.edu)
# 1-3 March 2020
# 6-11 February 2020
# 22 January 2020
#
import math
import matplotlib.pyplot as pp
import statistics

def stats(word, data):
    frequency_A = (data[word][1] / data['all'][1]) * 1000
    frequency_B = (data[word][2] / data ['all'][2]) * 1000
    frequency_C = (data[word][3] / data ['all'][3]) * 1000
    frequency_values = [frequency_A, frequency_B, frequency_C]
    frequency_mean = statistics.mean(frequency_values)
    standard_deviation = statistics.stdev(frequency_values)
    filler = f'occurrences of \'{word}\' per 1,000 words'
    print(f'{frequency_A:7.4f} {filler} (R1 dicta)')
    print(f'{frequency_B:7.4f} {filler} (R2 dicta)')
    print(f'{frequency_C:7.4f} {filler} (Other)')
    print(f'{frequency_mean:7.4f} {filler} (mean)')
    print(f'{standard_deviation:7.4f} {filler} (standard deviation)')
    return (frequency_A, frequency_B, frequency_C, frequency_mean, standard_deviation)

def f_plot(x_word, x_frequencies, y_word, y_frequencies):
    # frequency view
    value_x_A,value_x_B,value_x_C,frequency_x_mean,standard_deviation_x = x_frequencies
    value_y_A,value_y_B,value_y_C,frequency_y_mean,standard_deviation_y = y_frequencies
    pp.axis([frequency_x_mean - 2 * standard_deviation_x,
        frequency_x_mean + 2 * standard_deviation_x,
        frequency_y_mean - 2 * standard_deviation_y,
        frequency_y_mean + 2 * standard_deviation_y])
    pp.axhline(frequency_y_mean,linestyle='dashed')
    pp.axvline(frequency_x_mean, linestyle='dashed')
    pp.xlabel(f'frequency of occurrence of \'{x_word}\' per 1,000 words')
    pp.ylabel(f'frequency of occurrence of \'{y_word}\' per 1,000 words')
    # common
    pp.annotate(
        f'R1 dicta ({value_x_A:.3f}, {value_y_A:.3f})',
        (value_x_A, value_y_A),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )
    pp.annotate(
        f'R2 dicta ({value_x_B:.3f}, {value_y_B:.3f})',
        (value_x_B, value_y_B),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )
    pp.annotate(
        f'Other ({value_x_C:.3f}, {value_y_C:.3f})',
        (value_x_C, value_y_C),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )
    x_values = [value_x_A, value_x_B, value_x_C]
    y_values = [value_y_A, value_y_B, value_y_C]
    pp.scatter(x_values, y_values)
    pp.title('(frequency view)')
    # pp.savefig('../PNGs/Figure_ABC_frequency')
    pp.gcf().canvas.set_window_title('Figure 0')
    pp.show()

def z_plot(x_word, x_frequencies, y_word, y_frequencies):
    # z-score view
    frequency_x_A,frequency_x_B,frequency_x_C,frequency_x_mean,standard_deviation_x = x_frequencies
    frequency_y_A,frequency_y_B,frequency_y_C,frequency_y_mean,standard_deviation_y = y_frequencies
    value_x_A = (frequency_x_A - frequency_x_mean) / standard_deviation_x
    value_y_A = (frequency_y_A - frequency_y_mean) / standard_deviation_y
    value_x_B = (frequency_x_B - frequency_x_mean) / standard_deviation_x
    value_y_B = (frequency_y_B - frequency_y_mean) / standard_deviation_y
    value_x_C = (frequency_x_C - frequency_x_mean) / standard_deviation_x
    value_y_C = (frequency_y_C - frequency_y_mean) / standard_deviation_y
    pp.axis([-2, 2, -2, 2])
    pp.axhline(linestyle='dashed')
    pp.axvline(linestyle='dashed')
    pp.xticks([-1, 0, 1])
    pp.yticks([-1, 0, 1])
    pp.xlabel(f'\'{x_word}\'')
    pp.ylabel(f'\'{y_word}\'', rotation='horizontal')
    # common
    pp.annotate(
        f'R1 dicta ({value_x_A:.3f}, {value_y_A:.3f})',
        (value_x_A, value_y_A),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )
    pp.annotate(
        f'R2 dicta ({value_x_B:.3f}, {value_y_B:.3f})',
        (value_x_B, value_y_B),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )
    pp.annotate(
        f'Other ({value_x_C:.3f}, {value_y_C:.3f})',
        (value_x_C, value_y_C),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )
    x_values = [value_x_A, value_x_B, value_x_C]
    y_values = [value_y_A, value_y_B, value_y_C]
    pp.scatter(x_values, y_values)
    pp.title('(z-score view)')
    # pp.savefig('../PNGs/Figure_ABC_z-score')
    pp.gcf().canvas.set_window_title('Figure 0')
    pp.show()

def main():
    frequencies = {
        'all': [84654, 56713, 14255, 13686],
        'in':  [ 2187,  1450,   411,   326],
        'et':  [ 1968,  1293,   345,   249],
        'non': [ 1960,  1360,   306,   294],
    }
    f_plot('in', stats('in', frequencies), 'non', stats('non', frequencies))
    z_plot('in', stats('in', frequencies), 'non', stats('non', frequencies))

if __name__ == '__main__':
    main()
