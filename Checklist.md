### 2020 Dissertation Checklist

- [ ] Re-establish contact with Anders Winroth: 250-word proposal to ICMAC board for Stephan Kuttner Institute GitHub repository project, acknowledge D.6 d.p.c.3 bug report.
- [ ] Chapter 3: translate passages from _summa_ of Simon of Bisignano referring to Gratian as _magister_ and himself as _discipulus_.
- [ ] Chapter 3: summarize and analyze Pennington's argument about identity of Gratian
- [ ] Chapter 3: summarize and analyze Winroth's argument about identity of Gratian
- [ ] Read Mike Kestemont, Jeroen De Gussem, "Integrated Sequence Tagging for Medieval Latin Using Deep Representation Learning"
- [ ] Look for Ivonian vocabulary (admonition, indulgence, precept, prohibition, dispensation) in R1 and R2 _dicta_
- [ ] Check randomize.py into GitHub
- [ ] **~/Tmp is not checked in and not backed up!**
- [ ] Add statistics code to segment.py? (Mean size of samples plus standard deviation)

(28 July 2020)
- [x] Google Meet w/Larry Poos 13:00 PDT

(27 July 2020)
- [x] Zoom w/Kate Jansen 14:30 PDT

(13 July 2020)
-[x] Zoom w/Stan Chodorow 09:00 PDT

(14 May 2020)
- [x] Write definition of 1st- and 2nd-recension _dicta_ in samples

(24 April 2020)
- [ ] Upgrade R
- [ ] Upgrade RStudio

(21 April 2020)
- [x] Upgrade macOS Catalina to 10.15.4
- [x] Install IRkernel
- [ ] Contact Hugh Cayless

(20 April 2020)
- [x] Teleconference with Jeff Witt re: TEI P5 encoding academic medieval Latin texts

(18 April 2020)
- [x] Upgrade Python to 3.8.2

(17 April 2020)
- [x] Teleconference with Patrick Burns re: CLTK backoff lemmatizer
- [x] ICMCL cancelled

(11 April 2020)
- [x] First draft of Burrows's Delta section of Chapter 4

(2 April 2020)
- [x] Finish coding Zipf (1935) ab^2 = k demo
- [x] Modify burrows2.py to output results directly to CSV file
- [x] Repartition Gratian's _dicta_ into ten sample files: cases, laws, orders1, orders2, other, monastic, heresy, marriage, penance, second

(31 March 2020)
- [x] Order Stephan Dusil, "The Decretum of Gratian: A Janus-Faced Collection", from ILL.

(7 March 2020)
- [x] Record bug report for MGH Friedberg e-text: D.23 c.2 (1.79) (See Anders Winroth email, 23 Augest 2019)

(28 February 2020)
- [x] Create requirements.txt file in Backoff repository for Patrick Burns and commit: `pip3 freeze > requirements.txt`
- [x] Apply for ICMCL bursary

(27 February 2020)
- [x] Chapter 4: add footnote with formula for least squares linear regression
- [x] Clear backlog of git commits for Gratian repository

(10-11 Feb 2020)
- [x] Recheck statistical calculations in visualize.py. Population standard deviations calculated by pstdev and HP 48GX disagree: 1.6323 (pstdev) and 1.9022 (HP 48GX) for _in_, 1.2571 (pstdev) and 1.4649 (HP 48GX) for _non_.

(6 Feb 2020)
- [x] Correct serious flaw in introductory _in_/_non_ frequency and z-score plots. (Computed standard deviation as if samples of R1 and R2 _dicta_ were of the same size and had equal weight, see 22 Jan 2020)

(5 Feb 2020)
- [x] Recover PDF of Winroth, _The Making of Gratian's Decretum_
- [x] Write Python program to group dicta texts into samples of between 2500 and 3000 words along dictum boundaries

(4 Feb 2020)
- [x] Update to stylo version: 0.7.1
- [x] Update to macOS Catalina 10.15.3
- [x] Write Python program to randomize the word order of samples

(3 Feb 2020)
- [x] Read Maciej Eder, "Does size matter? Authorship, attribution, small samples, big problem"

(29 Jan 2020)
- [x] Report CLTK backoff lemmatizer problems to Patrick Burns (patrick@diyclassics.org)
- [x] Correct OCR error in MGH e-text of Fr. D.6 d.p.c.3 reported by Anders Winroth, 6 Oct 2019. (Change _**quantam** ad moralem intelligentiam_ to _**quantum** ad moralem intelligentiam_) **Fixed only in Gratian/analysis/edF.txt.**

