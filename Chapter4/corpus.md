---
author: Paul Evans
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
date: 13 May 2020
suppress-bibliography: false
title: Chapter 4
subtitle: Corpus preparation
---
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
the time frame available for my project. As a result, this investigation
depends for both the first and the second recension on the electronic
text of the Friedberg edition that Timothy Reuter and Gabriel Silagi
used to produce the *Wortkonkordanz zum Decretum Gratiani* for the
MGH.[@reuter_wortkonkordanz_1990]

In 1946, Father Roberto Busa, SJ (d. 2011), began work on what
ultimately became the *Index Thomisticus*, a concordance of the
works of St Thomas Aquinas. In 1949, Father Busa secured crucial
support from Thomas J. Watson of IBM, allowing concordance generation
to be carried out by means of electro-mechanical and later electronic
computers operating on punch-card data. The *Index Thomisticus* is
recognized today as the first important humanities computing project,
and figures prominently in origin stories for digital humanities
as a discipline.[^busa]  The success of Father Busa's project inspired a
number of imitators, as well as the development of specialized
software and data formats to support such efforts. Reuter and
Silagi's *Wortkonkordanz* was probably the last major Busa-style
concordance. For this reason, the MGH e-text of the Friedberg
edition was encoded in the obsolete Oxford Concordance Program (OCP)
format.

[^busa]: [@hockey_history_2004, 4-6]. The highest honor in the field
of Digital Humanities is the Roberto Busa Prize, awarded by the
Alliance of Digital Humanities Organizations (ADHO). A notable past
recipient of the Busa Prize is John Burrows, who first introduced
the fundamental stylometric technique now known as Burrows's Delta
in a lecture he delivered on the occasion of receiving the award
in 2001.

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

Anders Winroth and Lou Burnard of the Oxford Text Archive (OTA)
provided copies of the MGH e-text separately. The copies differed
significantly, and the e-text had to be reconstructed through an
editorial process quite similar to preparing a critical edition to
restore it to a state as close as possible to what Reuter and
Silagi presumably intended.

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
edition.[^c3]

[^d3]: Thanks to Anders Winroth for bringing the instance of
homeoteleuton at D.23 c.2 in the MGH e-text to my attention (August
23, 2019). Clemens Radl of the MGH confirmed to Winroth that the
e-text was typed.

[^c3]: **This is perhaps not entirely satisfactory. It would be
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

