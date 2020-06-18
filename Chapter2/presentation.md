---
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
reference-section-title: Bibliography
suppress-bibliography: true
title: Chapter 2
subtitle: The *Decretum*
---
## Presentation

Having considered how Gratian sourced and collected his materials---the
question of what canons are and where Gratian got them---we now
turn to the question of how Gratian presented and organized the
canons he had collected. Here, it is important to distinguish between
presentation, the small-grain or micro structure of the *Decretum*,
and organization, the large-grain or macro structure of the *Decretum*.
The organization of the *Decretum* is very regular, so structurally
regular, in fact, that Reuter and Silagi's OCP e-text of the Friedberg
edition can be taken apart using a recursive descent parser[^31]
and should be thought of as a sequence of hierarchically nested
containers. Taking a bottom-up approach, we will first consider the
presentation or small-grain structure, and start with the canons,
the atomic containers out of which the higher-order containers in
the *Decretum*---parts, distinctions, cases, and questions---are
built up.

The way in which canons are presented in the *Decretum* differs
somewhat from the way in which they were presented in the
formal sources from which Gratian selected his
material. A canon in the formal sources typically included
an inscription, a rubric, and the canon text. Gratian added
a *dictum post canonem* (plural *dicta post canones*)
containing his own commentary on the preceding canon or canons, a
feature borrowed from Alger of Liège's theological treatise *De
misericordia et iustitia* but without an immediate precedent in
the canonical literature.[^32]

#### Inscription

Most canons have an inscription, which identifies the ultimate
source of authority for that canon, usually a papal decretal, a
canon from an ecumenical council or an important provincial synod,
or a patristic text.[^33] This raises the need to distinguish
Gratian's material sources---an original letter of Pope Gregory I,
for example---from his formal sources---the collection from which
Gratian actually copied his text.[^34] Because Gratian collected
his texts almost exclusively from formal sources, the inscription
was sometimes historically inaccurate, especially if the text in
question was one derived from the Pseudo-Isidorian collections.

#### Rubric

A canon is often, though not always, introduced by a rubric. The
name refers to the fact that rubrics were conventionally written
in red ink in manuscripts. A rubric is a very short summary of what
the following canon is about. In many cases the rubric simply reads
"*de eodem*", which means "about the same thing" as the preceding
canon.[^35] **(Pennington and Eichbauer believe that Gratian wrote
the rubrics in the *Decretum* rather than reusing those he found
in formal source collections.[^36] The fact that the rubrics are
short, discontinuous, texts means that they are of effectively no
value for the purpose of authorship attribution. On the other hand,
the fact that they are believed to have been written by Gratian,
and therefore reflect his choice of wording, means that
they are potentially useful evidence in the search for new topics
introduced between the first and second recensions.)**

#### Canon text

**(The nature of the canon texts proper has been described above
in the section on the collection and selection of canons.)**

Finally, there are the *dicta post canones*, usually abbreviated
d.p.c. and literally meaning "something said after the canons." The
*dicta post* are statements that Gratian made on his own authority
as a jurist, carry the thread of his argument, and do his interpretive
work. The *dicta* are texts that Gratian (whether we think of him
as one person or many) actually wrote, and are therefore subject
to analysis for authorship attribution. "The *dicta* in Gratian's
*Decretum* bring the reader closer to its author than any other
part of the text."[@winroth_making_2000, 187] **(The *dicta post*
are not found in Part III, which is in this respect more structurally
similar to the formal source collections Gratian relied on than to
the rest of the *Decretum*)**.

[^31]: See Appendix 2 for the Python code listing for my implementation
of the recursive-descent parser. Thanks to Patricio Simari of the
Electrical Engineering and Computer Science Department at The
Catholic University of America, who provided helpful suggestions
on parser implementation. In Computer Science-theoretic terms, the
parsed *Decretum* can be thought of as an ordered tree, with parts,
distinctions, cases, and questions as interior nodes. A canon or
chapter, properly conceptualized as a node encapsulating rubrics,
inscriptions, canon texts, and *dicta post*, is also an internal
node. A *dictum* (*ante*, *post*, or *initiale*) is a terminal node.
So are rubrics, inscriptions, and canon texts. A case statement
(*dictum initiale*) is always the first terminal node of a case. A
*dictum ante* is always the first terminal node of a distinction
or question. The anomalous C.16 q.2 d.a.c.8 is actually the *dictum
ante* introducing a vestigial fifth question positioned between
C.16 q.2 and C.16 q.3 (see Friedberg, 1.787). The traditional
notation misleadingly implies that d.a.c.1 is a leaf node of c.1.
In fact, d.a.c.1 and c.1 are both child nodes at the same nesting
level under one parent distinction or question node. A *dictum
post* is an optional, and usually the last, terminal node of a
canon.

