---
author: Paul Evans
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
date: 10 April 2020
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
Gratian's *dicta* --- defined as the hypothetical case statements
(*themata*) plus the first- and second-recension *dicta* including
the *dicta* from *de Pen*. --- are the work of a unitary author,
the eponymous Gratian. The consequence of that assumption for the
purpose of experimental design (the design of that demonstration)
is that we can treat the corpus of texts analyzed in that
test/demonstration as the entire population of words attributable
to the author Gratian. Population standard deviation was therefore
the appropriate statistical technique to apply to visualize word
frequency variations among/between samples within that population.

(Explain that 2-D viz separated the population into R1, R2, and
other [define].)

Attempts to attribute authorship, however, are typically undertaken
in scenarios where there is a large (enough) number of texts securely
attributable to a known author, and a text, or at most a small
number of texts, of unknown authorship. The attempt is then made
to attribute the unknown text to the known author, or to rule out
such an attribution. Take *The Federalist* as an example. There are
numbers of the Federalist of disputed or unknown attribution, a
small and well-defined number of candidates for authorship ---
Hamilton, Jay, Madison --- to whom those numbers might be attributed,
and securely attributed samples from each of the candidates, from
the same work no less.

This is obviously not possible (this is not the case) with the
*dicta* from Gratian's *Decretum*. As the survey in Chapter 3 *supra*
indicated, near-contemporaries knew next to nothing about Gratian.
Perhaps most notably, although Gratian was thought to have been a
teacher, no one in the generation following made an unambiguous
claim to have been his student. There are no other writings securely,
or even insecurely, attributed to him. That does not mean that we
cannot apply the established techniques of authorship attribution
to Gratian's *dicta*, but it does mean that we have to make careful
(intentional) decisions about experimental design.

Introducing Burrow's Delta **(define)** at this point advances my
argument in two ways. As a technical matter, Burrows's Delta gets
around the limitation on the number of words to the two or, at best,
three dimensions that the human mind can visualize by collapsing
distance measurements across an arbitrary number of dimensions into
a single metric, the 'Delta'. It can also be fairly straightforwardly
adapted to the particular situation in which we find ourselves where
there are no other texts securely attributed to Gratian with which
we can compare, for example, the hypothetical case statements
(*themata*) or second-recension *dicta*.

Two experiments that demonstrate how Burrow's Delta can be applied
to meet both of these objectives follow. The first will be a
comparison of the hypothetical case statements (*themata*) with the
first- and second-recension *dicta* (both including the *dicta*
from *de Pen*.), using the frequencies of occurrence of the four
most frequent words (MFWs) in Gratian's *dicta* as the basis for
comparison. For each of the three subcorpora, we will hypothesize
each subcorpus in turn to be the work of an unknown author, and
will treat the other two subcorpora as making up a corpus of works
by a known author. Using three subcorpora and four dimensions makes
the solution compact enough to show all the intermediate steps. The
second experiments will compare the thirty most frequent words
(MFWs) across ten subcorpora: cases (C.1-36 d.init.), laws (D.1-20
R1 *dicta*), orders1 (D.21-80 R1 *dicta*), orders2 (D.81-101 R1
*dicta*), monastic (C.16-20 R1 *dicta*), heresy (C.23-26 R1 *dicta*),
marriage (C.27-36 R1 *dicta*), penance (*de Pen*. R1 *dicta*), other
(all other R1 *dicta*), and second (all R2 *dicta*, including *de
Pen*.). For each of the ten subcorpora, we will hypothesize each
subcorpus in turn to be the work of an unknown author, and will
treat the other nine subcorpora as composing a corpus of works by
a known author. The scale of the second experiment is closer to
that of the experiments carried out by John Burrows and David Hoover,
the pioneers of the technique, but makes it impractical to show the
results at every intermediate step in the process.

