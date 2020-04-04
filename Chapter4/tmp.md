---
author: Paul Evans
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
date: 3-5 April 2020
suppress-bibliography: false
title: Stylometry
subtitle: Zipf's law
---
Now, we are obviously not going to make an attribution of authorship
based on the frequencies of only two function words. Increasing the
number of function words for which one collects frequency data
increases the accuracy of stylometric analysis, up to a point. There
is, however, a limit to the marginal value of each additional word
included in an analysis, for two reasons. The first reason is that
word frequencies in a corpus of text tail off approximately as 1/N,
where N is the word's rank. As a consequence, assuming words are
weighted in proportion to their frequency of occurrence in the
corpus, every marginal word has less value as evidence than the
word before it. Some stylometric techniques, such as Burrows's
Delta, weight each word from a corpus of texts equally, but such
choices need to be made with an informed awareness of the trade-offs
involved. The second reason is that every marginal word is less
likely to be a function word, and more likely to be a content word.
Twenty-four out of the thirty most frequent words from Gratian's
*dicta* are function words potentially suitable for use in stylometric
analysis, but only 64 out of the 250 most frequent words.

### Zipf's law

The observed empirical relationship that word frequencies in a
corpus of text tail off approximately as 1/N is known as Zipf’s
law, after American quantitative linguist George Kingsley Zipf
(d.1950). Though he does not seem to have claimed discovery, Zipf
published the first extended discussions of the phenomenon.[^10]
**The 1/N rank-frequency distribution of words in a corpus of any
language is not merely a curiosity, but rather provides a general
background of "orderliness" (Zipf's characterization) against which
variations in frequency of occurrence of individual words are both
detectable and meaningful. Thus it is worthwhile to discuss theoretical
predictions about the rank-frequency distribution of words in a
corpus, and to demonstrate that Gratian's *dicta* display the
expected orderliness of word distribution.**

If the words in a corpus of text are rank-ordered from most to least
frequent, Zipf’s laws posits that, as a first-order approximation,
the frequency of each word will be 1/N times that of the most
frequent word, where N is the rank. In other words, the theoretical
Zipf distribution predicts that the frequency of the second most
frequent word in a corpus of text should be one half that of the
most frequent word, the frequency of the third most frequent word
should be one third that of the most frequent word, and so on. (See
Figure Za below.) The theoretical Zipf distribution plotted in
Figures Za and Zb has been scaled to facilitate direct comparison
with actual data from Gratian's *dicta* plotted in Figures Zc and
Zd. In all four plots, the first data point has a rank of 1 and a
frequency of 2187, corresponding to the 2,187 occurrences of the
most frequent word *in* in the *dicta*.

![Figure Za updated 12 Mar 2020](PNGs/Figure_Za.png)

Zipf's law can be restated with greater mathematical precision by
noting that the relationship of the logarithm of rank to the logarithm
of frequency is linear, with a slope of -1.0 corresponding to a
tail-off of 1/N. (See Figure Zb)[^11]

![Figure Zb updated 12 Mar 2020](PNGs/Figure_Zb.png)

Figure Zc below plots the actual rank-frequency distribution of the
thirty most frequent words (MFWs) in Gratian's *dicta*: *in* (2187),
*et* (1968), *non* (1960), *est* (1327), *de* (925), *quod* (888),
*ad* (832), *qui* (812), *sed* (736), *unde* (732), *uel* (705),
*si* (669), *ut* (641), *cum* (589), *a* (588), *autem* (582), *ex*
(501), *sunt* (428), *enim* (424), *que* (423), *uero* (411), *etiam*
(405), *ab* (391), *ait* (349), *esse* (339), *ergo* (338), *quia*
(336), *item* (327), *per* (304), *nec* (293).

![Figure Zc updated 12 Mar 2020](PNGs/Figure_Zc.png)

Zipf used word frequencies hand-tabulated from James Joyce's *Ulysses*
as the data set for his exploration of the rank-frequency relationship,
and it turns out that for English, the 1/N formulation holds up
reasonably well.[^13] The rank-frequency relationship does not at
first appear to hold up as well for Gratian's Latin as it does for
Joyce's English, since the frequencies for the thirty most frequent
words of the *dicta* do not drop off as sharply as the simplistic
1/N formulation of Zipf's law would predict. The frequency of *et*,
the second most frequent word in Gratian's *dicta* is 0.8999 times
that of *in*, the most frequent word, rather than 0.5 as Zipf's law
would predict; and the frequency of *non*, the third most frequent
word, is 0.8962 rather than 0.3333.

Plotting the data from Figure Zc on logarithmic axes and performing
least-squares linear regression analysis lets us calculate the
slope, -0.6518, for the rank-frequency tail-off of the thirty most
frequent words from Gratian's *dicta*.[^14] (See Figure Zd below.)
Transposing that result back into the linear (as opposed to
logarithmic) frame of reference used in Figure Zc, the expression
1/N^(0.6518)^ yields a good (though not perfect) fit to the actual
rank-frequency data.

![Figure Zd updated 12 Mar 2020](PNGs/Figure_Zd.png)

![Figure Ze updated 12 Mar 2020](PNGs/Figure_Ze.png)

[^10]: @zipf_human_1949, 73-131. Zipf himself referred to the
relationship as "the law of diminishing returns of words". Zipf
previously discussed the relationship in @zipf_psycho-biology_1935,
39-48. Zipf expressed the relationship as $ab^2 = k$ (1935) and
r × f = C (1949).

[^11]: Note that the base of the logarithms does not matter (as
long as they are the same for both axes). Regardless of whether we
take base e (natural) or base 10 logarithms of rank and word count,
the slopes will be the same: -1.0 for the theoretical Zipf distribution
of word frequencies, and (as we shall see) -0.6518 for the actual
frequencies of the thirty most frequent words in Gratian's *dicta*.

[^13]: "we have found a clearcut correlation between the number of
different words in the *Ulysses* and the frequency of their usage,
in the sense that they approximate the simple equation of an
equilateral hyperbola: r × f = C in which *r* refers to the word's
rank in the *Ulysses* and *f* to its frequency of occurrence (as
we ignore for the present the size of C)." @zipf_human_1949, 24. See
@zipf_human_1949, 23-52, for Zipf's extended discussion of the
rank-frequency distribution of words in Joyce's *Ulysses*.

[^14]: $m = \frac{\sum{x_iy_i - n\bar{xy}}}{\sum{x_i^2 - n\bar{x}^2}}$ or:

    ~~~ {.python}
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
    ~~~

