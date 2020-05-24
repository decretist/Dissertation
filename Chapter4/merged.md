---
author: Paul Evans
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
date: 24 May 2020
suppress-bibliography: false
title: Chapter 4
subtitle: Definition and Corpus Preparation
abstract: |
  In the absence of good modern critical editions for the first and
  second recensions of the *Decretum*, a proxy for the first recension
  is created by applying the variants recorded in Winroth's appendix
  as transformations to Friedberg's text. The proxy for the first
  recension is then subtracted from Friedberg's text, leaving text
  from the second recension as the difference. The text samples
  from the first and second recensions of the *Decretum* that provide
  the basis for authorship attribution are build up by iteratively
  appending short units of text (the individual first- and
  second-recension *dicta*) that are non-contiguous in the original
  context of the *Decretum*.
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
by the techniques discussed in this chapter.[^m3] The smallest unit of
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
deficiencies.[^m5]

Winroth himself acknowledged the provisional nature of his
appendix.[^m6] Furthermore, Pennington has pointed out that although
Winroth's appendix includes D.100 d.a.c.1, D.100 c.1, and D.101
d.p.c.1, in the Paris (P), Florence (Fd), and Barcelona (Bc)
manuscripts, the text of the first recension ends with D.99
c.1.[@pennington_biography_2014, 685]

Nevertheless, in the absence of a critical edition for the first
recension, applying the variants recorded in Winroth's appendix as
a set of transformations to the text of Friedberg's edition to
generate a stand-in or proxy for the text of the first recension
is a workable approach.[^m8] This method is well-theorized in a
Digital Humanities context as an example of "deformance." The term,
proposed by Lisa Samuels and Jerome McGann in "Deformance and
Interpretation" (1999), conflates the words "deformation" and
"performance", and describes a process through which a text is
transformed by the application of a series of deformances to generate
a "paratext". [@samuels_deformance_1999] The paratext is different
from the original text, but defined by the deformances through which
it was generated from it, and can be analyzed for otherwise unavailable
insights into the original text.

The methodology for producing the text samples used in this project
involves multiple stages of deformance. Starting with Friedberg's
1879 edition of Gratian's *Decretum* as the text, Winroth's appendix,
which compactly encodes first-recension variants with respect to
Friedberg, is used as a program (literally, as will be seen in the
section on corpus preparation below) for deforming Friedberg's text
to produce the first paratext, the proxy first recension *dicta*.
The first paratext is then used as the basis for a second deformation,
by which the first paratext is subtracted from Friedberg's text to
create the second paratext representing second recension additions
and changes to the *dicta*.

The approach of deriving all of the text samples used in this study
using only Friedberg's text and the first-recension variants recorded
in Winroth's appendix as sources has one final argument in its
favor, which is that it enables reproducibility. Reliance on publicly
available data means that those who wish to reproduce these results
are not dependent on private decisions about the content of the
text samples.

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
the time frame available for my project.[^m10]

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
as a discipline.[^m12] The success of Father Busa's project inspired
a number of imitators, as well as the development of specialized
software and data formats to support such efforts. Reuter and
Silagi's *Wortkonkordanz* was probably the last major Busa-style
concordance. For this reason, the MGH e-text of the Friedberg edition
was encoded in the obsolete Oxford Concordance Program (OCP) format.

The MGH e-text introduced a small number of textual errors in
addition to those it inherited from printed version of Friedberg's
edition. The table below lists all currently known errors in the
MGH e-text:[^m13]

| Citation      |   Column | Error                                         | Correction                                                        |
|:--------------|---------:|:----------------------------------------------|:------------------------------------------------------------------|
| D.6 d.p.c.3   |       11 | quantam ad moralem intelligentiam             | quantum ad moralem intelligentiam                                 |
| D.23 c.2      |       79 |                                               | carnis passione, mortuus uera corporis sui morte, resurrexit uera |
| D.54 d.p.c.22 |      214 | Quid autem serui ecclesiarum                  | Quod autem serui ecclesiarum                                      |
| C.2 q.6 c.41  |      483 | contra sententiam restitutionem inpetraverit  | contra sententiam restitutionem inpetrauerit                      |
| C.4 d.init.   |      536 | a communione ait remouendus                   | a communione sit remouendus                                       |
| C.4 d.init.   |      536 | in episcoporum indicio                        | in episcoporum iudicio                                            |
| C.7 d.init.   |      566 | Quidam longa inualetudinem grauatus episcopus | Quidam longa inualetudine grauatus episcopus                      |

