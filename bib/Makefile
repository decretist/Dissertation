biblio.docx: biblio.md merged.bib ../reference/final.docx
	pandoc -o biblio.docx --filter pandoc-citeproc --reference-doc=../reference/final.docx biblio.md

clean:
	rm -i biblio.docx

