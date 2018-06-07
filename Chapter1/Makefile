all: chapter1.docx chapter1b.docx

chapter1.docx:	chapter1.md chapter1.bib reference.docx
	pandoc -o chapter1.docx --filter pandoc-citeproc --reference-doc=reference.docx chapter1.md

chapter1b.docx:	chapter1b.md chapter1b.bib reference.docx
	pandoc -o chapter1b.docx --filter pandoc-citeproc --reference-doc=reference.docx chapter1b.md

reference.docx:
	pandoc --print-default-data-file reference.docx > reference.docx

clean:
	rm -i chapter1.docx chapter1b.docx

