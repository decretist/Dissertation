chapter1.docx: chapter1.md ../bib/merged.bib ../reference/final.docx
	pandoc -o chapter1.docx --filter pandoc-citeproc --reference-doc=../reference/final.docx chapter1.md

clean:
	rm -i chapter1.docx

