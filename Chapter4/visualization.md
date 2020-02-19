---
author: Paul Evans
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
date: February 6-16, 2020
title: Stylometry
subtitle: Simplified two-dimensional visualization
---
Visualizing data from the first- and second- recension *dicta*
(excluding the *dicta* from *de Penitentia*) in a simplified
two-dimensional form is a useful first step toward understanding
how this kind of stylometric analysis works in practice.[^z1]

*In* is the most frequently occurring word in the *dicta*. There
are 1,450 occurrences of *in* out of 56,713 words in the first-recension
*dicta* (2.56%). There are 411 occurrences of *in* out of 14,255
words in the second-recension *dicta* (2.88%). The mean frequency
of occurrence of *in* for the combined first- and second-recension
*dicta* is therefore 1,861 occurrences out of 70,968 words (2.62%).
*In* occurs 2.50% less frequently than the mean in the first-recension
*dicta*, but 9.95% more frequently than the mean in the second-recension
*dicta*. Because the first-recension *dicta* represent 79.9% of the
words in the combined total, we expect first-recension word frequencies
to be much closer to the mean.

*Non* is the second most frequently occurring word in the *dicta*.
There are 1,360 occurrences of *non* in the first-recension *dicta*
(2.40%). There are 306 occurrences of *non* in the second-recension
*dicta* (2.15%). The mean frequency of occurrence of *non* for the
combined first- and second-recension *dicta* is therefore 1,666
occurrences out of 70,968 words (2.35%). *Non* occurs 2.15% more
frequently than the mean in the first-recension *dicta*, but 8.56%
less frequently than the mean in the second-recension *dicta*.

*In* occurring 9.95% more frequently than the mean and *non* occurring
8.56% less frequently than the mean in the second-recension *dicta*
are unexpectedly large variations for such common words. (Such large
variations would be less surprising with uncommon words for which
small differences in count could result in a large differences in
percentage.)

We can graph the number of occurrences of *in* and *non* per 1,000
words in the first- and second-recension *dicta*, with the frequency
of *in* plotted along the horizontal x-axis, and the frequency of
*non* plotted along the vertical y-axis, to produce a simplified
visualization of the total variation between the two. Means are
provided for context: the vertical dashed line represents the mean
for the horizontal (*in*) axis, and the horizontal dashed line
represents the mean for the vertical (*non*) axis.

![Figure 0a updated 10 Feb 2020](PNGs/Figure_0_frequency_excluding_de_Pen.png)

Figure 0a introduces several conventions common to two-dimensional
graphical representations of word frequency data that readers will
encounter repeatedly throughout this chapter. The feature (in this
case the frequency of occurrence of the word *in*) that explains
more of the variation between the samples is plotted along the
horizontal x-axis, while the feature (in this case the frequency
of occurrence of the word *non*) that explains less of the variation
between the samples is plotted along the vertical y-axis. Although
this plot, produced by the Matplotlib Python two-dimensional plotting
library, is rectangular and the axes are approximately to scale,
most of the figures in this chapter were generated using stylo, an
R package for stylometric analysis, which outputs square plots.
Regardless of appearance, readers should bear in mind that the area
plotted is wider than it is tall, that is, that it always displays
greater variation between samples horizontally along the x-axis
than it does vertically along the y-axis.

Figure 0a plots the first- and second-recension values (labelled
R1 and R2 respectively), as well as the means (indicated by the
dashed lines), for the frequencies of *in* and *non* per 1,000
words. It is more statistically meaningful, however, to measure and
plot the differences between values and means in units of standard
deviations rather than frequency per 1,000 words. The difference
of a value from the mean divided by standard deviation is referred
to as the value's z-score. A value that has a difference of one
standard deviation from the mean is said to have a z-score of 1.0
or -1.0 depending on whether the value is greater or lesser than
the mean. It is appropriate in this context to use the formula for
population rather than sample standard deviation,[^z2] because the
data we have represents the totality of known words attributed to
Gratian. The formula used to calculate the population standard
deviation is:

$\sigma=\sqrt{\frac{1}{N}\sum_{i=1}^N(x_i-\mu)^2}$

The formula is somewhat daunting notationally, but it is not difficult
to calculate the result. First, we calculate the squared deviations
from the mean for the frequency of *in* in the first-recension
*dicta*:

$(x_1-\mu)^2 = (25.5673 - 26.2231)^2 = (-0.6558)^2 = 0.4300$,

