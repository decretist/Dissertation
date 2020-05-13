all: draft.docx chapter4.docx zipf.docx burrows.docx definition.docx corpus.docx

corpus.docx: corpus.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o corpus.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx corpus.md

burrows.docx: burrows.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o burrows.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx burrows.md

definition.docx: definition.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o definition.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx definition.md

zipf.docx: zipf.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o zipf.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx zipf.md

draft.docx: draft.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o draft.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx draft.md

chapter4.docx: chapter4.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o chapter4.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx chapter4.md

ICMCL.docx: ICMCL.md project.bib ../ref/reference.docx
	pandoc -o ICMCL.docx --filter pandoc-citeproc --reference-doc=../ref/reference.docx ICMCL.md

Rem_Non_Novam.docx: Rem_Non_Novam.md project.bib ../ref/reference.docx
	pandoc -o Rem_Non_Novam.docx --filter pandoc-citeproc --reference-doc=../ref/reference.docx Rem_Non_Novam.md

clean:
	rm -i chapter4.docx draft.docx zipf.docx burrows.docx definition.docx

