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

def pstdev(data, **kwargs):
    '''Temporary replacement for statistics.pstdev()'''
    mu = None
    if 'mu' in kwargs: mu = kwargs['mu'] # type check: int, float, or None
    if mu == None: mu = statistics.mean(data)
    sum = 0
    for i in range(len(data)):
        sum += (data[i] - mu) ** 2
    return(math.sqrt(sum / len(data)))

def stats(word, data):
    frequency_mean = (data[word][0] / data['all'][0]) * 1000
    frequency_r1 = (data[word][1] / data['all'][1]) * 1000
    frequency_r2 = (data[word][2] / data ['all'][2]) * 1000
    frequency_dP = (data[word][3] / data ['all'][3]) * 1000
    frequency_values = [frequency_r1, frequency_r2]
    standard_deviation = pstdev(frequency_values, mu=frequency_mean)
    filler = f'occurrences of \'{word}\' per 1,000 words'
    print(f'{frequency_r1:7.4f} {filler} (R1)')
    print(f'{frequency_r2:7.4f} {filler} (R2)')
    print(f'{frequency_dP:7.4f} {filler} (de Pen.)')
    print(f'{frequency_mean:7.4f} {filler} (mean)')
    print(f'{standard_deviation:7.4f} {filler} (standard deviation)')
    percentage(word, 'R1', frequency_r1, frequency_mean)
    percentage(word, 'R2', frequency_r2, frequency_mean)
    percentage(word, 'de Pen.', frequency_dP, frequency_mean)
    return (frequency_r1, frequency_r2, frequency_dP, frequency_mean, standard_deviation)

def f_plot(x_word, x_frequencies, y_word, y_frequencies):
    # frequency view
    value_x_r1,value_x_r2,value_x_dP,frequency_x_mean,standard_deviation_x = x_frequencies
    value_y_r1,value_y_r2,value_y_dP,frequency_y_mean,standard_deviation_y = y_frequencies
    pp.axis([frequency_x_mean - 5 * standard_deviation_x,
        frequency_x_mean + 5 * standard_deviation_x,
        frequency_y_mean - 5 * standard_deviation_y,
        frequency_y_mean + 5 * standard_deviation_y])
    pp.axhline(frequency_y_mean,linestyle='dashed')
    pp.axvline(frequency_x_mean, linestyle='dashed')
    pp.xlabel(f'frequency of occurrence of \'{x_word}\' per 1,000 words')
    pp.ylabel(f'frequency of occurrence of \'{y_word}\' per 1,000 words')
    # common
    pp.annotate(
        f'R1 ({value_x_r1:.3f}, {value_y_r1:.3f})',
        (value_x_r1, value_y_r1),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )
    pp.annotate(
        f'R2 ({value_x_r2:.3f}, {value_y_r2:.3f})',
        (value_x_r2, value_y_r2),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )
    pp.annotate(
        f'de Pen. ({value_x_dP:.3f}, {value_y_dP:.3f})',
        (value_x_dP, value_y_dP),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )
    x_values = [value_x_r1, value_x_r2, value_x_dP]
    y_values = [value_y_r1, value_y_r2, value_y_dP]
    pp.scatter(x_values, y_values)
    pp.title('(frequency view)')
    # pp.savefig('../PNGs/Figure_0_frequency')
    pp.gcf().canvas.set_window_title('Figure 0')
    pp.show()

def z_plot(x_word, x_frequencies, y_word, y_frequencies):
    # z-score view
    frequency_x_r1,frequency_x_r2,frequency_x_dP,frequency_x_mean,standard_deviation_x = x_frequencies
    frequency_y_r1,frequency_y_r2,frequency_y_dP,frequency_y_mean,standard_deviation_y = y_frequencies
    value_x_r1 = (frequency_x_r1 - frequency_x_mean) / standard_deviation_x
    value_y_r1 = (frequency_y_r1 - frequency_y_mean) / standard_deviation_y
    value_x_r2 = (frequency_x_r2 - frequency_x_mean) / standard_deviation_x
    value_y_r2 = (frequency_y_r2 - frequency_y_mean) / standard_deviation_y
    value_x_dP = (frequency_x_dP - frequency_x_mean) / standard_deviation_x
    value_y_dP = (frequency_y_dP - frequency_y_mean) / standard_deviation_y
    pp.axis([-5, 5, -5, 5])
    pp.axhline(linestyle='dashed')
    pp.axvline(linestyle='dashed')
    pp.xticks([-2.5, 0, 2.5])
    pp.yticks([-2.5, 0, 2.5])
    pp.xlabel(f'\'{x_word}\'')
    pp.ylabel(f'\'{y_word}\'', rotation='horizontal')
    # common
    pp.annotate(
        f'R1 ({value_x_r1:.3f}, {value_y_r1:.3f})',
        (value_x_r1, value_y_r1),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )
    pp.annotate(
        f'R2 ({value_x_r2:.3f}, {value_y_r2:.3f})',
        (value_x_r2, value_y_r2),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )
    pp.annotate(
        f'de Pen. ({value_x_dP:.3f}, {value_y_dP:.3f})',
        (value_x_dP, value_y_dP),
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )
    x_values = [value_x_r1, value_x_r2, value_x_dP]
    y_values = [value_y_r1, value_y_r2, value_y_dP]
    pp.scatter(x_values, y_values)
    pp.title('(z-score view)')
    # pp.savefig('../PNGs/Figure_0_z-score')
    pp.gcf().canvas.set_window_title('Figure 0')
    pp.show()

def percentage(word, title, frequency, mean):
    percentage = ((frequency - mean) / mean) * 100
    if percentage > 0: more_or_less = 'more'
    else: more_or_less = 'less'
    print(f'\'{word}\' occurs {abs(percentage):.2f}% {more_or_less} frequently in {title} than in mean')

def main():
    frequencies = {
        # include frequency data for 'de'
        'all': [84654, 56713, 14255,  9525],
        'in':  [ 2187,  1450,   411,   232],
        'et':  [ 1968,  1293,   345,   249],
        'non': [ 1960,  1360,   306,   262],
        # 'de':  [     ,      ,      ,      ]
    }
    f_plot('in', stats('in', frequencies), 'non', stats('non', frequencies))
    z_plot('in', stats('in', frequencies), 'non', stats('non', frequencies))
    f_plot('in', stats('in', frequencies), 'et', stats('et', frequencies))
    z_plot('in', stats('in', frequencies), 'et', stats('et', frequencies))
    f_plot('et', stats('et', frequencies), 'non', stats('non', frequencies))
    z_plot('et', stats('et', frequencies), 'non', stats('non', frequencies))

if __name__ == '__main__':
    main()
