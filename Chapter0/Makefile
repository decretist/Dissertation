chapter0.docx:	chapter0.md chapter0.bib ../reference/reference.docx
	pandoc -o chapter0.docx --filter pandoc-citeproc --reference-doc=../reference/reference.docx chapter0.md

contents.docx:	contents.md ../reference/reference.docx
	pandoc -o contents.docx --reference-doc=../reference/reference.docx contents.md

clean:
	rm -i chapter0.docx

