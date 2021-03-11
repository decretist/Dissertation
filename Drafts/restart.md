---
author: Paul Evans
bibliography: ../bib/merged.bib
csl: ../csl/chicago-fullnote-bibliography.csl
date: 7 March 2021
reference-section-title: Bibliography
suppress-bibliography: false
title: Restart
abstract: |
  My point is that at your defense a central point will be: "OK, Paul,
  you did an enormous amount of work inputting all the data, how can
  you and we trust what a computer program is telling us?" It would
  be very good if you can tell us about other medieval authors about
  which there is some consensus that the computer has given us firm
  conclusions. - Ken Pennington, 13 July 2020

---
+ Ulpian
+ August 1, August 3, and September 17 emails
+ Patrick Juola, "The Rowling Case: A Proposed Standard Analytic
Protocol for Authorship Questions", *Digital Scholarship in the
Humanities*, Vol. 30, Supplement 1, 2015.

### Successes and Failures

Historians and literary scholars have long (if imprecise) memories
about poorly-conceived attempts at authorship attribution (e.g.,
Tony Honoré's attempt to attribute Roman law texts to Ulpian, and R.A.
Cooper and D.A. Pearsall's attempt to attribute authorship of the
Gawain Poems). Conversely, successful, methodologically rigorous,
attributions of authorship are quickly forgotten when the author
or the text in question is uninteresting to literary academia (e.g.,
Patrick Juola's successful attribution of *The Cuckoo's Calling*,
a 2013 crime fiction novel, to J.K. Rowling of Harry Potter fame.)

---

Bruce W. Frier of the University of Michigan Law School negatively
reviewed Tony Honoré's *Ulpian*(1982) for its misuse of stylometric
analysis for authorship attribution. Honoré generated lists of what
would now be called Most Distinctive Words (MDWs) and Statistically
Improbable Phrases (SIPs) from a concordance of the works of Ulpian,
and used them to attempt to periodize and to determine authorship
of texts attributed to Ulpian.

---

The A.S.G. Edwards essay in the July 3, 2020 issue of *The Times
Literary Supplement (TLS)* [@edwards_go_2020] appears to refer to
"The Gawain Poems" by R.A. Cooper and D.A. Pearsall. [@cooper_gawain_1988]

Cooper and Pearsall conclude that the stylometric evidence they
evaluate is consistent with common authorship for the four poems
preserved in British Library MS Cotton Nero A.x (*Sir Gawain and
the Green Knight*, *Pearl*, *Patience*, and *Cleanness*). Some of
the stylometric measures they employ are only relevant to poetry,
focusing specifically on the alliterative features of the texts.
Cooper and Pearsall also analyze the frequencies of 11 function
words, distinguishing between words occurring at the beginning of
a line and words occurring in the middle of a line. (John Burrows
and David Hoover in a series of papers starting in 2000 established
30 words as a best-practice minimum for this kind of word frequency
analysis.) It is not, for the most part, very methodologically
sophisticated work, even by the standards of 1988. The one exception
is their analysis of the co-occurrence of parts of speech (POSs)
within lines, which anticipates the kind of part of speech bigram
and trigram analysis that is sometimes performed today when
appropriately tagged electronic texts are available. (An example
of part of speech bigram analysis would be to analyze the frequencies
of occurrence of noun-adjective pairs versus adjective-noun pairs
in Latin texts.)

