---
author: Paul Evans
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
date: 19 February 2020
date: 18 March 2020
date: 5 May 2020
date: 13 May 2020
suppress-bibliography: false
title: Chapter 4
subtitle: Definition of first- and second-recension *dicta*
abstract: |
  In the absence of good modern critical editions of the first and
  second recensions of the *Decretum*, a **proxy** for the first
  recension is created by applying the annotations in Winroth's
  appendix as a transform to Friedberg's text. The **proxy** for
  the first recension is then subtracted from Friedberg's text,
  leaving text from the second recension as the difference. The
  text samples from the first and second recensions of the *Decretum*
  that provide the basis for authorship attribution are build up
  by iteratively appending short units of text (the individual
  first- and second-recension *dicta*) that are **non-contiguous**
  in the original context of the *Decretum*.
---
Many of the examples in this chapter will distinguish between first-
and second-recension *dicta*, so this is an appropriate point at
which to introduce an explicit definition for the way in which those
terms will be used in the following discussion. Because almost every
word in the first-recension *dicta* corresponds to a word in the
second-recension *dicta*, we could consider the first-recension
*dicta* to be a subset of the second-recension *dicta*, and conversely,
we could consider the second-recension *dicta* to be a superset of
the first-recension *dicta*. While true enough from a commonsensical
point of view, this is not a useful definition for the kinds of
questions we would like to be able ask and answer, such as whether
Gratian 1, the author of the first-recension *dicta*, is the same
person as Gratian 2, the author of the second-recension *dicta*.

Instead, for the purpose of the following analyses, the second-recension
*dicta* are defined as the ordered set of every word from the *dicta*
in the text of Friedberg's 1879 edition of Gratian's *Decretum* for
which there is not a one-to-one correspondence to a word in the
first-recension *dicta* as defined by Anders Winroth's appendix
"The Contents of the First Recension of Gratian's *Decretum*".[^d1]
An alternative restatement would be to define the second-recension
*dicta* as the difference left by subtracting all of the words
of the first-recension *dicta* as defined by Winroth's appendix
from the text in the Friedberg edition. This definition is implemented
by passing sequentially through the *dicta* and applying the following
three rules:

+ If a *dictum* is listed in Winroth's appendix as being in the
first recension of the *Decretum*, and as not having been added to
or changed in the second recension, the text for that *dictum* is
included in the first recension sample. This rule is applied on a
per-*dictum* basis.

+ If a *dictum* is in the text of the Friedberg edition, and is not
listed in Winroth's appendix as being in the first recension, in
either unmodified or modified form, the text for that *dictum* is
included in the second recension sample. This rule is applied on a
per-*dictum* basis.

+ If a *dictum* is listed Winroth's appendix as being in the first
recension, but as having been added to or changed in the second
recension, those words indicated by the appendix are included in
the first recension sample, while those words in the text of Friedberg
not corresponding to the words indicated by the appendix are included
in the second recension sample. This rule is applied on a word-by-word
basis.

Take D.54 d.p.c.23 as an example. The complete text of the *dictum*
as it appears in the Friedberg edition (column 214) is:

> *Ecce, quomodo serui ad clericatum ualeant assumi, uel quomodo
> non admittantur. Liberti quoque non sunt promouendi ad clerum,
> nisi ab obsequiis sui patroni fuerint absoluti. Unde in Concilio
> Eliberitano:*

Winroth's appendix indicates that only the first sentence of the
*dictum* appears in the first recension:

d.p.c. 23: **1** *Ecce quomodo serui* – **2** *quomodo non
admittantur.*[^d2]

Therefore, "*Ecce, quomodo serui ad clericatum ualeant assumi, uel
quomodo non admittantur.*" is included in the first recension text
sample, and "*Liberti quoque non sunt promouendi ad clerum, nisi
ab obsequiis sui patroni fuerint absoluti. Unde in Concilio
Eliberitano:*" is included in the second recension text sample.

Note that the individual *dicta* are too short for direct analysis
by the techniques discussed in this chapter. The smallest unit of
Latin prose for which computational stylometry works is about 2,500
words.[@eder_does_2015, 171] The longest first-recension *dictum*
(*de Pen*. D.1 d.p.c.87) is 1,591 words, and the longest second-recension
*dictum* (C.7 q.1 d.p.c.48) is 692 words. As a result, first and
second recension samples long enough for analysis have to be created
by rolling up or concatenating the first and second recension *dicta*
as they occur sequentially but discontinuously throughout the
*Decretum*.

Both the text of Friedberg's 1879 edition of Gratian's *Decretum*
and Winroth's appendix are potentially open to criticism.[^d4] Winroth
himself acknowledged the provisional nature of his appendix,[^d5]
and Pennington has pointed out at least one interesting substantive
problem, the inclusion of D.101. Nevertheless, in the absence of a
critical edition for the first recension, creating a **proxy** for
the text of the first recension by applying the information in
Winroth's appendix as a set of transforms to the text of Friedberg's
edition is the most workable approach. The resulting **proxy** for
the first-recension text can then be subtracted from Friedberg's
text to create a text representing second-recension additions and
changes. Furthermore, this approach has one extremely powerful
argument in its favor, which is that it enables reproducibility.
Reliance on publicly available data means that those who wish to
reproduce these results are not dependent on private decisions about
the content of the text samples.

Depending on the nature of the analysis we wish to conduct, we may
choose to either include or exclude the *dicta* from *de Penitentia*.
Including the *dicta* from *de Penitentia*., there are 897 *dicta*
represented in the first-recension text sample and 419 represented
in the second-recension sample. Of those, 65 *dicta* are represented
in both the first- and second-recension samples. Excluding the
*dicta* from *de Penitentia*., there are 836 first-recension and
398 second-recension *dicta*, of which 61 *dicta* are represented
in both samples.

[^d1]: @winroth_making_2000, 197-227.

[^d2]: @winroth_making_2000, 201. The numbers 1 and 2 refer to line
numbers relative to the first line of the *dictum*, as opposed to
the first line of the column, in the print version of the Friedberg
edition.

[^d4]: [@kuttner_gratiani_1948] The article, and not just the title,
is in Latin.  @kuttner_research_1990, 10, 21-22.  **Add Anders
Winroth, "Recent Work on the Making of Gratian's *Decretum*",
24-25.** The latter articles two mention the deficiency of Friedberg's
edition without offering detailed critiques.

[^d5]: "The list is based on a collation of *incipits* and
*explicits* of every canon and *dictum* in the first recension. Differences
within the texts may very well have been overlooked, and minor differences
have not normally been registered." @winroth_making_2000, 197.

