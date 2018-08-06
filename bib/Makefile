bibliography.docx:	bibliography.md ../bib/chapter1.bib ../reference/final.docx
	pandoc -o bibliography.docx --filter pandoc-citeproc --reference-doc=../reference/final.docx bibliography.md

clean:
	rm -i bibliography.docx

