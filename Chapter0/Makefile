chapter0.docx: chapter0.md ../bib/merged.bib ../reference/final.docx
	pandoc -o chapter0.docx --filter pandoc-citeproc --reference-doc=../reference/final.docx chapter0.md

clean:
	rm -i chapter0.docx