The error in D.23 c.2 is particularly noteworthy. Contrary to the
widespread belief that the MGH e-text was created by scanning a
physical copy of the Friedberg edition using optical character
recognition (OCR) technology and then correcting the results, it
is the product of keyboard transcription. Conclusively, the e-text
contains at least one instance of homeoteleuton. The following fours
lines from the text of D.23 c.2 in the Friedberg edition (column
79):

> *Patre et Spiritu sancto omnium creaturarum; qui passus  
> sit pro salute nostra uera carnis **passione, mortuus uera  
> corporis sui morte, resurrexit uera carnis** suae receptione  
> et uera animae resumptione, in qua ueniat iudicare*  

were transcribed as the following three lines in the e-text:

> *Patre et Spiritu sancto omnium creaturarum; qui passus  
> sit pro salute nostra uera carnis suae receptione  
> et uera animae resumptione, in qua ueniat iudicare*  

skipping over the words "*passione, mortuus uera corporis sui morte,
resurrexit uera carnis*."[^m14]

Notwithstanding its textual flaws and the highly specialized and
outdated requirements that constrained the choice of file format,
the MGH e-text remains a useful tool for the study of Gratian's
*Decretum*.[@winroth_uncovering_1997]

The deformance algorithm used to generate the paratexts described
in the previous section on the definition of the first- and
second-recension *dicta* was implemented in the form of a 201-line
Python program. The program reads the MGH e-text of the Friedberg
edition, and parses it to extract the *dicta*. The Oxford Concordance
Program (OCP) format in which the e-text is encoded is extremely
difficult to parse because it is not tree-structured---it has start
tags for textual elements such as canons and *dicta*, cases and
distinctions, but not (unlike XML) end tags.[@hockey_history_2004]
The extraction engine captures every element of text between a
*dictum* start tag (`<T A>` or `<T P>`) and the start tag for the
next element that can possibly follow a *dictum*:

```python
import re

f = open('edF.txt', 'r')
file = f.read()
# (?<=...) positive lookbehind assertion.
dicta = re.findall('(?:\<T [AP]\>|(?<=\<T [AP]\>))(.*?)'    # dictum starts with dictum ante or dictum post tag.
    '(?:'                   # non-capturing group.
        '\<1 [CD][CP]?\>|'  # dictum ends with major division,
        '\<2 \d{1,3}\>|'    # or number of major division,
        '\<3 \d{1,2}\>|'    # or number of question,
        '\<4 \d{1,3}\>|'    # or number of canon,
        '\<P 1\>|'          # or Palea,
        '\<T [AIPRT]\>'      # or inscription or text tag.
    ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline.
```

The extracted *dicta* require considerable scrubbing before they
can be used. Here, for example, is what D.54 d.p.c.23 looks like
in its raw state:

```python
[' -Gratian.+ Ecce, quomodo serui ad clericatum ualeant assumi,\n
uel quomodo non admittantur. Liberti quoque non sunt promouendi\n
ad clerum, nisi ab obsequiis sui patroni fuerint absoluti.\n
Unde in Concilio Eliberitano: -[c. 80.]+\n']
```

Each *dictum* is then processed into an item (key-value pair) in a
Python dictionary:

```python
{'D.54 d.p.c.23': 'Ecce, quomodo serui ad clericatum ualeant assumi, uel quomodo non admittantur. Liberti quoque non sunt promouendi ad clerum, nisi ab obsequiis sui patroni fuerint absoluti. Unde in Concilio Eliberitano:'}
```

The first recension variants from the Friedberg edition recorded
in Winroth's appendix are then encoded as a list of dictionaries
in which the `'pattern'` item is the variant represented as a Python
regular expression:

```python
[{'key': 'D.54 d.p.c.23', 'pattern': '(Ecce, quomodo serui.*?quomodo non admittantur\.)'}]
```

Finally, the deformance engine uses the variants encoded as regular
expression patterns to generate the first and second paratexts
corresponding the first- and second-recension *dicta*. For each
*dictum*, the text matching the pattern is inserted into a dictionary
representing the first recension paratext; then the text resulting
when the text matching the pattern is replaced by the null string
`''` is inserted into a dictionary representing the second
recension paratext:

