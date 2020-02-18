all: antecedents.docx visualization.docx chapter4.docx

antecedents.docx: antecedents.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o antecedents.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx antecedents.md

visualization.docx: visualization.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o visualization.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx visualization.md

chapter4.docx: chapter4.md ../bib/merged.bib ../ref/reference.docx
	pandoc -o chapter4.docx --filter pandoc-citeproc --reference-doc=../ref/reference.docx chapter4.md

ICMCL.docx: ICMCL.md project.bib ../ref/reference.docx
	pandoc -o ICMCL.docx --filter pandoc-citeproc --reference-doc=../ref/reference.docx ICMCL.md

Rem_Non_Novam.docx: Rem_Non_Novam.md project.bib ../ref/reference.docx
	pandoc -o Rem_Non_Novam.docx --filter pandoc-citeproc --reference-doc=../ref/reference.docx Rem_Non_Novam.md

clean:
	rm -i chapter4.docx

