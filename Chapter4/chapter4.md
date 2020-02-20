---
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
suppress-bibliography: false
title: Chapter 4
subtitle: Stylometry
abstract: |
  Since the discovery by Winroth in 1996 of a first recension of
  Gratian's *Decretum*, there has been scholarly controversy over
  whether the compiler of the first recension was the same person
  as the compiler of the second recension. Techniques for authorship
  attribution developed by researchers in the field of computation
  linguistics make it possible to approach this problem in a new
  way. Using the Stylometry with R package, I have analyzed those
  texts from the *Decretum* traditionally attributed to Gratian
  personally: the case statements and the *dicta*. Principal component
  analysis (PCA) of the frequencies of function words (prepositions
  and conjunctions) in the texts suggests that the author of the
  case statements was not the same person as the authors of either
  the first- or second-recension *dicta*. PCA also provides evidence
  concerning the first- and second-recension *dicta* that suggests
  they are the product of collaborative authorship rather than being
  the work of either one or two authors.
---
Twenty years ago, Anders Winroth announced his discovery of the
first recension of Gratian's *Decretum* at the Tenth International
Congress of Medieval Canon Law in Syracuse, New York. One of the
most important questions raised by that discovery is whether Gratian
1, the compiler of the first recension was the same person as Gratian
2, the compiler of the second recension. It does not appear that
the debate over authorship can be settled using currently available
evidence. The goal of my project is to find new evidence for the
authorship of case statements and *dicta* in Gratian's *Decretum*
using computational methods.[^1]

First I'm going to discuss in general terms the use of stylometry
for authorship attribution. Then, I'm going to discuss the methodology
and the software that I am using for this project. Finally, I am
going to show the results of stylometric analysis of the case
statements, the first-recension *dicta*, and the second-recension
*dicta* (first without, then with, the *dicta* from *de Penitentia*),
and discuss some possible interpretations of those results.

Stylometry is the measurement of style. "Style is a property of
texts constituted by an ensemble of formal features which can be
observed quantitatively or qualitatively." [@herrmann_revisiting_2015,
44] While style has both qualitative and quantitative aspects,
stylometry is concerned only with quantitative aspects of style.
One well-established use of stylometry is to attribute authorship.
And for the purpose of authorship attribution, the formal linguistic
features that stylometry measures are the frequencies of occurrence
of function words.

Linguists draw a distinction between function words and content
words. Function words are words like prepositions and conjunctions.
Content words are words like adjectives, nouns, and verbs. Function
words convey meaning by their use in grammatical structure. The
Latin conjunction "*sed*" doesn't mean anything by itself, but
rather it places two words or grammatical constructs into an
adversative relationship with each other.

Here's another way of thinking about the distinction: function words
are closed-class words and content words are open-class words.
Language-speaking communities can and do make up new adjectives and
nouns and verbs all the time; so content words are an open class
that can be added to at will. But new prepositions and conjunctions
are almost never added to a language, and they change very slowly
over time, if they change at all, and are therefore, for all practical
purposes, a closed, finite, class. In theory, that means that you
ought to be able to make a list of every function word in a language,
although in practice, that's not easy to do.

Evidence from experimental psychology suggests that both authors
and readers process function words at an subconscious level.
[@kestemont_function_2014] The frequency with which a given author
uses particular function words is therefore considered to be more
or less invariant, making it a reliable authorial signature.

### The Federalist (Hamilton and Madison)

Stylometric analysis of the frequency of functions words for the
purpose of attributing authorship has had a number of notable
successes. The validity of this approach for textual scholarship
was firmly established by the work of Frederick Mosteller and David
L. Wallace on the *Federalist Papers*. The authorship of 12 of the
*Federalist Papers*, 49-57 and 62-63, had been disputed since the
early 19th century, with competing claims advanced on behalf of
Alexander Hamilton and James Madison.[^f] In 1944, Douglass Adair,
using traditional scholarly methods, settled the dispute largely
to the satisfaction of early American historians, determining that
Madison was the author of all 12 of the disputed numbers.[^4] In
1964, Mosteller and Wallace confirmed Adair's findings by conducting
a stylometric analysis of the frequencies of 70 function words to
compare the 12 disputed numbers with numbers securely attributed
to Hamilton and Madison.[@mosteller_inference_1964]

![Federalist](JPGs/Federalist_CA_72_MFWs.jpg)

### Simplified two-dimensional visualization

Visualizing data from the first- and second- recension *dicta*
(excluding the *dicta* from *de Penitentia*) in a simplified
two-dimensional form is a useful first step toward understanding
how this kind of stylometric analysis works in practice.[^6]

