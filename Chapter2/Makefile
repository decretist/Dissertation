chapter2.docx:	chapter2.md chapter2.bib reference.docx
	pandoc -o chapter2.docx --filter pandoc-citeproc --reference-doc=reference.docx chapter2.md

reference.docx:
	pandoc --print-default-data-file reference.docx > reference.docx

clean:
	rm -i chapter2.docx

