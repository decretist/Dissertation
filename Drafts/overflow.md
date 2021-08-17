---
author: Paul Evans
date: 13 May, 2021
title: Overflow
---
## Chapter 3

### *Decretum* vs. *dicta*

Furthermore, the *Decretum* is mostly quoted text. Therefore, the
questions of the authorship and authority of the *Decretum* as a
whole and of the *dicta* have to be considered distinctly although
not separately from one another.

---

### Gratian's teaching career

Evidence concerning Gratian's career as a teacher of canon law is
contradictory.  We might be better able to assess Gratian's teaching
career and how it influenced the compilation and transmission of
the *Decretum* were we in a position to positively identify at least
a few of his students. Here again, however, the evidence is mixed
at best.

---

### Epilogue

By the beginning of the thirteenth century, the systematic study
of canon law had evolved in a direction of which its father Gratian
would probably not have approved, and which he may even have had
difficulty recognizing as the same practical or applied branch of
theology his own work presupposed it to be. After around 1190, the
attention of both academic and practicing canonists decisively
turned away from theological jurisprudence in the tradition of
Gratian, based on a rich collection of scriptural, patristic,
conciliar, and papal source texts, and towards a much more narrowly
circumscribed technical jurisprudence focused exclusively on
contemporary papal decretals.

---

Modern scholars considering the authorship of a text are primarily
interested in the question of whose thought is reflected in the
arguments it makes.

This dissertation is about whether one, two, or many authors wrote
the exact words in the text of the *dicta* in the *Decretum*.

#### Sg

Much of the debate over whether the *Decretum* was the result of a
continuous or discontinuous process of composition focused on the
Sankt Gallen Stiftsbibliothek 673 (Sg) manuscript. Pennington,
Eichbauer, and Larson have argued that it represents, at some unknown
number of removes, an earlier version of the *Decretum* than Winroth's
first recension. Winroth and Wei have argued that Sg is a relatively
uninteresting abbreviation of a first recension manuscript with
some second recension interpolations.[^40]

The version of the *Decretum* preserved in the Sankt Gallen
Stiftsbibliothek 673 (Sg) manuscript contains somewhat fewer than
1,050 canons,[^41] and is therefore considerably shorter than either
the first recension (1,860 canons) or the vulgate (3,945) versions
of the text.[^42] Formally, Sg is not divided into parts; all of
its content is presented in the form of cases. The first case,
however, is unique to Sg, and is referred to as *Causa Prima* to
distinguish it from the *Causa* I found in all other pre-vulgate
and vulgate versions of the *Decretum*. (*Causa* I appears as *Causa*
II in Sg.) It contains a subset of canons and *dicta* found in Part
I, presented in almost exactly the same order in which they appear
in other versions of the *Decretum*. (There is one relatively minor
exception with respect to the ordering of the texts, the four canons
corresponding to D.32 c.3, c.4, c.6, and c.7 are inserted between
the canons corresponding to D.31 c.6 and D.31
c.7.)[@larrainzar_borrador_1999, 653] Notably, *Causa Prima* contains
no texts (canons or *dicta*) from the *tractatus de legibus*
(distinctions 1-20) and none from Gratian's "epilogue" (distinctions
81-101).

[^40]: See @eichbauer_gratians_2013 for a good recent overview of
these debates.

[^41]: Carlos Larrainzar describes Sg as having "poco menos de 1,050
*auctoritates* y en torno a los 650 *dicta*." @larrainzar_borrador_1999, 601.
"The second recension contains 3,945 canons (including the
paleae) in the editions. The first recension contains only 1,860
canons (47 percent)." @winroth_making_2000, 122.

[^42]: See @larrainzar_borrador_1999, 601, for the number of canons
in Sg, emphasizing that it is approximate. See @winroth_making_2000,
122, for the number of canons in the first recension. 3,945 is a
conventional number.

---

## Chapter 4

The two-dimensional visualization above proceeded from the traditional
assumption that Gratian's *dicta*---defined as the hypothetical
case statements (*themata*) plus the first- and second-recension
*dicta* including the *dicta* from *de Pen*.---are the work of a
unitary author, the eponymous Gratian. The consequence of that
assumption for the purpose of experimental design (the design of
that demonstration) is that we can treat the corpus of texts analyzed
in that test/demonstration as the entire population of words
attributable to the author Gratian. Population standard deviation
was therefore the appropriate statistical technique to apply to
visualize word frequency variations among/between samples within
that population.

