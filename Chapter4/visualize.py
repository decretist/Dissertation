#!/usr/local/bin/python3
#
# Paul Evans (10evans@cua.edu
# 6 February 2020
# 22 January 2020
#
import math
import matplotlib.pyplot as pp
import statistics

def standard_deviation(values, mu):
    sum = 0
    for value in values:
        sum += (value - mu) ** 2
    return(math.sqrt(sum / len(values)))

de_pen = False
frequency_view = False

if de_pen:
    # number of words in R1 and R2 dicta
    words_r1 = 66238
    words_r2 = 14811
    # number of occurrences of 'in' and 'non' in R1 and R2 dicta
    occurrences_in_r1 = 1682
    occurrences_in_r2 = 431
    occurrences_non_r1 = 1622
    occurrences_non_r2 = 314
else:
    # number of words in R1 and R2 dicta
    words_r1 = 56713
    words_r2 = 14255
    # number of occurrences of 'in' and 'non' in R1 and R2 dicta
    occurrences_in_r1 = 1450
    occurrences_in_r2 = 411
    occurrences_non_r1 = 1360
    occurrences_non_r2 = 306

# frequency of occurrence of 'in' per 1000 words
frequency_in_r1 = (occurrences_in_r1 / words_r1) * 1000
frequency_in_r2 = (occurrences_in_r2 / words_r2) * 1000
frequency_in_values = [frequency_in_r1, frequency_in_r2]
frequency_in_mean = ((occurrences_in_r1 + occurrences_in_r2) / (words_r1 + words_r2)) * 1000
standard_deviation_in = statistics.pstdev(frequency_in_values, mu=frequency_in_mean)
standard_deviation_in_hp = standard_deviation(frequency_in_values, frequency_in_mean)
percentage_in_r1 = ((frequency_in_r1 - frequency_in_mean) / frequency_in_mean) * 100
percentage_in_r2 = ((frequency_in_r2 - frequency_in_mean) / frequency_in_mean) * 100
if de_pen: print('(including de Pen.)')
else: print('(excluding de Pen.)')
string_in = 'occurrences of  \'in\' per 1,000 words'
print(f'{frequency_in_r1:6.3f} {string_in} (R1)')
print(f'{frequency_in_r2:6.3f} {string_in} (R2)')
print(f'{frequency_in_mean:6.3f} {string_in} (mean)')
print(f'{standard_deviation_in:6.4f} {string_in} (standard deviation: pstdev)')
print(f'{standard_deviation_in_hp:6.4f} {string_in} (standard deviation: HP 48GX)')
if percentage_in_r1 > 0: more_or_less = 'more'
else: more_or_less = 'less'
print(f'\'in\' occurs {abs(percentage_in_r1):.2f}% {more_or_less} frequently in R1 than in mean')
if percentage_in_r2 > 0: more_or_less = 'more'
else: more_or_less = 'less'
print(f'\'in\' occurs {abs(percentage_in_r2):.2f}% {more_or_less} frequently in R2 than in mean')

# frequency of occurrence of 'non' per 1000 words
frequency_non_r1 = (occurrences_non_r1 / words_r1) * 1000
frequency_non_r2 = (occurrences_non_r2 / words_r2) * 1000
frequency_non_values = [frequency_non_r1, frequency_non_r2]
frequency_non_mean = ((occurrences_non_r1 + occurrences_non_r2) / (words_r1 + words_r2)) * 1000
standard_deviation_non = statistics.pstdev(frequency_non_values, mu=frequency_non_mean)
standard_deviation_non_hp =  standard_deviation(frequency_non_values, frequency_non_mean)
percentage_non_r1 = ((frequency_non_r1 - frequency_non_mean) / frequency_non_mean) * 100
percentage_non_r2 = ((frequency_non_r2 - frequency_non_mean) / frequency_non_mean) * 100
string_non = 'occurrences of \'non\' per 1,000 words'
print(f'{frequency_non_r1:6.3f} {string_non} (R1)')
print(f'{frequency_non_r2:6.3f} {string_non} (R2)')
print(f'{frequency_non_mean:6.3f} {string_non} (mean)')
print(f'{standard_deviation_non:6.4f} {string_non} (standard deviation: pstdev)')
print(f'{standard_deviation_non_hp:6.4f} {string_non} (standard deviation: HP 48GX)')
if percentage_non_r1 > 0: more_or_less = 'more'
else: more_or_less = 'less'
print(f'\'non\' occurs {abs(percentage_non_r1):.2f}% {more_or_less} frequently in R1 than in mean')
if percentage_non_r2 > 0: more_or_less = 'more'
else: more_or_less = 'less'
print(f'\'non\' occurs {abs(percentage_non_r2):.2f}% {more_or_less} frequently in R2 than in mean')

if frequency_view:
    value_in_r1 = frequency_in_r1
    value_non_r1 = frequency_non_r1
    value_in_r2 = frequency_in_r2
    value_non_r2 = frequency_non_r2
    pp.axis([frequency_in_mean - 2 * standard_deviation_in,
        frequency_in_mean + 2 * standard_deviation_in,
        frequency_non_mean - 2 * standard_deviation_non,
        frequency_non_mean + 2 * standard_deviation_non])
    pp.axhline(frequency_non_mean,linestyle='dashed')
    pp.axvline(frequency_in_mean, linestyle='dashed')
    pp.xlabel('frequency of occurrence of $\it{in}$ per 1,000 words')
    pp.ylabel('frequency of occurrence of $\it{non}$ per 1,000 words')
else: #standard deviation view
    value_in_r1 = (frequency_in_r1 - frequency_in_mean) / standard_deviation_in
    value_non_r1 = (frequency_non_r1 - frequency_non_mean) / standard_deviation_non
    value_in_r2 = (frequency_in_r2 - frequency_in_mean) / standard_deviation_in
    value_non_r2 = (frequency_non_r2 - frequency_non_mean) / standard_deviation_non
    pp.axis([-2, 2, -2, 2])
    pp.axhline(linestyle='dashed')
    pp.axvline(linestyle='dashed')
    pp.xticks([-1, 0, 1])
    pp.yticks([-1, 0, 1])
    pp.xlabel('$\it{in}$')
    pp.ylabel('$\it{non}$', rotation='horizontal')

pp.annotate(
    f'R1 ({value_in_r1:.3f}, {value_non_r1:.3f})',
    (value_in_r1, value_non_r1),
    textcoords="offset points",
    xytext=(0,10),
    ha='center'
)
pp.annotate(
    f'R2 ({value_in_r2:.3f}, {value_non_r2:.3f})',
    (value_in_r2, value_non_r2),
    textcoords="offset points",
    xytext=(0,10),
    ha='center'
)
in_values = [value_in_r1, value_in_r2]
non_values = [value_non_r1, value_non_r2]
pp.scatter(in_values, non_values)
if frequency_view:
    title_string = '(frequency view, '
    filename = './PNGs/Figure_0_frequency_'
else:
    title_string = '(z-score view, '
    filename = './PNGs/Figure_0_z-score_'
if de_pen:
    title_string += 'including $\it{de Pen.}$)'
    filename += 'including_de_Pen.png'
else:
    title_string += 'excluding $\it{de Pen.}$)'
    filename += 'excluding_de_Pen.png'
pp.title(title_string)
# pp.savefig(filename)
pp.gcf().canvas.set_window_title('Figure 0')
pp.show()