+ if a *dictum* is listed in Winroth's appendix as being in the
first recension of the *Decretum*, and as not having been added to
or changed in the second recension, it is included in the first
recension sample.

+ if a *dictum* is in the MGH e-text of the 1879 Friedberg edition,
and is not listed in Winroth's appendix as being in the first
recension, in either unmodified or modified form, it is included
in the second recension sample.

+ if a *dictum* is listed Winroth's appendix as being in the first
recension, but as having been added to or changed in the second
recension, words indicated by the appendix are included in the first
recension sample, while words in the e-text of Friedberg not
corresponding to the words indicated by the appendix are included
in the second recension sample.

D.54, d.p.c.23 is a good example. The complete text of the *dictum*
as it appears in the Friedberg edition (1.214) is:

*Ecce, quomodo serui ad clericatum ualeant assumi, uel quomodo non
admittantur. Liberti quoque non sunt promouendi ad clerum, nisi ab
obsequiis sui patroni fuerint absoluti. Unde in Concilio Eliberitano:*

Winroth's appendix (201) indicates that only the first sentence of
the *dictum* appears in the first recension (the numbers 1 and 2
refer to line numbers in the print version of the Friedberg edition):

d.p.c. 23: **1** *Ecce quomodo serui* – **2** *quomodo non admittantur*.

Therefore, "Ecce, quomodo serui ad clericatum ualeant assumi, uel
quomodo non admittantur." is included in the first recension text
sample, and "Liberti quoque non sunt promouendi ad clerum, nisi ab
obsequiis sui patroni fuerint absoluti. Unde in Concilio Eliberitano:"
is included in the second recension text sample.

``` {'key': 'D.54 d.p.c.23', 'pattern': '(Ecce, quomodo serui.*?quomodo non admittantur\.)'},```

There are 897 *dicta* represented in the first-recension text sample
and 419 in the second-recension sample. Of those, 65 *dicta* are
represented in both the first- and second-recension samples.

Depending on the nature of the analysis we want to conduct, we may
choose to either include or exclude the *dicta* from *de Pen*.
Excluding the *dicta* from *de Pen*., there are 836 first-recension
and 398 second-recension *dicta*, of which 61 *dicta* are represented
in both samples.

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
population rather than sample standard deviation,[^7] because the
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

![Figure 0b updated 10 Feb 2020[^8]](PNGs/Figure_0_z-score_excluding_de_Pen.png)

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

### Zipf's law

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
1/N times that of the most frequent word, where N is the rank.[^9]
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
tail-off of 1/N. (See Figure Zb)[^10]

"we have found a clearcut correlation between the number of different
words in the *Ulysses* and the frequency of their usage, in the
sense that they approximate the simple equation of an equilateral
hyperbola: r × f = C in which *r* refers to the word's rank in the
*Ulysses* and *f* to its frequency of occurrence (as we ignore for
the present the size of C)."[@zipf_human_1949, 24]

![Figure Zb updated 16 Feb 2020](PNGs/Figure_Z_theoretical_log-log_scatter.png)

Zipf used word frequencies hand-tabulated from James Joyce's *Ulysses*
as the data set for his exploration of the relationship, and it
turns out that for English, the 1/N relationship holds up reasonably
well.[^12] The reader, however, already has enough data to question
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

![Figure Zc updated 19 Feb 2020](PNGs/Figure_Z_actual_bar.png)

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
suitable for use in stylometric analysis,[^13] but if we want to
use somewhere in the neighborhood of fifty function words for
stylometric analysis, we will have to reach all the way down to the
240th most frequent word to populate the wordlist.

### Principal Component Analysis

But increasing the number of function words also introduces a new
problem. We were able to represent our stylometric analysis of the
frequency of "*in*" and "*non*" in the samples from the first- and
second-recension *dicta* on a two-dimensional graph. But there will
be as many dimensions on the graph as there are function words for
which we collect data. And because human beings are not good at
visualizing quantitative data in more than three dimensions, we
need to find a way to reduce the number of dimensions. This is where
the technique of principal component analysis, or PCA, becomes
useful.[^14]

