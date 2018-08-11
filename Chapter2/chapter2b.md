---
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
title: Chapter 2b
subtitle: The *Decretum*
suppress-bibliography: true
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
edition can be taken apart using a recursive descent parser,[^32]
and should be thought of as a sequence of hierarchically nested
containers. Taking a bottom-up approach, we will turn first to the
presentation or small-grain structure, and start with the canons,
the atomic containers out of which the higher-order containers in
the *Decretum*---parts, distinctions, cases, and questions---are
built up.

The way in which canons are presented in the *Decretum* differs
somewhat from the way in which they are presented in the predecessor
collections of formal sources from which Gratian selected his
material. The canon package in the formal sources typically included
an inscription, a rubric, and the canon text. Gratian added to the
package a *dictum post canonem* (plural *dicta post canones*)
containing his own commentary on the preceding canon or canons, a
feature borrowed from Alger of Liège's theological treatise *De
misericordia et iustitia*, but without an immediate precedent in
the canonical literature.[^33]

A canon is often, though not always, introduced by a rubric. The
name refers to the fact that rubrics were conventionally written
in red ink in manuscripts. A rubric is a very short summary of what
the following canon is about. In many cases the rubric simply reads
"*de eodem*", which means "about the same thing" as the preceding
canon.[^34]

Most canons have an inscription, which identifies the ultimate
source of authority for that canon, usually a papal decretal, a
canon from an ecumenical council or an important provincial synod,
or a patristic text.[^35] This raises the need to distinguish
Gratian's material sources---an original letter of Pope Gregory I,
for example---from his formal sources---the collection from which
Gratian actually copied his text.[^36] Because Gratian collected
his texts almost exclusively from formal sources, the inscription
was frequently historically inaccurate, especially if the text in
question was one derived from the Pseudo-Isidorian collections.

Finally, there are the *dicta post canones*, usually abbreviated
d.p.c., and literally meaning "something said after the canon". The
*dicta post* are statements that Gratian made on his own authority
as a jurist, carry the thread of his argument, and do his interpretive
work. The *dicta* are texts that Gratian (whether we think of him
as one person or many) actually wrote, and are therefore subject
to analysis for authorship attribution. "The *dicta* in Gratian's
*Decretum* bring the reader closer to its author than any other
part of the text."[@winroth_making_2000, 187]

## Organization

The *Decretum* in the form that circulated after around 1150 (the
Köln Dombibliothek manuscripts 127 and 128 are good early examples)
has three parts. The first part consists of 101 distinctions. Groups
of distinctions form treatises within the work: the first twenty
distinctions, for example, form a treatise on laws (*tractatus de
legibus*) that explores the sources of law. Other topics covered
include ecclesiastical hierarchy and clerical discipline. The second
part consists of 36 cases, which are further subdivided into 168
questions. Four of the questions, C.11 q.2, C.17 q.3, C.22 q.3, and
C.29 q.1 are empty, and one, C.33 q.3, encapsulates a treatise on
penance (*tractatus de penitentia*, abbreviated *de Pen.*) divided
into seven distinctions. The third part of the *Decretum* is a
treatise on sacraments (*tractatus de consecratione*, abbreviated
*de Cons.*) divided into five distinctions.[@winroth_making_2000,
5] Contemporaries like Rufinus and Stephen of Tournai understood
the parts to treat respectively of ministries, business, and
sacraments: "*primam ministeriis, secundam negotiis, tertiam
ecclesiasticis deputat sacramentis.*"[^39]

* * *

The hypothetical case statements or *themata* that introduce each
of the thirty-six *causae* (cases) that constitute Part II of the
*Decretum* reflect at least in places an outlook and a set of
concerns that university-educated urban professionals of the present
day would not find it difficult to identify with. At a time when
considerable attention is being paid in the realm of popular discourse
(if not yet public policy) to the issue of "opportunity hoarding"
on behalf of upper- and upper-middle class children by their
university-educated, urban professional parents, the intense concern
of "a certain man" in the first case statement to secure a good
ecclesiastical career for his son (and his willingness on more than
one occasion to resort to bribery in order to realize that objective)
has a distinctly contemporary feel to it.[^40]

The cases are hypotheticals like those used in modern law schools,
and some of them are quite far-fetched. In case 28, for example, a
married infidel converts to Christianity, as a result of which his
wife separates from him out of hatred for his new faith. (By
"infidel," Gratian means a Muslim.) The convert then takes a new
Christian wife, and after she dies, he is made a priest. Finally,
"on account of the merit of his life and learning," he is elected
bishop. Gratian extracts questions from this fantastical fact-pattern,
however, that are of considerable theoretical (if not practical)
interest: whether there can be marriage between infidels, whether
there is ever a situation in which a man can take another wife if
his previous wife is still alive; and whether someone who had one
wife before he was baptized and another wife after he was baptized
should be considered a bigamist.

