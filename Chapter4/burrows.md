---
author: Paul Evans
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
date: 9 June 2020
suppress-bibliography: false
title: Chapter 4
subtitle: Burrows's Delta
---
The examples presented in the previous section are suggestive of
ways in which differences between the frequencies of occurrence of
common words in samples from a corpus of texts can be quantified
in statistically meaningful units (standard deviations or values
of z) and combined to represent the distance between those samples.
This technique is, however, of limited value so long as we are
restricted to the two, or at most three, dimensions the human mind
is capable of visualizing. In 2001, John F. Burrows (d.2019) of the
University of Newcastle, Australia, proposed a generalization that
gets around the limitation on the number of features to two or three
by averaging z-score distance measurements of word frequency data
for any number of features. This has the effect of collapsing
distance measurements in an arbitrary number of dimensions into a
single metric. Burrows called this metric the Delta, and it is now
generally referred to as Burrows's Delta ($\Delta_B$).[^b1]

Burrows applied the metric, which he called the Delta, in the context
of a new technique for authorship attribution.

(**The metric is not the technique.**)

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
from each of the candidates, conveniently from the same work.

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

(**Burrows's Delta measures Manhattan Distance.**)

Although other distance methods of authorship attribution have been
proposed since,[@evert_understanding_2017] Burrows's Delta is widely
accepted in the scholarly literature of the field of computational
linguistics, and it will therefore be used as the basis for the
demonstrations in this section.

The first experiment will be a comparison of four subcorpora,
Gratian0 (the hypothetical case statements or *themata*), Gratian1
(the first-recension *dicta* excluding the *dicta* from *de
Penitentia*), dePen (first- and second-recension *dicta* from *de
Penitentia*), and Gratian2 (the second-recension *dicta* excluding
the *dicta* from *de Penitentia*), using the frequencies of occurrence
of the four most frequent words (MFWs) in Gratian's *dicta* as the
basis for comparison. We will hypothesize that the subcorpus
containing the hypothetical case statements (*themata*) is the work
of an unknown author, and will treat the other three subcorpora as
making up a corpus of works by a known author. Using four subcorpora
and four features, where every feature analyzed is represented in
a different dimension, demonstrates that z-score distance methods
can be extended to cases in which the number of dimensions is greater
than three. It also has the advantage of making the solution compact
enough to allow readers to follow along and reassure themselves of
the mathematical validity of all of the intermediate steps leading
to the final result.

The first experiment resumes directly where the two-dimensional
visualization demonstration left off, so all function definitions
and variable values in force at the conclusion of that demonstration
are still valid. In particular, this experiment inherits the z-scores
for all of the four most frequent words (MFWs). While we disregarded
the data for the third and fourth most frequent words (*et* and
*est*) for the purpose of the visualization demonstration, they
will be fully taken into account here. (Remember that the values
for mean and standard deviations used to derive the z-scores were
calculated without reference to the Gratian0 sample here being
treated as the unknown).

First, split the z-scores into two new dataframes, one for the test
sample Gratian0, assumed for the purpose of this experiment to be
the work of an unknown author:

```python
test = z_scores[[unknown]]
```

|     |   Gratian0 |
|:----|-----------:|
| in  |    -2.8702 |
| non |    -6.5491 |
| et  |    -3.2375 |
| est |    -3.5264 |

the other for the comparison samples Gratian1, dePen, and Gratian2,
assumed for the purpose of this experiment to represent the work
of known authors:

```python
corpus = z_scores[samples]
```

|     |   Gratian1 |   dePen |   Gratian2 |
|:----|-----------:|--------:|-----------:|
| in  |    -0.4342 | -0.7095 |     1.1437 |
| non |    -0.0361 |  1.0176 |    -0.9814 |
| et  |    -0.9786 |  1.0201 |    -0.0414 |
| est |     0.4179 |  0.7233 |    -1.1412 |

The formula used to calculate Burrows's Delta is:

$\Delta_B = \frac{1}{N}\sum_{i = 1}^N|z_i(t) - z_i(c)|$

It is easiest to deal with the formula in two steps, first evaluating
the expression $|z_i(t) - z_i(c)|$. Note that because we take the
absolute value of the result, the order of operands on either side
of the subtraction operator '-' does not matter. For each of the
three columns (Gratian1, dePen, and Gratian2) in the *corpus*
dataframe, subtract the z-score in each row from the z-score in the
same row of the *test* (Gratian0) dataframe, take the absolute
value, and record the result in the corresponding column and row
of the *differences* dataframe. For example, the z-score for *non*
in *test* (Gratian0) is -6.5491, the z-score for *non* in the
Gratian1 column of *corpus* is -0.0361, so the absolute value of
the difference recorded in the *non* row of the Gratian1 column of
*differences* would be 6.5130.

```python
differences = (test.values - corpus).abs()
```

|     |   Gratian1 |   dePen |   Gratian2 |
|:----|-----------:|--------:|-----------:|
| in  |     2.436  |  2.1606 |     4.0139 |
| non |     6.513  |  7.5667 |     5.5677 |
| et  |     2.2589 |  4.2576 |     3.1961 |
| est |     3.9443 |  4.2497 |     2.3852 |

Given the layout of the *differences* dataframe in which we have
stored the intermediate results, the part of the formula we deferred
dealing with ($\frac{1}{N}\sum_{i = 1}^N$) is simply a notationally
exact way of indicating that we are to take the average (arithmetic
mean) of the values in each of the columns, and record the resulting
value of $\Delta_B$ in the corresponding column of the *deltas*
dataframe.

```python
row = (differences.mean(axis = 0)).to_frame(unknown).transpose()
```

|          |   Gratian1 |   dePen |   Gratian2 |
|:---------|-----------:|--------:|-----------:|
| Gratian0 |      3.788 |  4.5586 |     3.7907 |

The Gratian1 subcorpus is just slightly closer than the Gratian2
subcorpus to the unknown Gratian0 test case, with values of Delta
for both rounding to 3.79. A candidate is defined as being *closest*
to the unknown when it has the lowest mean of the absolute values
of the differences between the z-scores for the unknown and the
candidate.But as Burrows pointed out, one candidate will always
have the lowest $\Delta_B$, so that in itself is not enough to make
or to rule out an attribution of authorship. We will need further
information before we can provide any kind of interpretation for
the result. The most we can say based on this result is that the
hypothetical case statements are less likely to have been written
by the author of the *dicta* in *de Penitentia* than by the authors
of the first- and second-recension *dicta*.

The second experiment is a variation on the first, in which a
3881-word sample made up of seven extended passages from the
pseudo-Augustinian *De vera et falsa penitentia* quoted by Gratian
in *de Penitentia* are substituted for the 3605-word sample containing
the hypothetical case statements.[^b3] As noted in Chapter 0 above,
Gratian can be said with a high degree of confidence **not** to be
the author of *De vera et falsa penitentia*. The authors are strongly
distinguished by their choice of post-positive conjunctions: Gratian
has a preference for *autem*, while pseudo-Augustine has an even
stronger preference for *enim*. Substituting the pseudo-Augustinian
sample in place of the case statements demonstrates the kinds of
results to be expected from Burrows's Delta in a situation in
which an attribution of authorship can reasonably be ruled out.

|       |   Gratian1 |   dePen |   Gratian2 |
|:------|-----------:|--------:|-----------:|
| psAug |     2.6456 |  1.7373 |     3.4318 |

The third experiment extends the first by treating each of the
subcorpora, Gratian0, Gratian1, dePen, and Gratian2 sequentially
as the work of an unknown author, and the other three subcorpora
as constituting a corpus of works by a known author. This is an
attempt to demonstrate the adaptation of Burrows's technique in a
circumstance in which there are no securely attributed comparison
texts outside of the corpus, and in which there is some reason to
suspect that there are multiple authors at work within the corpus.

```python
# author candidates, e.g. Gratian 1, the Master of Penance, Gratian 2, etc.
candidates = ['Gratian0', 'Gratian1', 'dePen', 'Gratian2']
deltas = pd.DataFrame(columns = candidates)
limit = 4 # 4 most frequent words (MFWs)
for candidate in candidates:
    unknown = candidate
    samples = candidates[:]
    samples.remove(unknown)
    features = get_features(samples)
    mfws = list(features.keys())[:limit]
    counts = get_counts(mfws, [unknown] + samples)
    lengths = get_lengths([unknown] + samples)
    frequencies = (counts / lengths.values) * 1000
    means = frequencies[samples].mean(axis = 1).to_frame('mean')
    standard_deviations = frequencies[samples].std(axis = 1).to_frame('std')
    z_scores = (frequencies - means.values) / standard_deviations.values
    test = z_scores[[unknown]]
    corpus = z_scores[samples]
    differences = (test.values - corpus).abs()
    row = (differences.mean(axis = 0)).to_frame(unknown).transpose()
    deltas = deltas.append(row)
```

|          |   Gratian0 |   Gratian1 |    dePen |   Gratian2 |
|:---------|-----------:|-----------:|---------:|-----------:|
| Gratian0 |   nan      |     3.788  |   4.5586 |     3.7907 |
| Gratian1 |     1.4361 |   nan      |   0.3628 |     0.5453 |
| dePen    |     1.9873 |     0.4515 | nan      |     0.7673 |
| Gratian2 |     1.7185 |     0.6278 |   0.7905 |   nan      |

Considering the results of the first three experiments together,
we can start to form some very preliminary conclusions. Based on
the values for $\Delta_B$ in the table above, the most likely
attribution is that the first-recension *dicta* (Gratian1) and the
*dicta* from *de Penitentia* (dePen) have the same author. It is
less likely that the first-recension *dicta* (Gratian1) and the
second-recension *dicta* (Gratian2) have the same author. It is
less likely still that the *dicta* from *de Penitentia* and the
second-recension *dicta* have the same author. It is much less
likely that the case statements (Gratian0) have the same author as
either the first- (Gratian1) or second-recension (Gratian2) *dicta*.
Finally, the least likely attribution is that the case statements
(Gratian0) have the same author as the *dicta* from *de Penitentia*.

---

The fourth and final experiment will compare the thirty most frequent
words (MFWs) across fourteen subcorpora: cases (C.1-36 d.init.),
laws (D.1-20 R1 *dicta*), orders1 (D.21-80 R1 *dicta*), orders2
(D.81-101 R1 *dicta*), simony (C.1 R1 *dicta*), procedure (C.2-6
R1 *dicta*), other1 (C.7-10 R1 *dicta*), other2 (C.11-15 R1 *dicta*),
monastic (C.16-20 R1 *dicta*), other3 (C.21-22 R1 *dicta*), heresy
(C.23-26 R1 *dicta*), marriage (C.27-36 R1 *dicta*), penance (R1
and R2 *dicta* from *de Penitentia*), and second (all R2 *dicta*,
excluding those from *de Penitentia*).[^b4] For each of the fourteen
subcorpora, we will hypothesize each subcorpus in turn to be the
work of an unknown author, and will treat the other thirteen
subcorpora as composing a corpus of works by a known author. The
scale of the fourth experiment is similar to that of the experiments
carried out by John Burrows and David Hoover, the pioneers of the
technique, but makes it impractical to show intermediate results
at every step in the process.

[^b1]: @burrows_questions_2003; and -@burrows_delta_2002.

[^b3]: *de Penitentia* D.1 c.88 (R1), D.3 c.42 (R1), D.3 c.49 (R1),
D.5 c.1 (R1), D.6 c.1 (R1), and D.7 c.6 (R1). These seven extended
passages average 554.4 words in length. **See edF 1.XXXV, for a
complete list of passages from *De vera et falsa penitentia* quoted
in the *Decretum*. Explain rationale for omitting certain passages:
D.25 c.5 (R2 or Palea), *de Penitentia* D.3 c.4.5 (what Friedberg
means by 4.5 in this context is unclear), D.3 c.45 (R2). Acknowledge
Karen Teresa Wagner, *De vera et falsa penitentia : an edition and
study*, 1995.**

[^b4]: The division of the first-recension (R1) *dicta* into twelve
sections follows the division of Gratian's *Decretum* proposed by
Alfred Beyer in -@beyer_lokale_1998, 17-18.