PCA first combines as many of the raw dimensions as possible into
synthetic components on the basis of strong correlations, either
positive or negative. For example, going back to the data on the
frequencies of "*in*" and "*non*" in the first- and second-recension
*dicta*, the two dimensions of the graph could be collapsed into a
single component that could be thought of as representing the
probability that "*in*" will, and that "*non*" will *not*, occur
in a given sample. (And this is, in fact, what the software that
I'm using for this project does.)

Finally, PCA displays the two components that contribute the most
to the total variation between the samples, and graphically arranges
the samples according to their probability relative to those two
components.

An important (and time-consuming) aspect of any project of this
nature is corpus preparation. A baseline requirement for carrying
out stylometric analysis is the availability of an electronic text.
Ideally, I would be working with electronic texts of good critical
editions of both the first and second recensions of Gratian's
*Decretum*, following consistent orthographic conventions, and
encoded in a standard format like TEI P5 XML. The Mellon
Foundation-supported project, directed by Anders Winroth, to edit
the first recension is making good progress, but is not yet complete
enough for me to use on this project. So, I am working with the
electronic text of the Friedberg edition that Timothy Reuter and
Gabriel Silagi used to produce the *Wortkonkordanz zum Decretum
Gratiani* for the MGH. [@reuter_wortkonkordanz_1990] The MGH e-text
is encoded in the obsolete Oxford Concordance Program format.

Anders Winroth and Lou Burnard of the Oxford Text Archive (OTA)
each provided me with copies of the MGH e-text. The copies differed,
and I went through an exercise not unlike preparing a critical
edition to restore the e-text to the state that Reuter and Silagi
intended.

I generated the sample text for the first-recension *dicta* by
extracting from the MGH e-text of the Friedberg edition all of the
*dicta* listed by Winroth in the appendix of *The Making of Gratian's
Decretum*, and by applying the changes to the *dicta* that differed
between the first and second recensions. [@winroth_making_2000,
197-227] I generated the sample text for the second-recension *dicta*
by starting with all the *dicta* in parts 1 and 2 of the Friedberg
edition, and then taking away every word that appeared in the
first-recension *dicta*. For the case statements, I simply used the
text from the vulgate *Decretum* as it appears in the Friedberg
edition.[^17]

Because stylometric analysis for authorship attribution depends on
the frequencies of prepositions and conjunctions, it is important
to include enclitics substituting for conjunctions. Every word in
the samples with a -*que* ending that is actually an enclitic, and
not just part of the word, has been mapped to the word plus the
pseudo-conjunction "xque".[^18]

Now that we have the preliminaries out of the way, we can take a
look at the results. I used the stylo R package to generate all of
the plots that I'm going to show you today. [@stylo] R is a statistical
programming language. [@R] Mike Kestemont, Maciej Eder, and Jan
Rybicki of the Computational Stylistics Group developed the package,
and Mike Kestemont in particular has been very generous in his
technical advice for this project.

![Figure 1 updated 11 Dec 2015](JPGs/3-way_PCA_51_MFWs_001.jpg)

Here is the plot of a three-way comparison between the case statements,
the first-recension *dicta*, and the second-recension *dicta*,
excluding the *dicta* from *de Penitentia*. The case statements are
red, the first-recension *dicta* are green, and the second-recension
*dicta* are blue. Each of the texts has been divided into 1200-words
samples. Principal component 1, along the horizontal axis is 11.2%.
Principal component 2, along the vertical axis is 7.3%. That is,
PC1 explains 11.2% of the total variation between the samples, and
PC2 explains 7.3% of the total variation between the samples. This
is good: as a general rule, we want to see a value for PC1 greater
than 10% and we want to see a value for PC2 greater than 5%. The
most striking feature of this plot is the fact that the case
statements are so far away from the *dicta*, and the next step is
to take a look at which function words are producing that effect.

![Figure 2 updated 11 Dec 2015](JPGs/3-way_PCA_51_MFWs_Loadings_001.jpg)

Turning on a stylo option called "feature loadings" lets us see how
strongly particular words influence the placement of text samples
along the PC1 and PC2 axes. The documentation calls this the feature's
"discriminative strength." For example, we see that "*sed*" and
"*non*" are way out on the right of the PC1 axis, while "*unde*"
is way down at the bottom of the PC2 axis.

Remember that in our first experiment with counting function words,
"*non*", the second most common word in the samples, was strongly
associated with the first-recension *dicta*. Here we see "*non*"
on the far right, and in fact the samples from the first-recension
*dicta* (but not from the second-recension *dicta*) tend to spread
out to the right. Note also that "*in*", the most common word in
the samples, is actually pretty close to the middle. So, it's not
so much that the second-recension *dicta* have more occurrences of
"*in*", it's that the first-recension *dicta* have fewer.

What is really interesting here is that "*an*" and "*si*" cluster
with the case statements, "*an*" very strongly, "*si*" somewhat
less so. This makes sense because indirect questions dominate the
language of the case statements. It is a question of genre. So the
next step in the stylometric analysis is to control for genre by
removing the question words "*an*" and "*si*" from the list of
function words.

![Figure 3 updated 11 Dec 2015](JPGs/3-way_PCA_49_MFWs_001.jpg)

We've now reached the final stage of the three-way comparison between
the case statements, the first-recension *dicta*, and the
second-recension *dicta*. We are now using the 49 most frequent
words on our function list instead of the 51 most frequent words,
having commented out "*an*" and "*si*". And even without "*an*" and
"*si*", PC1 still explains 10.5% of the total variation between the
samples, down slightly from 11.2%. PC2 still explains 7.3% of the
total variation between the samples. So, even controlling for genre,
the distance between the case statements and the *dicta*---both
first- and second-recension---is still quite striking.

![Figure 4 updated 25 Jun 2019](JPGs/NoQ_PCA_3_001.jpg)

![Figure 5 updated 25 Jun 2019](JPGs/NoQ_PCA_4_001.jpg)

![Figure 6 updated 21 Jan 2019](JPGs/Sg_PCA_52_001.jpg)

To turn to the other interesting aspect of the three-way comparison,
you'll note that the second-recension *dicta* in blue cluster
strongly to the upper-left quadrant. Now, Mike Witmore, a member
of my dissertation committee who isn't an insider with respect to
debates about Gratian's *Decretum*, but is very experienced in the
use of stylometry with the plays of Shakespeare, was somewhat
optimistic on the basis of this evidence that the first- and
second-recension *dicta* might be statistically distinguishable.

![Figure 7 updated 11 Dec 2015](JPGs/2-way_PCA_53_MFWs_001.jpg)

So, in an attempt to take a closer look at the *dicta* by themselves,
I removed the case statements and ran a two-way comparison of
1000-word samples of just the first- and second-recension *dicta*,
again, excluding the *dicta* from *de Penitentia*. (Stylo changes
the color assignments depending on the number of samples, so in
this plot the first-recension *dicta* are red and the second-recension
*dicta* are green.) And the results are ambiguous. The PC1 axis is
9%, somewhat under the 10% threshold we would like to see. Also,
although we see the second-recension *dicta* clustering mostly to
the right of the PC1 axis, the two sets of samples are not separated
as cleanly as we'd like to see, and certainly nowhere near as cleanly
as the case statements were from the *dicta*.

![Figure 8 updated 11 Dec 2015](JPGs/4-way_PCA_49_MFWs_001.jpg)

All of the slides we've seen so far exclude the *dicta* from *de
Penitentia*, so before moving on to my conclusion, I do want to
quickly show you what the results look like when we include the
first-recension *dicta* from *de Pen.* (there are not enough words
in the second-recension *dicta* in *de Pen.* to be statistically
significant---9,525 vs. 556). Many scholars have observed that
*dicta* and canons are poorly separated in *de Pen.* I believe that
the unusual dispersion of the samples that you see in this plot is
a result of that feature.

## Conclusion

Principal component analysis (PCA) of the frequencies of function
words (prepositions and conjunctions) in the texts strongly suggests
that the author of the case statements was not the same person as
the authors of either the first- or second-recension *dicta*. PCA
also suggests (less strongly) that the first- and second-recension
*dicta* were not the work of either one or two authors, but are
more likely to have been the product of collaborative authorship.

On Monday, Anders presented a sketch of what a stemma for the first
recension might look like. It suggested that the textual transmission
was far more complicated than we may have imagined (or at least may
have hoped for). The results I've presented here today suggest that
the question of authorship is potentially as complicated as the
question of transmission. I believe that there is enough evidence
at least to question assumptions of monolithic authorships (of
either the one Gratian or two Gratians variety). If we cannot
satisfactorily answer the question "was there one Gratian or were
there two?" it is probably because that is not the right question
to ask.

[^1]: Earlier versions of this chapter were presented as conference
papers. "Can Stylometry Provide New Evidence about the Identity of
Gratian 1 and Gratian 2?", was presented to the session on Canon
Law in the Twelfth and Thirteenth Centuries at the *Rem non novam
nec insolitam aggredimur* conference and grand opening of the Stephan
Kuttner Institute of Medieval Canon Law at Yale Law School, May
21-22, 2015. "New evidence for the authorship of case statements
and *dicta* in Gratian's *Decretum*" was presented to the Classical
Sources III session at the Fifteenth International Congress of
Medieval Canon Law (ICMCL) at Université Paris II Panthéon-Assas,
July 17-23, 2016.

[^f]: @mosteller_inference_1964, 14. See also @adair_authorship_1944a, 104.

[^4]: @adair_authorship_1944a and @adair_authorship_1944b.

[^6]: Including the *dicta* from *de Penitentia* distorts the
results of the analysis, because out of the 10,081 words of the
vulgate version of the *de Pen.* *dicta*, only 556 were added or
changed between the first and second recensions of the *Decretum*.

[^7]: The formula for sample standard deviation is:

    $s=\sqrt{\frac{1}{N-1}\sum_{i=1}^N(x_i-\bar{x})^2}$

[^8]: Is standard deviation measuring anything here other than the
fact that the R1 sample is 3.9785 times the size of the R2 sample?

    $0.3447\times\frac{56713}{14255} = 0.3447\times3.9785 = 1.3756$

[^9]: @zipf_human_1949, 73-131. Zipf himself referred to the
relationship as "the law of diminishing returns of words". Zipf
previously discussed the relationship in @zipf_psycho-biology_1935.
[UCSD Geisel Library has a copy, currently (18 February 2020)
unavailable, of a 1965 MIT Press reprint of this book.] Zipf expressed
the relationship as r × f = C.

[^10]: Note that the base of the logarithms does not matter (as
long as they are the same for both axes). Regardless of whether we
take base e (natural) or base 10 logarithms of rank and word count,
the slopes will be the same: -1.000 for the theoretical Zipf
distribution of word frequencies, and (as we shall see) -0.5923 for
the actual frequencies of the twenty most frequent words in the
first- and second-recension *dicta*.

[^12]: See @zipf_human_1949, 23-52, for Zipf's discussion of the
rank-frequency distribution of words in Joyce's *Ulysses*.

[^13]: **Even if we have to later discard *si* for other reasons.**

[^14]: For a general introduction to the use of principal component
analysis (PCA) in literary stylometric analysis, see @craig_stylistic_2004
and Chapter 6 "Style" in @jockers_macroanalysis_2013.

[^17]: **This is perhaps not entirely satisfactory. It would be
more methodologically consistent with the way in which the samples
of the first-recension dicta were prepared to apply the differences
found in Winroth's appendix to the case statements as well, however
the differences are quite minimal. The only case statement (*thema*)
for which Winroth notes a textual difference is C.19 d.init.
(Winroth, 216). The first-recension version of the text omits a
13-word clause added to the second recension version, seemingly for
the purpose of piling up descriptive detail. (*unus relicta propria
ecclesia eo inuito, alter dimissa regulari canonica cenobio se
contulit*). None of the wordlists used to perform the principal
component analyses include any of these 13 words, so the use of
the vulgate rather than a proxy first-recension version of the text
of C.19 d.init. has no effect on the outcome of these tests.**

[^18]: In the case statements, 1st-, and 2nd-recension *dicta* from
Gratian's *Decretum*, there are 747 occurrences of 79 unique words
ending in -*que*. (This does not count 423 occurrences of the word
'*que*' itself.) Of those, 498 are occurrences of 19 unique words
from Schinke's 54-word pass list, while 249 occurrences of 60 unique
words are not. It is from these 249 words that, according to Schinke,
the -*que* ending should be detached as an enclitic.

    However, the 249 words include 72 occurrences of 17 unique words
    ending with the adverbial enclitics -*cumque* or -*cunque*,
    from which the -*que* ending should not be detached. The 249
    words also include a further 149 occurrences of 21 unique false
    positives:

    cumque, eque (aeque), namque, pleraque, plerique, plerisque,
    plerumque, quinque, unamquamque, unaqueque, unicuique,
    uniuscuiusque, unumquemque, unusquisque, usquequaque, utramque,
    utraque, utrique, utrisque, utriusque, utrumque.

    This leaves only 28 occurrences of 22 unique words from which
    the -*que* ending should actually be detached as an enclitic.

    False positives over-represent the frequency of occurrence of
    the '-*que*’ enclitic as a conjunction by an order of magnitude.
    Including all false positives makes 'xque' the 37th most frequent
    word in the sample, while excluding them makes it the 376th
    most frequent word. There are 55 occurrences of the word
    '*namque*', the most frequently occurring false positive.
    Detaching the '-*que*' ending from '*namque*' overstates the
    frequency of '*nam*', making what is actually the 480th most
    frequent word appear to be the 130th, while making '*namque*',
    which is actually the 176th most frequent word in the samples
    when false positives are excluded, disappear from the list
    altogether.