and for the frequency of *in* in the second-recension *dicta*:

$(x_2-\mu)^2 = (28.8320 - 26.2231)^2 = (2.6089)^2 = 6.8064$.

We then sum (as indicated by $\sum$) the two squared deviations
from the mean, divide the sum by their number ($N = 2$), and take
the square root of the quotient:

$\sigma =
\sqrt{\frac{1}{2}(0.4300 + 6.8064)} =
\sqrt{\frac{1}{2}(7.2364)} =
\sqrt{3.6182} =
1.9022$

The units of $\sigma$ are the same as those used to calculate the
mean, in this case, the frequency of occurrence of a word per 1,000
words.

For the frequency of *in* in the first-recension *dicta*:

$z =
\frac{x_1 - \mu}{\sigma} =
\frac{25.5673 - 26.2231}{1.9022} =
\frac{-0.6558}{1.9022} =
-0.3447$

and for the frequency of *in* in the second-recension *dicta*:

$z =
\frac{x_2 - \mu}{\sigma} =
\frac{28.8320 - 26.2231}{1.9022} =
\frac{2.6089}{1.9022} =
1.3716$

![Figure 0b updated 10 Feb 2020[^z3]](PNGs/Figure_0_z-score_excluding_de_Pen.png)

Labels on the axes of the plot refer to standard deviations (values
of z) away from the mean (represented by the dashed lines).

The technique of plotting word frequency data by z-score is known
as Burrows's Delta, after John F. Burrows (d.2019) of the University
of Newcastle, Australia, who first proposed the metric in 2001. It
has the advantage of making the statistical significance of plotted
data apparent in a way that plotting raw frequency data does not.
Burrows's Delta is one of a number of distance methods of authorship
attribution, but has the particular advantage of being widely
accepted in the scholarly literature of the field of computational
linguistics.

Figures 0a and 0b represents the axes as orthogonal (perpendicular)
to one another. Although doing so is acceptable as a first-order
approximation in a simplified representation of this kind, plotting
the values along orthogonal axes invokes an implicit assumption
that the word frequencies (in this case, of *in* and *non*) are
completely independent of one another, i.e., that there is no
correlation or covariance relationship between the words' frequency
of occurrence in the samples. This is not necessarily the case, and
an advanced technique introduced below, principal component analysis
(PCA), handles this problem in a more sophisticated way.

Now, we are obviously not going to make an attribution of authorship
based on the frequencies of only two function words.

Increasing the number of function words for which one collects
frequency data increases the accuracy of stylometric analysis, up
to a point. There is, however, a limit to the marginal value of
each additional word included in an analysis, for two reasons. The
first reason is that word frequencies in a sample of text tail off
approximately according to an observed empirical relationship known
as Zipf’s law, after American quantitative linguist George Kingsley
Zipf (d.1950), who first published an extended discussion of the
relationship. (Zipf did not apparently claim to have discovered the
relationship himself.) If the words in a sample of text are
rank-ordered from most to least frequent, Zipf’s laws posits that,
as a first-order approximation, the frequency of each word will be
1/N times that of the most frequent word, where N is the rank.[^z4]
In other words, the theoretical Zipf distribution predicts that the
frequency of the second most frequent word in a sample of text
should be one half that of the most frequent word, the frequency
of the third most frequent word should be one third that of the
most frequent word, and so on.

(See Figure Za below. The theoretical Zipf distribution plotted in
Figures Za and Zb has been scaled to facilitate direct comparison
with the actual data from the first- and second-recension *dicta*
plotted in Figures Zc and Zd. In all four plots, the first data
point has a rank of 1 and a frequency of 1861, corresponding to the
1,861 occurrences of the most frequent word *in* in the *dicta*.)

![Figure Za updated 16 Feb 2020](PNGs/Figure_Z_theoretical_bar.png)

Zipf's law can be restated with greater mathematical precision by
noting that the relationship of the logarithm of rank to the logarithm
of frequency is linear, with a slope of -1.0 corresponding to a
tail-off of 1/N. (See Figure Zb)[^z5]

"we have found a clearcut correlation between the number of different
words in the *Ulysses* and the frequency of their usage, in the
sense that they approximate the simple equation of an equalateral
hyperbola: r × f = C in which *r* refers to the word's rank in the
*Ulysses* and *f* to its frequency of occurrence (as we ignore for
the present the size of C)."[@zipf_human_1949, 24]

