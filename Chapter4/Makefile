all: corpus.docx visualization.docx

burrows.docx: burrows.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o burrows.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx burrows.md

chapter4.docx: chapter4.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o chapter4.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx chapter4.md

corpus.docx: corpus.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o corpus.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx corpus.md

definition.docx: definition.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o definition.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx definition.md

draft.docx: draft.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o draft.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx draft.md

visualization.docx: visualization.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o visualization.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx visualization.md

zipf.docx: zipf.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o zipf.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx zipf.md

ICMCL.docx: ICMCL.md project.bib ../ref/reference.docx
	pandoc -o ICMCL.docx --filter pandoc-citeproc --reference-doc=../ref/reference.docx ICMCL.md

Rem_Non_Novam.docx: Rem_Non_Novam.md project.bib ../ref/reference.docx
	pandoc -o Rem_Non_Novam.docx --filter pandoc-citeproc --reference-doc=../ref/reference.docx Rem_Non_Novam.md

clean:
	rm -i burrows.docx chapter4.docx corpus.docx definition.docx draft.docx visualization.docx zipf.docx 

