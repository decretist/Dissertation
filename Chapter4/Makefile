all: chapter4.markdown chapter4.docx

chapter4.markdown: chapter4.md ../bib/merged.bib
	pandoc -o chapter4.markdown --citeproc -f markdown-smart -t gfm chapter4.md
	cat ../lic/license.html >> chapter4.markdown

chapter4.docx: chapter4.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter4.docx --citeproc --reference-doc=../ref/final.docx chapter4.md

ICMCL.docx: ICMCL.md project.bib ../ref/reference.docx
	pandoc -o ICMCL.docx --citeproc --reference-doc=../ref/reference.docx ICMCL.md

Rem_Non_Novam.docx: Rem_Non_Novam.md project.bib ../ref/reference.docx
	pandoc -o Rem_Non_Novam.docx --citeproc --reference-doc=../ref/reference.docx Rem_Non_Novam.md

clean:
	rm -i chapter4.markdown chapter4.docx

