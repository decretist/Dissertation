chapter0.docx: chapter0.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter0.docx --filter pandoc-citeproc --reference-doc=../ref/final.docx chapter0.md

clean:
	rm -i chapter0.docx

