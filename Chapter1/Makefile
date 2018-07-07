all: chapter1.docx school-faculty-university.docx
chapter1.docx:	chapter1.md chapter1.bib ../reference/reference.docx
	pandoc -o chapter1.docx --filter pandoc-citeproc --reference-doc=../reference/reference.docx chapter1.md

chapter1b.docx:	chapter1b.md chapter1.bib ../reference/reference.docx
	pandoc -o chapter1b.docx --filter pandoc-citeproc --reference-doc=../reference/reference.docx chapter1b.md

school-faculty-university.docx:	school-faculty-university.md chapter1.bib ../reference/reference.docx
	pandoc -o school-faculty-university.docx --filter pandoc-citeproc --reference-doc=../reference/reference.docx school-faculty-university.md

clean:
	rm -i chapter1.docx school-faculty-university.docx

