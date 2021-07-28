ICMCL.docx: ICMCL.md project.bib ../ref/reference.docx
	pandoc -o ICMCL.docx --citeproc --reference-doc=../ref/reference.docx ICMCL.md

Rem_Non_Novam.docx: Rem_Non_Novam.md project.bib ../ref/reference.docx
	pandoc -o Rem_Non_Novam.docx --citeproc --reference-doc=../ref/reference.docx Rem_Non_Novam.md

clean:
	rm -i ICMCL.docx Rem_Non_Novam.docx

