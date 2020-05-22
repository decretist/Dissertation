---
author: Paul Evans
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
date: 21 May 2020
suppress-bibliography: false
title: Chapter 4
subtitle: Definition and Corpus Preparation
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
### Definition of first- and second-recension *dicta*

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
"The Contents of the First Recension of Gratian's
*Decretum*".[@winroth_making_2000, 197-227] An alternative restatement
would be to define the second-recension *dicta* as the difference
left by subtracting all of the words of the first-recension *dicta*
as defined by Winroth's appendix from the text in the Friedberg
edition. This definition is implemented by passing sequentially
through the *dicta* and applying the following three rules:

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
admittantur.*[^m2]

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
and Winroth's appendix are potentially open to criticism. Although
modern scholars admire Friedberg's learning and energy --- the 1879
edition of the *Decretum* was only one of many such projects that
he undertook --- his editorial standards were those of 140 years
ago. In particular, Friedberg's selection of eight unrepresentative
German manuscripts as the basis for his edition, and his particular
reliance on two of them --- Köln Erzbischöfliche Diözesan- und
Dombibliothek 127 (Ka) and 128 (Kb) --- are seen today as serious
deficiencies.[^m4]

Winroth himself acknowledged the provisional nature of his
appendix.[^m5] Furthermore, Pennington has pointed out that although
Winroth's appendix includes D.100 d.a.c.1, D.100 c.1, and D.101
d.p.c.1, in the Paris (P), Florence (Fd), and Barcelona (Bc)
manuscripts, the text of the first recension ends with D.99
c.1.[@pennington_biography_2014, 685]

Nevertheless, in the absence of a critical edition for the first
recension, creating a **proxy** for the text of the first recension
by applying the information in Winroth's appendix as a set of
transforms to the text of Friedberg's edition is the most workable
approach. The resulting **proxy** for the first-recension text can
then be subtracted from Friedberg's text to create a text representing
second-recension additions and changes.

This approach---applying the variants recorded in Winroth's appendix
to Friedberg's vulgate text to generate a stand-in or proxy for the
first recension---is consistent with the approach I have taken
throughout my dissertation project. Winroth himself took a similar
approach when he created the baseline text for the edition in
progress of the first recension (although he imposed a set of
orthographic conventions different from Friedberg's on the resulting
text). Regardless of how Winroth conceptualized what he was doing,
it is an approach that is well-theorized in a Digital Humanities
context as an example of "deformance." The term, proposed by Lisa
Samuels and Jerome McGann in "Deformance and Interpretation" (1999),
conflates the words "deformation" and "performance", and describes
a process through which a text is transformed by the application
of a series of deformances to generate a "paratext".
[@samuels_deformance_1999] The paratext is different from the
original text, but defined by the deformances through which it was
generated from it, and can be analyzed for otherwise unavailable
insights into the original text.

Furthermore, this approach has one extremely powerful argument in
its favor, which is that it enables reproducibility. Reliance on
publicly available data means that those who wish to reproduce these
results are not dependent on private decisions about the content
of the text samples.

Depending on the nature of the analysis we wish to conduct, we may
choose to either include or exclude the *dicta* from *de Penitentia*.
Including the *dicta* from *de Penitentia*., there are 897 *dicta*
represented in the first-recension text sample and 419 represented
in the second-recension sample. Of those, 65 *dicta* are represented
in both the first- and second-recension samples. Excluding the
*dicta* from *de Penitentia*., there are 836 first-recension and
398 second-recension *dicta*, of which 61 *dicta* are represented
in both samples.

### Corpus preparation

The most important and time-consuming aspect of any digital humanities
project is corpus preparation. The availability of a suitable corpus
of electronic texts is a baseline requirement for carrying out
stylometric analysis. The ideal textual basis for a project of this
nature would be a set of electronic texts of good modern critical
editions of both the first and second recensions of Gratian’s
*Decretum*, following consistent orthographic conventions, and
adhering to a widely-accepted encoding standard such as the XML
Text Encoding Initiative (TEI P5) format. The Mellon Foundation-supported
effort directed by Anders Winroth to edit the first recension is
ongoing, but work on Winroth's edition in progress had not reached
a sufficiently advanced state of completion for it to be used within
the time frame available for my project.

As a result, this investigation depends for both the first and the
second recension on the electronic text of the Friedberg edition
that Timothy Reuter and Gabriel Silagi used to produce the
*Wortkonkordanz zum Decretum Gratiani* for the
MGH.[@reuter_wortkonkordanz_1990] Anders Winroth and Lou Burnard
of the Oxford Text Archive (OTA) provided copies of the MGH e-text
separately. The copies differed significantly, and the e-text had
to be reconstructed through an editorial process quite similar to
preparing a critical edition to restore it to a state as close as
possible to what Reuter and Silagi presumably intended.

