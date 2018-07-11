---
author: Paul Evans
bibliography: chapter0.bib
csl: ../csl/chicago-fullnote-bibliography.csl
nocite: |
  @*
reference-section-title: Bibliography
title: Chapter 0
abstract: |
  Genesis of the project or: How I came to write a PhD dissertation
  about a completely unexpected finding I wasn't looking for to
  begin with.
---
## Introduction

The most significant finding of the following dissertation is that
the author who wrote the thirty-six case statements introducing the
hypothetical cases that make up the second part of Gratian's
*Decretum* is very unlikely to have been the same person as the
author who wrote the *dicta* in the first recension of the *Decretum*.
The technique used to make this determination takes the statistical
frequencies of common function words like prepositions and conjunctions
in a sample of text as the basis for assigning probable authorship,
and will be explained in considerable depth in Chapter 4.

I did not start work on this project thinking that the authorship
of the case statements was a research problem in any way. I assumed
that by definition the author of the case statements was one and
the same person as the author of the first-recension (R1) *dicta*.[^1]
It is therefore worth explaining in some detail how I came to write
a PhD dissertation about a completely unexpected finding that I was
not looking for in the first place.

I worked in information technology as a system administrator and
manager for most of the twenty-three years after graduating from
UC San Diego in 1984 with an undergraduate degree in History.
Stanley Chodorow had been the advisor for my undergraduate senior
thesis on the role of the cardinals in the thirteenth and fourteenth
centuries. I was therefore aware of Gratian's *Decretum* in a general
sort of way, although the only use I made of it in connection with
that project was to consult the Latin text of Nicholas II's 1059
decree on papal elections (D.23 c.1).

Stan encouraged me to use computer-aided typesetting for my thesis,
so I acquired an unusual skill that led directly to my IT career.
In the mid to late 80s I went on to take most of the required courses
for the undergraduate Computer Science major at UC San Diego (e.g.,
Data Structures, Compiler Construction, Operating Systems) although
I did not enroll in a degree program. During my professional career,
I was never primarily a programmer, but from time to time my job
responsibilities did include programming projects in C and Perl,
and ultimately Java servlet-based web applications.

I became aware of Anders Winroth's *The Making of Gratian's Decretum*
in October 2003, when I did a Google search for Stan's contact
information and found instead his review of Anders's book in *The
English Historical Review*.[@chodorow_review_2003] It was immediately
apparent to me on reading the review that there had been a revolution
in Gratian studies. My wife Carol gave me a copy of the book for
Christmas 2003 with the inscription "I'm sure you'll gulp this one
down within 24 hours." I did. Some years later, Anders thanked
Carol: "I'm sure I did something very useful with the money".

From September 2007 to May 2009, I was a student in the History of
Christianity MAR program at Yale Divinity School. Among the courses
I took was a one on Latin Paleography that Richard and Mary Rouse
of UCLA taught at the Beinecke Rare Book and Manuscript Library in
Spring 2009. Although I had a general interest in applying my
computing background to my academic work, I do not believe I had
heard of Digital Humanities as an academic discipline before I
graduated from YDS, and almost certainly not by that name.

In October 2009, David Ganz (then of King's College, London) suggested
that I compare two texts of the Capitulare Carisiacense (873) in
Beinecke MS 413. At first, I did not think of it as a digital
project; it was simply a transcription exercise of the kind the
Rouses had taught me to do. But within a month, I had created a
custom text encoding format for my transcriptions and written a
prototype textual difference visualizer in Perl to compare them.
A January 2010 meeting with Barbara Shailor on the Beinecke 413
project was the occasion for the first use I can find in my own
notes of the term "Digital Humanities."

In the summer of 2010, I taught myself to write Python web applications
on the Google App Engine platform (learning Python was incidental
to learning GAE, which is what I was really interested in), and in
the first half of 2011, I developed Ingobert, a Python/GAE web
application to visualize textual differences in Beinecke 413, in
connection with an independent study project supervised by Ken
Pennington and Jennifer Davis. Largely on the strength of the
Ingobert project, Neil Fraistat of the University of Maryland hired
me as a graduate assistant at the Maryland Institute for Technology
in the Humanities (MITH) to work as a Scala/Lift programmer on the
Active OCR project.[^3]

* * *

To the extent that I was looking in the first half of 2013 for a
dissertation project with a Digital Humanities component, my focus
was on the use of David Mimno's MALLET (MAchine Learning for LanguagE
Toolkit) to topic model *dicta* and canon texts from the first and
second recensions of Gratian's *Decretum* as a way to identify new
topics added in the second recension.

* * *

I closely followed the DH 2013 conference at the University of
Nebraska-Lincoln via Twitter, which was still very much at that
time the town square of the Digital Humanities community.

![Figure 1 10 Sep 2013](JPGs/Photo51.jpg)

## Note on Translations

I have, wherever possible, supplied for each Latin passage quoted
the corresponding passage from a published English translation.[^4]
In cases where no such translation was available, or I considered
the available translation seriously misleading, I have supplied my
own translation, indicated with the notation **(trans. PLE)**.
**Acknowledge Atria A. Larson.**

[^1]: To the extent that there is some one person we can point to
as corresponding to our idea of "Gratian," it's the author of the
first-recension dicta. "The *dicta* in Gratian's *Decretum* bring
the reader closer to its author than any other part of the text."
[@winroth_making_2000, 187]. **See if there is anything else that
can be used to support this point in "The men behind the 'Decretum'",
pp.175-192.**

[^3]: NEH ODH Grant number:
[HD-51568-12](https://securegrants.neh.gov/publicquery/main.aspx?f=1&gn=HD-51568-12)

[^4]: @jansen_medieval_2009; @somerville_prefaces_1998; and
@thompson_treatise_1993 have been particularly helpful resources
in this regard.

