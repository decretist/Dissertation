chapter3.docx:	chapter3.md ../bib/chapter3.bib ../reference/reference.docx
	pandoc -o chapter3.docx --filter pandoc-citeproc --reference-doc=../reference/reference.docx chapter3.md

reference.docx:
	pandoc --print-default-data-file reference.docx > reference.docx

clean:
	rm -i chapter3.docx

