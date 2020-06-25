all: chapter5.docx

chapter5.docx: chapter5.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter5.docx --filter pandoc-citeproc --reference-doc=../ref/final.docx chapter5.md

clean:
	rm -i chapter5.docx