(24 Jan 2020)
- [x] Meet with Stan Chodorow
- [x] Confirm that the 21 January 2019 version of Sg_PCA_52_001.jpg was generated from a valid text sample including C.Prima d.init. and C.3 d.init.

(23 Jan 2020)
- [x] Upgrade pip from 19.3.1 to 20.0.1
- [x] Upgrade Django from 2.2.6 to 3.0.2. This is a major change and requires more testing that I've been able to do so far.
- [x] Incorporate Sg case statements PCA plot into chapter4.md (plot first, then explanation)
- [x] Clean up (commit, merge, rebase) GitHub Critical repository
- [x] Install Jekyll 4.0.0

(22 Jan 2020)
- [x] Create introductory _in_/_non_ frequency plot and incorporate it into chapter4.md
- [x] Add 'R2' to spelling dictionary. Don't forget to run `:1,$!sort --ignore-case` and `:mkspell! %` in vim to update en.utf-8.add.spl after editing en.utf-8.add!

(21 Jan 2020)
- [x] Incorporate dash-q (_sine questionibus_) case statement plots into chapter4.md

(16 Jan 2020)
- [x] Enroll in MDST 996 Doctoral Dissertation Research

(15 Jan 2020)
- [x] Submit request for candidacy extension to CUA

(14 Jan 2020)
- [x] Teleconference with Ken Pennington. Ken is less interested in translation
  of the case statements than analysis. Why are the case statements in Sg so
  different than the ones in the first and second recensions? Look at the
  development/progression of thought from the second case in Sg to Causa 1. (Ken
  wrote an article about this.) Are the issues of fact or the issues of law the
  same?

(13 Jan 2020)
- [x] eduroam access restored

(12 Jan 2020)
- [x] USD GMail access restored

(10 Jan 2020)
- [x] Install pylint-2.4.4

(9 Jan 2020)
- [x] Update to macOS Catalina 10.15.2

(8 Jan 2020)
- [x] Disable SIP (System Integrity Protection or rootless):  
`csrutil disable` from Terminal in Recovery Mode  
- [x] Install wdiff 1.2.2 in /usr/local/bin

(6 Jan 2020)
- [x] Upgrade Python3 to 3.7.6
- [x] Install CLTK (cltk-0.1.113)

(31 Dec 2019)
- [x] Install enscript 1.6.6 in /usr/local/bin

### 2019 Dissertation Checklist

- [ ] Transcribe Fd C.4 d.init.
- [ ] Translate R1 C.4 d.init.
- [ ] Is "Diffinimus eum rite" (4.1.1) a marker that the text is
descended from the α hyparchetype? (All of the formal sources in
Clavis Canonum read "Definimus eum rite".)

(15 Dec 2019)
+ **†John F. Burrows (1928-2019)**

(30 Nov 2019)
+ **†Brian Tierney (1922-2019)**

(14 August 2019)
- [x] Submit proposal for paper for 16th International Congress of Medieval Canon Law

(13 August 2019)
- [x] Submit proposal for poster presentation for 16th International Congress of Medieval Canon Law

(1 Jul 2019)
- [x] Correct OCR error in MGH e-text of Fr. C.4 d.init. (Change _Sexto, si in episcoporum **indicio** ..._ to _Sexto, si in episcoporum **iudicio** ..._) **Fixed only in Gratian/analysis/edF.txt.**

(25 Jun 2019)
- [x] Run stylo() on Gratian0-q.txt

(20 Jun 2019)
- [x] Read Samuels and McGann, "Deformance and Interpretation"

(18 Jun 2019)
- [x] Update to R version 3.6.0 (2019-04-26)
- [x] Update to RStudio Version 1.2.1335
- [x] Update to stylo version: 0.6.9

(17 Jun 2019)
- [x] Create modified sample file Gratian0-q.txt (1618 words) for case statements minus questions (remove everything after, e.g., *Hic primum queritur*, etc.)

(23 May 2019)
+ **†Peter Landau (1935-2019)**

(5 March 2018)
+ **†Hayden White (1928-2018)**

(9 July 2017)
+ **†Gene Brucker (1924-2017)**

(27 April 2017)
+ **†John Noonan (1926-2017)**