![Figure Zb updated 16 Feb 2020](PNGs/Figure_Z_theoretical_log-log_scatter.png)

Zipf used word frequencies hand-tabulated from James Joyce's *Ulysses*
as the data set for his exploration of the relationship, and it
turns out that for English, the 1/N relationship holds up reasonably
well.[^z7] The reader, however, already has enough data to question
whether the relationship holds up as well for Gratian's Latin as
it does for Joyce's English, since the frequency of *non*, the
second most frequent word in the first- and second-recension *dicta*,
is 0.8952 times that of *in* rather than 0.5000 as Zipf's law
predicts. In reality, then, the word frequencies for the first- and
second-recension *dicta* do not appear to drop off nearly as sharply
as the simplistic 1/N formulation of Zipf's law would predict.

Figure Zc below plots the actual rank-frequency distribution of the
twenty most frequent words (MFWs) in the first- and second-recension
*dicta*: *in* (1861), *non* (1666), *et* (1638), *est* (1132),
*quod* (784), *de* (768), *unde* (691), *ad* (681), *qui* (677),
*sed* (661), *uel* (631), *ut* (534), *cum* (530), *autem* (518),
*si* (510), *a* (473), *ex* (418), *sunt* (379), *uero* (372), and
*enim* (357).

![Figure Zc updated 16 Feb 2020](PNGs/Figure_Z_actual_bar.png)

Plotting the data from Figure Zc on logarithmic axes and performing
least-squares linear regression analysis lets us calculate the
slope, -0.5923, for the rank-frequency tail-off of the twenty most
frequent words from the first- and second-recension *dicta*. (See
Figure Zd below.) Transposing that result back into the linear (as
opposed to logarithmic) frame of reference used in Figure Zc, the
expression 1/N^(0.5923)^ yields a good (though not perfect) fit to
the actual rank-frequency data.

![Figure Zd updated 16 Feb 2020](PNGs/Figure_Z_actual_log-log_scatter.png)

The second reason that there is a limit to the marginal value of
each additional word included in stylometric analysis is that as
the wordlist extends downward, the mix shifts from disproportionately
function words to disproportionately content words. The twenty most
frequent words in the first- and second-recension *dicta* are *in*,
*non*, *et*, *est*, *quod*, *de*, *unde*, *ad*, *qui*, *sed*, *uel*,
*ut*, *cum*, *autem*, *si*, *a*, *ex*, *sunt*, *uero*, and *enim*.
Sixteen out of the first twenty are function words potentially
suitable for use in stylometric analysis,[^z8] but if we want to
use somewhere in the neighborhood of fifty function words for
stylometric analysis, we will have to reach all the way down to the
240th most frequent word to populate the wordlist.

[^z1]: Including the *dicta* from *de Penitentia* distorts the
results of the analysis, because out of the 10,081 words of the
vulgate version of the *de Pen.* *dicta*, only 556 were added or
changed between the first and second recensions of the *Decretum*.

[^z2]: The formula for sample standard deviation is:

    $s=\sqrt{\frac{1}{N-1}\sum_{i=1}^N(x_i-\bar{x})^2}$

[^z3]: Is standard deviation measuring anything here other than the
fact that the R1 sample is 3.9785 times the size of the R2 sample?

    $0.3447\times\frac{56713}{14255} = 0.3447\times3.9785 = 1.3756$

[^z4]: @zipf_human_1949, 73-131. Zipf himself referred to the
relationship as "the law of diminishing returns of words". Zipf
previously discussed the relationship in @zipf_psycho-biology_1935.
[UCSD Geisel Library has a copy, currently (18 February 2020)
unavailable, of a 1965 MIT Press reprint of this book.] Zipf expressed
the relationship as r × f = C.

[^z5]: Note that the base of the logarithms does not matter (as
long as they are the same for both axes). Regardless of whether we
take base e (natural) or base 10 logarithms of rank and word count,
the slopes will be the same: -1.000 for the theoretical Zipf
distribution of word frequencies, and (as we shall see) -0.5923 for
the actual frequencies of the twenty most frequent words in the
first- and second-recension *dicta*.

[^z7]: See @zipf_human_1949, 23-52, for Zipf's discussion of the
rank-frequency distribution of words in Joyce's *Ulysses*.

[^z8]: **Even if we have to later discard *si* for other reasons.**
