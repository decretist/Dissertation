all:	chapter4.docx ICMCL.docx Rem_Non_Novam.docx

chapter4.docx:	chapter4.md chapter4.bib reference.docx
	pandoc -o chapter4.docx --filter pandoc-citeproc --reference-doc=reference.docx chapter4.md

ICMCL.docx:	ICMCL.md project.bib reference.docx
	pandoc -o ICMCL.docx --filter pandoc-citeproc --reference-doc=reference.docx ICMCL.md

Rem_Non_Novam.docx:	Rem_Non_Novam.md project.bib reference.docx
	pandoc -o Rem_Non_Novam.docx --filter pandoc-citeproc --reference-doc=reference.docx Rem_Non_Novam.md

clean:
	rm -i chapter4.docx ICMCL.docx Rem_Non_Novam.docx chapter4.docx

