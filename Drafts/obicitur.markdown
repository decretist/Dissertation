### Lemmas or Words

The work that I presented at the *Rem non novam* and ICMCL conferences
in 2015 and 2016 was patterned as closely as possible on the example of
Mike Kestemont, Sara Moens, and Jeroen Deploige.[1]

Kestemont, *et al.*, used principal component analysis of the
frequencies of 65 lemmas of common function words to investigate the
role of collaborative authorship in origin of two late visionary texts
attributed to Hildegard of Bingen.

They lemmatized their samples using Morfette, a software package written
in the Haskell programming language by Grzegorz Chrupała, who describes
it as "a tool for supervised learning of inflectional morphology."[2]

Supervised learning algorithms are a class of machine learning algorithm
that perform a task on the basis of a trained model.

In the context of Latin The operative word in this description is
"supervised."

(The issue is not so much that I could not have installed Haskell and
Morfette in 2015, as that such tools need to be trained using large
amounts of pre-tagged Latin text. Because Kestemont's co-authors were
working on a critical edition of the Hildegard texts for Brill, they
were given special access to a large and very high-quality pre-tagged
corpus of Medieval Latin texts that they used to train the model they
then used to lemmatize their samples.)

Kestemont recently indicated that the question of whether it is
preferable to use words or lemmas words as the basis for principal
component analysis of function word frequencies is "controversial."

I could have installed Haskell and Morfette in 2015 (and probably did),
but I did not have access to IT-TB, and in any event, training a model
would have been considerably beyond the scope the project. I considered
the possibility of stemming as an alternative to lemmatization. This
would have involved implementing in Python the Schinke Latin stemming
algorithm as documented on the website for the Snowball stemmer.[3]

The Snowball stemmer and associated stemming algorithms come from the
field of information retrieval, and are probably unsuitable for
scholarly purposes. The Schinke algorithm "has the feature that it stems
each word to two forms, noun and verb," e.g.,

|        | NOUN   | VERB   |
|:-------|:-------|:-------|
| aquila | aquil  | aquila |
| portat | portat | porta  |
| portis | port   | por    |

I ultimately decided to perform PCA on the *dicta* from Gratian's
*Decretum* using word rather than lemma or stem frequencies.

### Words, lemmas, or n-grams

### Pronouns

Kestemont, *et al.*, were analyzing the letters of Hildegard of Bingen,
Guibert of Gembloux, and Bernard of Clairvaux. They therefore expected
personal pronouns, especially second-person pronouns, to be salient
features of the samples they were analyzing.

When the delete pronouns option is selected, stylo() excludes:

-   all forms, singular and plural, of the first-person personal pronoun
    *ego*, *mei*

-   all forms, singular and plural, of the second-person personal
    pronoun *tu*, *tui*

-   all forms of the demonstrative adjectives *ille*, *illa*, *illud*
    (but **not** *hic*, *haec*, *hoc*) and *is*, *ea*, *id*, treated as
    third-person personal pronouns

-   all forms of the possessive pronouns *meus*, *mea*, *meum*; *tuus*,
    *tua*, *tuum*; *suus*, *sua*, *suum*; *noster*, *nostra*, *nostrum*;
    and *vester*, *vestra*, *vestrum*.

<!-- -->

    > stylo.pronouns(corpus.lang = "Latin")
     [1] "ea"        "eae"       "eam"       "earum"     "eas"       "ego"
     [7] "ei"        "eis"       "eius"      "eo"        "eorum"     "eos"
    [13] "eum"       "id"        "illa"      "illae"     "illam"     "illarum"
    [19] "illas"     "ille"      "illi"      "illis"     "illius"    "illo"
    [25] "illorum"   "illos"     "illud"     "illum"     "is"        "me"
    [31] "mea"       "meae"      "meam"      "mearum"    "meas"      "mei"
    [37] "meis"      "meo"       "meos"      "meorum"    "meum"      "meus"
    [43] "mihi"      "nobis"     "nos"       "noster"    "nostra"    "nostrae"
    [49] "nostram"   "nostrarum" "nostras"   "nostri"    "nostris"   "nostro"
    [55] "nostros"   "nostrorum" "nostrum"   "sua"       "suae"      "suam"
    [61] "suarum"    "suas"      "sui"       "suis"      "suo"       "suos"
    [67] "suorum"    "suum"      "suus"      "te"        "tibi"      "tu"
    [73] "tua"       "tuae"      "tuam"      "tuarum"    "tuas"      "tui"
    [79] "tuis"      "tuo"       "tuos"      "tuorum"    "tuum"      "tuus"
    [85] "vester"    "vestra"    "vestrae"   "vestram"   "vestrarum" "vestras"
    [91] "vestri"    "vestris"   "vestro"    "vestros"   "vestrorum" "vestrum"
    [97] "vobis"     "vos"
    >

### Parking lot

Cite:

[Latin BERT: A Contextual Language Model for Classical
Philology](https://arxiv.org/abs/2009.10053).

PIE: A Framework for Joint Learning of Sequence Labeling Tasks[4]

Pie Extended[5]

# Bibliography

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-thibault_clerice_2020_3883590" class="csl-entry">

Clérice, Thibault. *Pie Extended, an Extension for Pie with
Pre-Processing and Post-Processing*. Zenodo, 2020.
<https://doi.org/10.5281/zenodo.3883589>.

</div>

<div id="ref-kestemont_collaborative_2015" class="csl-entry">

Kestemont, Mike, Sara Moens, and Jeroen Deploige. “Collaborative
Authorship in the Twelfth Century: A Stylometric Study of Hildegard of
Bingen and Guibert of Gembloux.” *Literary and Linguistic Computing* 30,
no. 2 (June 2015): 199–224.

</div>

<div id="ref-manjavacas-etal-2019-improving" class="csl-entry">

Manjavacas, Enrique, Ákos Kádár, and Mike Kestemont. “Improving
Lemmatization of Non-Standard Languages with Joint Learning.” In
*Proceedings of the 2019 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language Technologies,
Volume 1 (Long and Short Papers)*, 1493–503. Minneapolis, Minnesota:
Association for Computational Linguistics, 2019.
<https://doi.org/10.18653/v1/N19-1153>.

</div>

</div>

[1] “Collaborative Authorship in the Twelfth Century: A Stylometric
Study of Hildegard of Bingen and Guibert of Gembloux,” *Literary and
Linguistic Computing* 30, no. 2 (June 2015): 199–224.

[2] "Morfette is a tool for supervised learning of inflectional
morphology. Given a corpus of sentences annotated with lemmas and
morphological labels, and optionally a lexicon, morfette learns how to
morphologically analyse new sentences." [morfette: A tool for supervised
learning of morphology](https://hackage.haskell.org/package/morfette)

[3] [The Schinke Latin stemming
algorithm](http://snowball.tartarus.org/otherapps/schinke/intro.html),
now superseded by [The Schinke Latin stemming algorithm -
Snowball](https://snowballstem.org/otherapps/schinke/)

[4] Enrique Manjavacas, Ákos Kádár, and Mike Kestemont, “Improving
Lemmatization of Non-Standard Languages with Joint Learning,” in
*Proceedings of the 2019 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language Technologies,
Volume 1 (Long and Short Papers)* (Minneapolis, Minnesota: Association
for Computational Linguistics, 2019), 1493–503,
<https://doi.org/10.18653/v1/N19-1153>.

[5] Thibault Clérice, *Pie Extended, an Extension for Pie with
Pre-Processing and Post-Processing* (Zenodo, 2020),
<https://doi.org/10.5281/zenodo.3883589>.