```python
import re

dictionary_1r = {} # first recension paratext
dictionary_2r = {} # second recension paratext
dictionary_Fr = {'D.54 d.p.c.23': 'Ecce, quomodo serui ad clericatum ualeant assumi, uel quomodo non admittantur. Liberti quoque non sunt promouendi ad clerum, nisi ab obsequiis sui patroni fuerint absoluti. Unde in Concilio Eliberitano:'}
keysandpatterns = [{'key': 'D.54 d.p.c.23', 'pattern': '(Ecce, quomodo serui.*?quomodo non admittantur\.)'}]
for i in range (len(keysandpatterns)):
    key = keysandpatterns[i]['key']
    pattern = keysandpatterns[i]['pattern']
    result = re.search(pattern, dictionary_Fr[key])
    dictionary_1r[key] = result.group(1)
    dictionary_2r[key] = re.sub(pattern, '', dictionary_Fr[key])
```

Here is the resulting first recension paratext:

```python
{'D.54 d.p.c.23': 'Ecce, quomodo serui ad clericatum ualeant assumi, uel quomodo non admittantur.'}
```
and the corresponding second recension paratext:

```python
{'D.54 d.p.c.23': 'Liberti quoque non sunt promouendi ad clerum, nisi ab obsequiis sui patroni fuerint absoluti. Unde in Concilio Eliberitano:'}
```

[^m2]: @winroth_making_2000, 201. The numbers 1 and 2 refer to line
numbers relative to the first line of the *dictum*, as opposed to
the first line of the column, in the print version of the Friedberg
edition.

[^m3]: **This paragraph may have to be moved to a separate section
explaining the rationale for the various roll-ups of the *dicta*
used in the following analyses, e.g., Gratian0, Gratian1, dePen,
Gratian2, etc.**

[^m5]: @winroth_making_2000, 9-11. See also @kuttner_gratiani_1948
(Latin), and -@kuttner_research_1990, 10, 21-22, which mentions the
deficiency of Friedberg's edition without offering a detailed
critique.

[^m6]: "The list is based on a collation of *incipits* and
*explicits* of every canon and *dictum* in the first recension. Differences
within the texts may very well have been overlooked, and minor differences
have not normally been registered." @winroth_making_2000, 197.

[^m8]: **Anders, my understanding is that you took a similar approach
when you created the baseline text for the edition in progress of
the first recension (although you adopted a set of orthographic
conventions different from Friedberg's in the resulting text).**

[^m10]: As of the most recent, 22 April 2019, version, eight case
statements (for cases 1-3, 9, 15, 24, 30, and 34) appear to have a
complete critical apparatus. An addition six case statements (for
cases 4-7, 10, and 11) have an incomplete critical apparatus that
records variant readings from Fd only. The critical apparatus for
the case statement for case 35 records a single variant reading
from Aa. The remaining 21 case statements (for cases 8, 12-14,
16-23, 25-29, 31-33, and 36) have no critical apparatus at all.

    **Update for 5 October 2019 version of the edition in progress.
    The case statement are used as the example here because they
    are the focus of my dissertation.**

[^m12]: [@hockey_history_2004, 4-6]. The highest honor in the field
of Digital Humanities is the Roberto Busa Prize, awarded by the
Alliance of Digital Humanities Organizations (ADHO). A notable past
recipient of the Busa Prize is John Burrows, who first introduced
the fundamental stylometric technique now known as Burrows's Delta
in a lecture he delivered on the occasion of receiving the award
in 2001.

[^m13]: Data current as of 23 May 2020. For more recent error reports,
see the list I maintain for the Stephan Kuttner Institute on
[GitHub](https://github.com/StephanKuttnerInstitute/FriedbergBugs/blob/master/bug-reports.csv).
Thanks to Anders Winroth for reporting the errors in D.6 d.p.c.3
(6 October 2019) and D.23 c.2 (23 August 2019).

[^m14]: Thanks to Anders Winroth for bringing the instance of
homeoteleuton at D.23 c.2 in the MGH e-text to my attention (August
23, 2019). Clemens Radl of the MGH confirmed to Winroth that the
e-text was typed.