[^32]: Gratian is known to have used Alger as both a source,
especially in C.1, and, to some extent, as a methodological model.
[@winroth_making_2000, 17, 39, 144]. See Robert Kretzschmar's
edition, [-@kretzschmar_alger_1985]. Somewhat confusingly for Gratian
scholars, Kretzschmar uses regular typeface for Alger's *dicta* and
italics for the canons, the opposite of the convention adopted by
Friedberg and maintained by Winroth.

[^33]: The distinction between rubrics and *dicta* is blurry:
"Gratian rarely took his rubrics from earlier collections. Rather
he created his own and often melded the rubrics with the dicta."
[@eichbauer_redactions_2007, 107] "Both J. Rambaud-Buhot and John
Noonan, Jr. have highlighted the similarity between dicta and
rubrics, that is, a rubric very often echoes the dictum that
immediately preceded it." and "These isolated instances in the first
cluster show that Gratian felt that the dictum was sufficient for
summarizing the following *auctoritas*." [@eichbauer_redactions_2007,
115] **Expand to include inscriptions.**

[^34]: "Since Gratian frequently took fragments of letters from the
Register of Gregory I---266 in all---using the inscription 'in
registro', older research assumed that he must have used this
important source in the form of the *Registrum Hadrianum*. According
to more recent research (Landau), even these texts from the Register
of Gregory I found in Gratian derive almost without exception from
canonical collections predating Gratian; the direct use of the
Register is probable in only a single case." [C.27 q.1 c.19 (JE
1496)] [@landau_gratian_2008, 34].

[^35]: **The role of the *de eodem* rubrics in Winroth's argument
that the Aa, Bc, Fd, and P mss. of the *Decretum* are a first
recension rather than an abbreviation of the vulgate.
[@winroth_making_2000] Kuttner's statement of the "untidy seams"
problem in "Acta and Agenda", and how Winroth solves it.
[@kuttner_research_1990].** Winroth observed that there are 398 *de
eodem* rubrics in the vulgate *Decretum*, see [@winroth_uncovering_1997,
28]; and [@winroth_making_2000, 127]. The precision of this
frequently-cited number can be refined in ways that demonstrate the
true power of the careful use of electronic resources for the study
of this, or any, text. (In the following examples, ```edF.txt```
is the filename of the OCP-format Reuter and Silagi e-text of the
Friedberg edition. The commands used in the examples should work
on any macOS or Linux-based system.) Winroth's figure of 398 simply
represents the number of occurrences of the substring "de eodem"
in the file: ```grep -i "de eodem" edF.txt | wc -l``` returns 398.
Most, but not all, of the occurrences of the substring "de eodem"
do, in fact, appear in the context of a rubric, In one case, *de
Cons.* D.2 c.3, the inscription reads *Idem de eodem* ("the same
person about the same thing"), and refining the search to count
those occurrences that do **not** appear alongside the OCP rubric
```<T R>``` or inscription ```<T I>``` tags reveal that in 8
instances, the words *de eodem* are simply part of the text of a
canon or *dictum*: ```grep -i "de eodem" edF.txt | egrep -v "<T
R>|<T I>" | wc -l``` returns 8. Setting aside, then, those instances
in which the words *de eodem* occur in canons, *dicta*, or inscriptions
(and acknowledging that the criteria for distinguishing between
inscriptions and rubrics can be blurry) leaves 389 rubrics containing
the substring "de eodem": ```grep -i "de eodem" edF.txt | grep "<T
R>" | wc -l``` returns 389. Of those 389, there are 373 *De eodem*
rubrics and 13 *Item de eodem* rubrics (12 of those 13 introduce
second-recension canons in D.30 in the first part of the *Decretum*):
```fgrep "De eodem." edF.txt | grep "<T R>" | wc -l``` returns 373,
and ```fgrep "Item de eodem." edF.txt | grep "<T R>" | wc -l```
returns 13. In the three remaining cases, words *de eodem* are part
of a longer rubric: ```grep -i "de eodem" edF.txt | grep "<T R>" |
fgrep -v "De eodem." | fgrep -v "Item de eodem."``` returns the
rubrics for D.23 c.32 (*De eodem, et ut clerici comam non nutriant*),
C.22 q.5 c. 16 (*De eodem, et ut a ieiunis iuramenta prestentur*),
and *de Cons.* D.1 c.17 (*De eodem, et quod octo diebus dedicationum*).
Winroth's larger point, however, had to do with the place of the
*de eodem* rubrics in the "untidy seams" problem. For that purpose,
only the 137 *de eodem* rubrics in the first recension of the
Decretum are potentially relevant evidence. **See GitHub
[Sand](https://github.com/decretist/Sand/tree/master/rubrics)
repository. This result (137) is potentially off by one, i.e., the
total number of *de eodem* rubrics in the first and second recension
rubric data sets is 388 instead of 389, with no way to tell whether
the missing rubric is from the first or second recension.**

[^36]: **Placeholder for footnote referencing Eichbauer's observation
that Gratian wrote his own rubrics.**

