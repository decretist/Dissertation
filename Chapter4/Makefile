all: chapter4.docx pca.docx

chapter4.docx: chapter4.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter4.docx --filter pandoc-citeproc --reference-doc=../ref/final.docx chapter4.md

pca.docx: pca.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o pca.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx pca.md

ICMCL.docx: ICMCL.md project.bib ../ref/reference.docx
	pandoc -o ICMCL.docx --filter pandoc-citeproc --reference-doc=../ref/reference.docx ICMCL.md

Rem_Non_Novam.docx: Rem_Non_Novam.md project.bib ../ref/reference.docx
	pandoc -o Rem_Non_Novam.docx --filter pandoc-citeproc --reference-doc=../ref/reference.docx Rem_Non_Novam.md

clean:
	rm -i chapter4.docx pca.docx