The third part, *de Consecratione*, is problematic in several ways.
That *de Cons.* is a very late addition is not in doubt---it is
absent from all first-recension manuscripts, nor was it included
in the earliest manuscripts of the more widely-circulated
second-recension version of the *Decretum*, as indicated by glosses
found in the Gt, Pf, and Tr manuscripts describing Gratian's work
as "principally divided into two parts."[^41]

[^32]: See Appendix 2 for the Python code listing for my implementation
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
or question. A *dictum post* is an optional, and usually the last,
terminal node of a canon. **Example of d.a.c.8. The traditional
notation is misleading: d.a.c.1 is not a leaf node of c.1.**

[^33]: Gratian is known to have used Alger as both a source,
especially in C.1, and, to some extent, as a methodological model.
[@winroth_making_2000, 17, 39, 144]. See Robert Kretzschmar's
edition, [-@kretzschmar_alger_1985]. Somewhat confusingly for Gratian
scholars, Kretzschmar uses regular typeface for Alger's *dicta* and
italics for the canons, the opposite of the convention adopted by
Friedberg **(and Richter before him?)** and continued by Winroth.

[^34]: **The role of the *de eodem* rubrics in Winroth's argument
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

[^35]: The distinction between rubrics and *dicta* is blurry:
"Gratian rarely took his rubrics from earlier collections. Rather
he created his own and often melded the rubrics with the dicta."
[@eichbauer_redactions_2007, 107] "Both J. Rambaud-Buhot and John
Noonan, Jr. have highlighted the similarity between dicta and
rubrics, that is, a rubric very often echoes the dictum that
immediately preceded it." and "These isolated instances in the first
cluster show that Gratian felt that the dictum was sufficient for
summarizing the following *auctoritas*." [@eichbauer_redactions_2007,
115] **Expand to include inscriptions.**

[^36]: "Since Gratian frequently took fragments of letters from the
Register of Gregory I---266 in all---using the inscription 'in
registro', older research assumed that he must have used this
important source in the form of the *Registrum Hadrianum*. According
to more recent research (Landau), even these texts from the Register
of Gregory I found in Gratian derive almost without exception from
canonical collections predating Gratian; the direct use of the
Register is probable in only a single case." [C.27 q.1 c.19 (JE
1496)] [@landau_gratian_2008, 34].

[^39]: Rufinus and Stephen of Tournai describe the tripartite
division in exactly the same words: "librum suum in tribus partibus
distinguit, quarum primam ministeriis, secundam negotiis, tertiam
ecclesiasticis deputat sacramentis." [@singer_summa_1963, 5] "he
divides his book into three parts, the first of which he devotes
to ecclesiastical ministries, the second to [ecclesiastical] business,
and the third to ecclesiastical sacraments." [@somerville_prefaces_1998,
192-193] (Rufinus) "Harum primam ministeriis, secundam negotiis,
tertiam ecclesiasticis deputat sacramentis." [@schulte_summa_1965,
6] "The first of these parts is devoted to ecclesiastical ministries,
the second to ecclesiastical problems, the third to ecclesiastical
sacraments." [@somerville_prefaces_1998, 201] (Stephen of Tournai)
(Brasington translated the preface of Rufinus, Somerville that of
Stephen of Tournai. [@somerville_prefaces_1998, vii]. There is no
indication as to why Somerville chose to translate *negotiis* as
"problems" rather than "business".)

    Given the probable dates of the *summae* of Rufinus (1164) and
    Stephen of Tournai (1165/66), it is just possible that Stephen
    got the wording from the preface to the *Summa* of Rufinus.
    Kenneth Pennington,
    [Rufinus](http://amesfoundation.law.harvard.edu/BioBibCanonists/Report_Biobib2.php?record_id=a492)
    and [Stephanus
    Tornacensis](http://amesfoundation.law.harvard.edu/BioBibCanonists/Report_Biobib2.php?record_id=a502),
    *Bio-Bibliographical Guide to Medieval and Early Modern Jurists.*
    Stephen, however, had been a student of Rufinus in Bologna, and
    it seems more likely that this is something he had heard Rufinus
    say in lecture. **Kenneth Pennington, "Étienne of Tournai".**

[^40]: "Quidam habens filium ..." C.1, d.init., edF. 1.357. Although
Gratian does not say so explicitly, I think that we can reasonably
infer that the father is an urban merchant or professional, rather
than a member of the landed aristocracy, since his wealth, the
source of several bribes, is so readily convertible into cash.

[^41]: **Need footnote on Gt, Pf, and Tr gloss**

