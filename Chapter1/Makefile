chapter1.docx:	chapter1.md chapter1.bib ../reference/reference.docx
	pandoc -o chapter1.docx --filter pandoc-citeproc --reference-doc=../reference/reference.docx chapter1.md

chapter1b.docx:	chapter1b.md chapter1.bib ../reference/reference.docx
	pandoc -o chapter1b.docx --filter pandoc-citeproc --reference-doc=../reference/reference.docx chapter1b.md

clean:
	rm -i chapter1.docx

