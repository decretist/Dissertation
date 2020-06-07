---
author: Paul Evans
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
date: 6 June 2020
suppress-bibliography: false
title: Chapter 4
subtitle: Burrows's Delta
---
The plotting examples presented in the previous section are suggestive
of ways in which differences between the frequencies of occurrence of
common words in samples from a corpus of texts can be quantified
in statistically meaningful units (standard deviations or values
of z) and combined to represent the distance between those samples.
This technique is, however, of limited value so long as we are
restricted to the two, or at most three, dimensions the human mind
is capable of visualizing. In 2001, John F. Burrows (d.2019) of the
University of Newcastle, Australia, proposed a generalization that
gets around the limitation on the number of words to two or three
dimensions by collapsing z-score distance measurements of word
frequency data across an arbitrary number of dimensions into a
single metric. Burrows applied the metric, which he called the
Delta, in the context of a new technique for authorship attribution.
Although other distance methods of authorship attribution have been
proposed since, Burrows's Delta is widely accepted in the scholarly
literature of the field of computational linguistics, and it will
therefore be used as the basis for the demonstrations in this
section.

Every attribution experiment starts from an hypothesis (sometimes
implicit rather than explicit) concerning authorship. Attempts to
attribute authorship are typically undertaken in scenarios where
there is a large (enough) number of texts securely attributable to
a known author, and a text, or at most a small number of texts, of
unknown authorship. The attempt is then made to attribute the unknown
text to a known author, or to rule out such an attribution. Take
the *Federalist* as an example. There are numbers of the *Federalist*
of disputed or unknown attribution, a small and well-defined number
of candidates for authorship---Hamilton, Jay, Madison---to whom
those numbers might be attributed, and securely attributed samples
from each of the candidates, conveniently from the same work no
less.

Such an approach is obviously not possible in the case of the *dicta*
from Gratian's *Decretum*. As the survey in Chapter 3 above indicated,
near-contemporaries knew next to nothing about Gratian. Perhaps
most notably, although Gratian was thought to have been a teacher,
no one in the generation following made an unambiguous claim to
have been his student. There are no other writings securely, or
even insecurely, attributed to him. Fortunately, Burrows's Delta
can be readily adapted to the particular situation in which we find
ourselves, where there are no other texts attributed to Gratian
with which we can compare, for example, the hypothetical case
statements (*themata*) or second-recension *dicta*.

---

Two experiments that demonstrate how Burrow's Delta can be applied
to meet both of these objectives follow. The first will be a
comparison of four subcorpora, Gratian0 (the hypothetical case
statements or *themata*), Gratian1 (the first-recension *dicta*
excluding the *dicta* from *de Penitentia*), dePen (first- and
second-recension *dicta* from *de Penitentia*), and Gratian2 (the
second-recension *dicta* excluding the *dicta* from *de Penitentia*),
using the frequencies of occurrence of the four most frequent words
(MFWs) in Gratian's *dicta* as the basis for comparison. We will
hypothesize that the subcorpus containing the hypothetical case
statements (*themata*) is the work of an unknown author, and will
treat the other three subcorpora as making up a corpus of works by
a known author. Using four subcorpora and four dimensions makes the
solution compact enough to show all of the intermediate steps.

The second experiment will compare the thirty most frequent words
(MFWs) across fourteen subcorpora: cases (C.1-36 d.init.), laws
(D.1-20 R1 *dicta*), orders1 (D.21-80 R1 *dicta*), orders2 (D.81-101
R1 *dicta*), simony (C.1 R1 *dicta*), procedure (C.2-6 R1 *dicta*),
other1 (C.7-10 R1 *dicta*), other2 (C.11-15 R1 *dicta*), monastic
(C.16-20 R1 *dicta*), other3 (C.21-22 R1 *dicta*), heresy (C.23-26
R1 *dicta*), marriage (C.27-36 R1 *dicta*), penance (R1 and R2
*dicta* from *de Penitentia*), and second (all R2 *dicta*, excluding
those from *de Penitentia*).[^b1] For each of the fourteen subcorpora,
we will hypothesize each subcorpus in turn to be the work of an
unknown author, and will treat the other thirteen subcorpora as
composing a corpus of works by a known author. The scale of the
second experiment is closer to that of the experiments carried out
by John Burrows and David Hoover, the pioneers of the technique,
but makes it impractical to show the results at every intermediate
step in the process.

---

|     |   Gratian0 |   Gratian1 |     dePen |   Gratian2 |
|:----|-----------:|-----------:|----------:|-----------:|
| in  |   -2.87019 | -0.434152  | -0.709549 |  1.1437    |
| non |   -6.54914 | -0.0361467 |  1.01758  | -0.981437  |
| et  |   -3.23751 | -0.978645  |  1.02007  | -0.0414224 |
| est |   -3.52638 |  0.417881  |  0.723278 | -1.14116   |

---

|     |   Gratian0 |
|:----|-----------:|
| in  |   -2.87019 |
| non |   -6.54914 |
| et  |   -3.23751 |
| est |   -3.52638 |

---

|     |   Gratian1 |   dePen |   Gratian2 |
|:----|-----------:|--------:|-----------:|
| in  |    2.43604 | 2.16064 |    4.01389 |
| non |    6.51299 | 7.56672 |    5.5677  |
| et  |    2.25886 | 4.25757 |    3.19608 |
| est |    3.94426 | 4.24965 |    2.38522 |

---

|          |   Gratian1 |   dePen |   Gratian2 |
|:---------|-----------:|--------:|-----------:|
| Gratian0 |    3.78804 | 4.55865 |    3.79072 |

---

|          |   Gratian0 |   Gratian1 |      dePen |   Gratian2 |
|:---------|-----------:|-----------:|-----------:|-----------:|
| Gratian0 |  nan       |   3.78804  |   4.55865  |   3.79072  |
| Gratian1 |    1.43613 | nan        |   0.362766 |   0.545326 |
| dePen    |    1.98731 |   0.451469 | nan        |   0.767281 |
| Gratian2 |    1.71849 |   0.627777 |   0.790456 | nan        |

---

|          |      psAug |   Gratian1 |      dePen |   Gratian2 |
|:---------|-----------:|-----------:|-----------:|-----------:|
| psAug    | nan        |   2.64561  |   1.7373   |   3.43185  |
| Gratian1 |   1.02276  | nan        |   0.465323 |   0.932542 |
| dePen    |   0.517843 |   0.473271 | nan        |   1.34527  |
| Gratian2 |   5.20047  |   3.35742  |   4.28572  | nan        |

[^b1]: The division of the first-recension (R1) *dicta* into twelve
sections follows the division of Gratian's *Decretum* proposed by
Alfred Beyer in -@beyer_lokale_1998, 17-18.
