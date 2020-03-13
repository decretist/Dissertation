all: draft.docx chapter4.docx tmp.docx

tmp.docx: tmp.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o tmp.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx tmp.md

draft.docx: draft.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o draft.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx draft.md

chapter4.docx: chapter4.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o chapter4.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx chapter4.md

ICMCL.docx: ICMCL.md project.bib ../ref/reference.docx
	pandoc -o ICMCL.docx --filter pandoc-citeproc --reference-doc=../ref/reference.docx ICMCL.md

Rem_Non_Novam.docx: Rem_Non_Novam.md project.bib ../ref/reference.docx
	pandoc -o Rem_Non_Novam.docx --filter pandoc-citeproc --reference-doc=../ref/reference.docx Rem_Non_Novam.md

clean:
	rm -i chapter4.docx

