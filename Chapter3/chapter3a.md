---
author: Paul Evans
date: January 14, 2021
title: Chapter 3
subtitle: Work in progress
---
The last time we talked, I indicated that chapter 3 on Gratian was
the one non-technical chapter you have not yet reviewed. My thinking
on chapter 3 has evolved considerably over the last month, so I
wanted to update you, partly as a way to clarify my current view
of the problem for my own benefit.

When I started writing the non-technical chapters in June 2017, I
hesitated about whether to start with Gratian or with the *Decretum*.
I eventually decided that it would be better to start with the
*Decretum* than with Gratian since we know much more about the
*Decretum* than we do about Gratian, and most of what we do know
about Gratian, we know through the *Decretum* (quote John Wei). The
chapter that followed from the decision to start with the *Decretum*
is the one we read and discussed with the HIGR 295 participants in
November 2017.

The purpose of the Gratian chapter in the original dissertation
outline was limited and clearly defined: to show that there was no
information in the known biography of Gratian, either from modern
scholarship (Noonan, Grebner, Winroth, and Pennington) or from
evidence left by near-contemporaries (i.e, the authors of the
prefaces of twelfth-century *summae* on the *Decretum*), that
contradicted or precluded the possibility that the case statements
and *dicta* had different authors. (quote Chodorow) To the extent
that I intended to review the evidence left by near-contemporaries,
I was mainly interested in the question of whether any of the
decretist authors of the prefaces to the *summae* suggested that
they had been students of Gratian or otherwise had first-hand
knowledge of the circumstances under which the *Decretum* had been
compiled. The conclusion of the first draft of the Gratian chapter
was that no near-contemporary makes an unambiguous claim to have
been Gratian's student or to otherwise have had first-hand knowledge
of the circumstances under which the *Decretum* was compiled, and
that nothing in modern scholarship precludes or contradicts the
possibility that the *Decretum* was a product of collective or group
authorship.

From 2012 to 2014, I worked as a graduate research assistant for
the Maryland Institute for Technology in the Humanities (MITH) at
the University of Maryland, one of the foremost centers for Digital
Humanities research in the US. In November 2014, I presented my
preliminary findings on the authorship of Gratian's *Decretum* to
a brown-bag seminar attended by members of the MITH staff, mostly
English and Information School faculty plus staff members holding
appointments in the UMD library system. As is quite common in the
Digital Humanities community, the primary academic expertise of the
faculty members present was in nineteenth-century English literature
(for example, Neil Fraistat, the director of MITH at the time, is
a leading authority on Keats, Shelley, and Byron). For the benefit
of the non-medievalist audience, I presented the problem I was
investigating in a simplified (though I believe not over-simplified)
form. Using a physical copy of the Friedberg edition of the *Decretum*
as a prop, I made the following points:

+ That the *Decretum* was a twelfth-century university textbook for
the study of canon law, the law of the Roman Catholic church.

+ That the *Decretum* was written in Latin (I had reason to know
that that would not be obvious to this particular audience).

+ That the *Decretum* was the first book written primarily for use
as a university textbook.

+ That Anders Winroth had in 1996 identified four early manuscripts
as exemplars of a first recension of the *Decretum* about half the
length of the vulgate *Decretum* represented in the Friedberg
edition, and that therefore the *Decretum*, like many modern
university textbooks, could be thought of as having a first and
second edition (recension).

+ That as a consequence of the subject matter, the commentary
historically attributed to the putative author Gratian amounted to
only around one-fifth of the text of the vulgate *Decretum*, while
the remaining four-fifths of the text was quoted or excerpted from
traditionally accepted authorities such as conciliar decrees,
patristic writings, and papal letters (22% and 78% by word count
respectively). I pointed out the typographical distinction in the
Friedberg edition between the commentary (italic) and the authorities
(roman) as a visual illustration of relative proportion between the
two.

+ That the *Decretum* is divided into three parts, and that the
second part, consisting of 36 cases each introduced by a hypothetical
case statement is considered by many (cite Noonan and Pennington)
to be both uniquely innovative, and to be the core around which the
compilation developed.

I introduced the scholarly controversy over whether the commentary
historically attributed to Gratian had one author (as Pennington
argues) or two (as Winroth argues). I then presented my preliminary
finding that the case statements had *not* in fact been written by
the author(s) of the rest of the commentary historically attributed
to Gratian, and that the commentary excluding the case statement
could not be definitively attributed to either one or two authors.

Much of the discussion that followed concentrated on the technical
details of using the frequencies of function words to attribute
authorship and tool I was using to do so (the stylometry for R
package). Neil Fraistat, however, summarized the conversation with
a higher-level observation. Accepting the way in which the question
had been framed by specialists in the field of canon law, I had
designed an experiment intended to answer the question of whether
the commentary historically attributed to Gratian had one or two
authors. If the results of the experiment made no sense in the terms
of the question it was intended to answer, that, Fraistat suggested,
meant that the field was asking the wrong question.

**"If the answer doesn't make sense, you're asking the wrong
question."**

**Authority**

In the middle ages, to presume to take on the role of *auctor* was
to make a claim (at least implicitly) to *auctoritas*. Medieval
writers were in general quite reticent about making claims to
*auctoritas* on their own behalf, and employed a variety of techniques
to maintain plausible deniability that they were in fact claiming
authorship and the authority that goes with it. Some repudiated the
role of author altogether and circulated the texts they wrote
pseudonymously under the name of a canonical author of unquestioned
authority. Augustine was the overwhelming favorite, and Gratian
extensively quoted from a text, *De vera et falsa penitentia*, that
circulated under such false pretences in his *de Penitentia*. Others
sought to distance themselves from the role of author by locating
authority in texts they quoted rather than in the original use they
made of those quoted texts in their own writing ("their authority
deriving mainly from the fact that they consisted mostly of quotations"
Winroth, *The Making of Gratian's Decretum*, 191).

The problem of authorship and authority was particularly acute in
the first half of the twelfth century, because early scholastic
readers were more alert to the chinks in the armor of traditional
authorities than their less-sophisticated predecessors had been.
Peter Abelard was unique in the radicalism of his solution to the
problem: in *Sic et non*, he subverted and indeed dissolved the
entire notion of authority by showing that texts written by equally
authoritative authors were in actual, not just apparent, disagreement.

Gratian, here defined as the author(s) of the first-recension
*dicta*, undertook the conservative hermeneutical project of
harmonizing the apparently discordant canons, and accordingly adopted
the strategy of locating authority in the texts that he quoted. It
seem, however, that the widespread reception of the *Decretum* as
itself authoritative was influenced be an accidental feature of the
text.

In any event, the modern notion that the authority of a text derives
from the independently testable validity of the arguments it contains
is simply not relevant in the context of the twelfth century.
