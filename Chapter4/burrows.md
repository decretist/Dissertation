---
author: Paul Evans
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
date: 6 June 2020
suppress-bibliography: false
title: Chapter 4
subtitle: Burrows's Delta
---
The technique of plotting word frequency data by z-score is known
as Burrows's Delta, after John F. Burrows (d.2019) of the University
of Newcastle, Australia, who first proposed the metric in 2001. It
has the advantage of making the statistical significance of plotted
data apparent in a way that plotting raw frequency data does not.
Burrows's Delta is one of a number of distance methods of authorship
attribution, but has the particular advantage of being widely
accepted in the scholarly literature of the field of computational
linguistics.

Every attribution experiment starts from an hypothesis (sometimes
implicit rather than explicit) concerning authorship. The two-dimensional
visualization above proceeded from the traditional assumption that
Gratian's *dicta*---defined as the hypothetical case statements
(*themata*) plus the first- and second-recension *dicta* including
the *dicta* from *de Pen*.---are the work of a unitary author,
the eponymous Gratian. The consequence of that assumption for the
purpose of experimental design (the design of that demonstration)
is that we can treat the corpus of texts analyzed in that
test/demonstration as the entire population of words attributable
to the author Gratian. Population standard deviation was therefore
the appropriate statistical technique to apply to visualize word
frequency variations among/between samples within that population.

---

Attempts to attribute authorship are typically undertaken in scenarios
where there is a large (enough) number of texts securely attributable
to a known author, and a text, or at most a small number of texts,
of unknown authorship. The attempt is then made to attribute the
unknown text to a known author, or to rule out such an attribution.
Take the *Federalist* as an example. There are numbers of the
*Federalist* of disputed or unknown attribution, a small and
well-defined number of candidates for authorship---Hamilton, Jay,
Madison---to whom those numbers might be attributed, and securely
attributed samples from each of the candidates, conveniently from
the same work no less.

Such an approach is obviously not possible in the case of the *dicta*
from Gratian's *Decretum*. As the survey in Chapter 3 above indicated,
near-contemporaries knew next to nothing about Gratian. Perhaps
most notably, although Gratian was thought to have been a teacher,
no one in the generation following made an unambiguous claim to
have been his student. There are no other writings securely, or
even insecurely, attributed to him. That does not mean that we
cannot apply the established techniques of authorship attribution
to Gratian's *dicta*, but it does mean that we have to make careful
decisions about experimental design.

Introducing Burrow's Delta at this point advances the argument in
two ways. As a technical matter, Burrows's Delta gets around the
limitation on the number of words to the two or, at best, three
dimensions that the human mind can visualize by collapsing distance
measurements across an arbitrary number of dimensions into a single
metric, the 'Delta'. It can also be fairly straightforwardly adapted
to the particular situation in which we find ourselves where there
are no other texts securely attributed to Gratian with which we can
compare, for example, the hypothetical case statements (*themata*)
or second-recension *dicta*.

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