In 1946, Father Roberto Busa, SJ (d. 2011), began work on what
ultimately became the *Index Thomisticus*, a concordance of the
works of St Thomas Aquinas. In 1949, Father Busa secured crucial
support from Thomas J. Watson of IBM, allowing concordance generation
to be carried out by means of electro-mechanical and later electronic
computers operating on punch-card data. The *Index Thomisticus* is
recognized today as the first important humanities computing project,
and figures prominently in origin stories for digital humanities
as a discipline.[^m9] The success of Father Busa's project inspired a
number of imitators, as well as the development of specialized
software and data formats to support such efforts. Reuter and
Silagi's *Wortkonkordanz* was probably the last major Busa-style
concordance. For this reason, the MGH e-text of the Friedberg
edition was encoded in the obsolete Oxford Concordance Program (OCP)
format.

The MGH e-text introduced a small number of textual errors in
addition to those it inherited from printed version of Friedberg's
edition.

+---------------+----------+-----------------------------------------------+-------------------------------------------------------------------+
| Citation      |   Column | Error                                         | Correction                                                        |
+===============+==========+===============================================+===================================================================+
| D.6 d.p.c.3   |       11 | quantam ad moralem intelligentiam             | quantum ad moralem intelligentiam                                 |
+---------------+----------+-----------------------------------------------+-------------------------------------------------------------------+
| D.23 c.2      |       79 |                                               | carnis passione, mortuus uera corporis sui morte, resurrexit uera |
+---------------+----------+-----------------------------------------------+-------------------------------------------------------------------+
| D.54 d.p.c.22 |      214 | Quid autem serui ecclesiarum                  | Quod autem serui ecclesiarum                                      |
+---------------+----------+-----------------------------------------------+-------------------------------------------------------------------+
| C.2 q.6 c.41  |      483 | contra sententiam restitutionem inpetraverit  | contra sententiam restitutionem inpetrauerit                      |
+---------------+----------+-----------------------------------------------+-------------------------------------------------------------------+
| C.4 d.init.   |      536 | a communione ait remouendus                   | a communione sit remouendus                                       |
+---------------+----------+-----------------------------------------------+-------------------------------------------------------------------+
| C.4 d.init.   |      536 | in episcoporum indicio                        | in episcoporum iudicio                                            |
+---------------+----------+-----------------------------------------------+-------------------------------------------------------------------+
| C.7 d.init.   |      566 | Quidam longa inualetudinem grauatus episcopus | Quidam longa inualetudine grauatus episcopus                      |
+---------------+----------+-----------------------------------------------+-------------------------------------------------------------------+

Contrary to the widespread belief that the MGH e-text was created
by scanning a physical copy of the Friedberg edition using optical
character recognition (OCR) technology and then correcting the
results, it is the product of keyboard transcription. Conclusively,
the e-text contains at least one instance of homeoteleuton. The
following fours lines from the text of D.23 c.2 in the Friedberg
edition (column 79):

> *Patre et Spiritu sancto omnium creaturarum; qui passus  
> sit pro salute nostra uera carnis **passione, mortuus uera  
> corporis sui morte, resurrexit uera carnis** suae receptione  
> et uera animae resumptione, in qua ueniat iudicare*  

were transcribed as the following three lines in the e-text:

> *Patre et Spiritu sancto omnium creaturarum; qui passus  
> sit pro salute nostra uera carnis suae receptione  
> et uera animae resumptione, in qua ueniat iudicare*  

skipping over the words "*passione, mortuus uera corporis sui morte,
resurrexit uera carnis*."[^m10]

---

Notwithstanding the highly specialized and outdated requirements it was originally created to meet, the MGH e-text has had a healthy afterlife.[@winroth_uncovering_1997]

The OCP format is very difficult to parse because it is not
tree-structured---it has start tags for elements such as canons and
*dicta*, cases and distinctions, but not end tags.[@hockey_history_2004]

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
edition.[^m14]

[^m2]: @winroth_making_2000, 201. The numbers 1 and 2 refer to line
numbers relative to the first line of the *dictum*, as opposed to
the first line of the column, in the print version of the Friedberg
edition.

[^m4]: @winroth_making_2000, 9-11. See also @kuttner_gratiani_1948
(Latin), and -@kuttner_research_1990, 10, 21-22, which mentions the
deficiency of Friedberg's edition without offering a detailed
critique.

[^m5]: "The list is based on a collation of *incipits* and
*explicits* of every canon and *dictum* in the first recension. Differences
within the texts may very well have been overlooked, and minor differences
have not normally been registered." @winroth_making_2000, 197.

[^m9]: [@hockey_history_2004, 4-6]. The highest honor in the field
of Digital Humanities is the Roberto Busa Prize, awarded by the
Alliance of Digital Humanities Organizations (ADHO). A notable past
recipient of the Busa Prize is John Burrows, who first introduced
the fundamental stylometric technique now known as Burrows's Delta
in a lecture he delivered on the occasion of receiving the award
in 2001.

[^m10]: Thanks to Anders Winroth for bringing the instance of
homeoteleuton at D.23 c.2 in the MGH e-text to my attention (August
23, 2019). Clemens Radl of the MGH confirmed to Winroth that the
e-text was typed.

[^m14]: **This is perhaps not entirely satisfactory. It would be
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
component analyses include any of these 13 words, so the use of the
vulgate rather than a proxy first-recension version of the text of
C.19 d.init. has no effect on the outcome of these tests.**