Google Scholar indicates that the Cooper and Pearsall article has
12 citations as of August 2020, so it does not appear to have had
much influence on the subsequent development of scholarship within
its subfield. (To put that number in context, Google Scholar indicates
that Pennington's "Bartolome de las Casas and the Tradition of
Medieval Law" has 86 citations.)

---

In the course of tracking down the work referenced in passing in
the Edwards TLS essay, I came across a recent project that seems
to have had a very favorable reception:

Neidorf, L., Krieger, M.S., Yakubek, M. et al. Large-scale quantitative
profiling of the Old English verse tradition. Nat Hum Behav 3,
560–567 (2019). https://doi.org/10.1038/s41562-019-0570-1

I have not been able to download the paper yet (USD doesn't have
institutional access to Nature Human Behavior), but I have been
able to gather enough information from other sources to get the
general idea. (Their code is publicly available on Github.) The
authors present stylometric evidence "consistent with the unitary
authorship of Beowulf." The method they use is to analyze the
statistical frequency of character bigrams in the text. If the
techniques I use give you heartburn, Ken, I suspect you'd really
object to character bigram and trigram analysis. This technique
involves breaking down words into their constituent two- or
three-letter substrings. The string "Gratian" broken down into
bigrams would be ['gr', 'ra', 'at', 'ti', 'ia', 'an'], and broken
down into trigrams would be ['gra', 'rat', 'ati', 'tia', 'ian']
(strings are lowercased before being split into bigrams or trigrams).
After breaking the text down into character bigrams or trigrams,
the principal component analysis (PCA) is then performed on the
frequencies of the bigrams or trigrams in exactly the same way as
it would be on word frequencies. There is justification in the
academic literature of psycholinguistics to give an account for why
stylometry based on the frequencies of function words works, i.e.,
the claim, supported by experimental evidence, that both writers
and readers process function words at a subconscious level. PCA
using bigrams and trigrams on the other hand is just sorcery. Which
is not to say that it doesn't work. I have analyzed the dicta from
the Decretum using character bigrams instead of words, and the
results are not notably different from the results I present in the
dissertation.

There seem to be at least two reasons unrelated to the academic
merits of the article that it has been as favorable received as it
has. First, one of the authors, M. Ski Krieger, is associated with
Harvard, and Harvard has seen fit to publicize the project very
enthusiastically. Second, the article's finding that Beowulf is the
product of unitary authorship supports an argument advanced by JRR
Tolkien in the 20th century, which attracted a significant amount
of coverage from non-specialist publications.

---

This email is resumptive of our conversation of August 3 about
recent attempts to apply stylometric methods to attribute medieval
texts. Ken suggested citing attributions that have achieved some
threshold of scholarly acceptance. Here's another one that I got
from a conversation this week with Mike Kestemont, the University
of Antwerp researcher whose work is a model for what I'm doing.

The text is a set of Latin love letters between an anonymous man
and woman (Vir and Mulier or just V. and M.), extant in a single
manuscript that was copied c.1470 under the title Ex epistolis
duorum amantium. Constant Mews in The Lost Love Letters of Heloise
and Abelard (2001) attributed the letters to Abelard and Heloise.
Jan Ziolkowski of Dumbarton Oaks contested Mews's attribution,
partly on stylometric grounds, in:

Ziolkowski, Jan M. "Lost and Not Yet Found: Heloise, Abelard, and
the "Epistolae Duorum Amantium"." The Journal of Medieval Latin 14
(2004): 171-202. (http://www.jstor.org/stable/45019598).

The stylometric component of Ziolkowski's argument consists of a
comparison of the relative frequencies of the function words autem,
igitur, ergo, ita(que), quia, and quippe as they appear in Historia
Calamitatum, Letters 3 and 5, and the letters attributed to Vir in
the EDA collection. Ziolkowski's rebuttal to Mews's attribution is
perhaps more relevant to my work than some of the other attributions
we've discussed, in that it is a negative attribution. Like my claim
that the case statements in the Decretum were not written by author(s)
of the dicta, Ziolkowski is arguing that the texts were not written
by the putative author. Furthermore, Ziolkowski's negative attribution
was made on the basis of function words drawn from discontinuous
and relatively small samples of medieval Latin.

In keeping with the previous emails in this series, I'll note that
Google Scholar shows that Ziolkowski's article has been cited 23
times, considerably less than Ken's "Bartolomeo de las Casas and
the Tradition of Medieval Law", but better than the Cooper and
Pearsall paper on Gawain that started this conversation.

### Authorship (Barthes and Foucault)

### Implications and Conclusions
