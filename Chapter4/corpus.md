---
author: Paul Evans
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
date: 13 May 2020
suppress-bibliography: false
title: Chapter 4
subtitle: Corpus preparation
---
An important (and time-consuming) aspect of any project of this
nature is corpus preparation. A baseline requirement for carrying
out stylometric analysis is the availability of an electronic text.
Ideally, I would be working with electronic texts of good critical
editions of both the first and second recensions of Gratian's
*Decretum*, following consistent orthographic conventions, and
encoded in a standard format like TEI P5 XML. The Mellon
Foundation-supported project, directed by Anders Winroth, to edit
the first recension is making good progress, but is not yet complete
enough for me to use on this project. So, I am working with the
electronic text of the Friedberg edition that Timothy Reuter and
Gabriel Silagi used to produce the *Wortkonkordanz zum Decretum
Gratiani* for the MGH. [@reuter_wortkonkordanz_1990] The MGH e-text
is encoded in the obsolete Oxford Concordance Program format.

Anders Winroth and Lou Burnard of the Oxford Text Archive (OTA)
each provided me with copies of the MGH e-text. The copies differed,
and I went through an exercise not unlike preparing a critical
edition to restore the e-text to the state that Reuter and Silagi
intended.

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

