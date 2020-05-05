---
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
suppress-bibliography: false
title: Chapter 4
subtitle: Definition of first- and second-recension *dicta*
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
in the MGH e-text of Friedberg's 1879 edition of Gratian's *Decretum*
for which there is not a one-to-one correspondence to a word in the
first-recension *dicta* as defined by Anders Winroths's appendix
"The Contents of the First Recension of Gratian's *Decretum*".[^d1]
An alternative restatement would be to define the second-recension
*dicta* as the difference left by subtracting all of the words
of the first-recension *dicta* as defined by Winroth's appendix
from the e-text if the Friedberg edition. This definition is applied
concretely in the form of the three following rules:

+ If a *dictum* is listed in Winroth's appendix as being in the
first recension of the *Decretum*, and as not having been added to
or changed in the second recension, the e-text for that *dictum*
is included in the first recension sample. This rule is applied on
a per-*dictum* basis.

+ If a *dictum* is in the e-text of the Friedberg edition, and is
not listed in Winroth's appendix as being in the first recension,
in either unmodified or modified form, the e-text for that *dictum*
is included in the second recension sample. This rule is applied
on a per-*dictum* basis.

+ If a *dictum* is listed Winroth's appendix as being in the first
recension, but as having been added to or changed in the second
recension, words indicated by the appendix are included in the first
recension sample, while words in the e-text of Friedberg not
corresponding to the words indicated by the appendix are included
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

Both the MGH e-text of Friedberg's 1879 edition of Gratian's
*Decretum* and Winroth's appendix are potentially open to criticism.
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
resurrexit uera carnis*."[^d3]

Winroth himself acknowledged the provisional nature of his appendix,[^d4]
and Pennington has pointed out at least one interesting substantive
problem, the inclusion D.101. Nevertheless, in the absence of a
critical edition for the first recension, creating a **proxy** for
the text of the first recension by applying the information in
Winroth's appendix as a set of transforms on the e-text of Friedberg's
edition is the most workable approach. The resulting **proxy** for
the first-recension text can then be subtracted from the Friedberg
e-text to create a text representing second-recension additions and
changes. Furthermore, this approach has one extremely powerful
argument in its favor, which is that it enables reproducibility.
Reliance on a public data set means that anyone who wishes to
reproduce these results is not dependent on private decisions about
the content of the text samples.

Depending on the nature of the analysis we wish to conduct, we may
choose to either include or exclude the *dicta* from *de Pen*.
Including the *dicta* from *de Pen*., there are 897 *dicta* represented
in the first-recension text sample and 419 represented in the
second-recension sample. Of those, 65 *dicta* are represented in
both the first- and second-recension samples. Excluding the *dicta*
from *de Pen*., there are 836 first-recension and 398 second-recension
*dicta*, of which 61 *dicta* are represented in both samples.

[^d1]: @winroth_making_2000, 197-227.

[^d2]: @winroth_making_2000, 201. The numbers 1 and 2 refer to line
numbers relative to the first line of the *dictum*, as opposed to
the first line of the column, in the print version of the Friedberg
edition.

[^d3]: Thanks to Anders Winroth for bringing the instance of
homeoteleuton at D.23 c.2 in the MGH e-text to my attention (August
23, 2019). Clemens Radl of the MGH confirmed to Winroth that the
e-text was typed.

[^d4]: "The list is based on a collation of *incipits* and *explicits* of
every canon and *dictum* in the first recension. Differences within
the texts may very well have been overlooked, and minor differences
have not normally been registered." @winroth_making_2000, 197.