---

That does not mean that we cannot apply the established techniques
of authorship attribution to Gratian's *dicta*, but it does mean
that we have to make careful decisions about experimental design.

---

First I'm going to discuss in general terms the use of stylometry
for authorship attribution. Then, I'm going to discuss the methodology
and the software that I am using for this project. Finally, I am
going to show the results of stylometric analysis of the case
statements, the first-recension *dicta*, and the second-recension
*dicta* (first without, then with, the *dicta* from *de Penitentia*),
and discuss some possible interpretations of those results.

In theory, that means that you ought to be able to make a list of
every function word in a language, although in practice, that's not
easy to do.

---

Increasing the number of function words also introduces a new
problem. We were able to represent our stylometric analysis of the
frequency of *in* and *non* in the samples from the first- and
second-recension *dicta* on a two-dimensional graph. But there will
be as many dimensions on the graph as there are function words for
which we collect data. And because human beings are not good at
visualizing quantitative data in more than three dimensions, we
need to find a way to reduce the number of dimensions. This is where
the technique of principal component analysis, or PCA, becomes
useful.

---

### Burrows

Thus far, I've focused on Burrows's Delta. In the spirit of *de
mortuis nihil nisi bonum*, I have not been critical of the recently
(18 December 2019) deceased Burrows. Burrows was not a statistician
as, e.g., Mosteller and Wallace were. It is unclear to me how much
mathematical learning he had. Burrows was an English professor who
was interested in Restoration-era poetry. He had a toolkit, Microsoft
Excel, that he was comfortable using, and he used the tools that
he found in that toolkit, such as mean and standard deviation. He
was not overly concerned as to whether his technique was mathematically
or statistically justified.

---

### De Doctrina Christiana (Milton)

The manuscript of *De Doctrina Christiana* was discovered in November
1823 by Robert Lemon the elder, Deputy Keeper of His Majesty's State
Papers in a 'press' (cupboard) in the Old State Paper Office in the
Middle Treasury Gallery in Whitehall.[^m1] The manuscript was
attributed by Lemon to Milton.[^m2] The discovery and attribution
of the manuscript generated enough public interest that Home Secretary
Robert Peel was asked, and answered, questions about the printing
arrangements in the House of Commons in March 1824 [@campbell_milton_2007,
1, 5]. The attribution was challenged by William Hunter in 1991.
[@campbell_milton_2007, 1]

[^m1]: For attempts to attribute authorship of *De Doctrina Christiana*
using stylometry, see: @campbell_provenance_1997; @rumrich_stylometry_2002;
and @campbell_milton_2007.

[^m2]: On what grounds?

---

### Zipf

Zipf's theories of language proceeded from wider assumptions: that
human language had evolved to take advantage the large but not
unlimited (considerable but finite) resources the human brain
dedicated to language processing and that the word distribution
(which Zipf saw as universal across all languages) was a necessary
adaptation to use those computational resources as efficiently as
possible.

---

[^a]: As of 10 February 2020, there is a bug in the `pstdev()` function
in the standard Python 3 statistics library such that the optional
`mu =` keyword argument to override the value of mean does not work.
Thanks to Saturnino Garcia (University of San Diego Department of
Computer Science) and James Krooskos (UC San Diego Alzheimer's
Disease Cooperative Study) for help reproducing this bug.

    ~~~ {python}
    import math
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
    ~~~

[^z]: The vertical bands toward the upper-left hand corner of the
plot - which also appear in Zipf's 1935 figures - require some
interpretation. There can be a range of values for numbers of
occurrence (b) for which only one value for number of words (a) has
that number of occurrence. There are 62 cases in the *dicta* from
Gratian's *Decretum* in which only a single word (a = 1) has a given
number of occurrences (b). For example, only one word, *potest*,
has 143 occurrences, and only one word, *in*, has 2,187 occurrences.
The upper-left-most vertical band represents all 62 of the words
for which only a single word (a = 1) has a particular value for the
number of occurrences (b). Similarly, the next vertical band to the
right represents all of the words for which only two words (a = 2)
have particular values for the number of occurrences (b).

