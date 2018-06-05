chapter0.docx:	chapter0.md chapter0.bib reference.docx
	pandoc -o chapter0.docx --filter pandoc-citeproc --reference-doc=reference.docx chapter0.md

reference.docx:
	pandoc --print-default-data-file reference.docx > reference.docx

clean:
	rm -i chapter0.docx

