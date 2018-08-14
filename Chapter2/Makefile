all: chapter2.docx chapter2c.docx

chapter2.docx: chapter2.md ../bib/merged.bib ../reference/final.docx
	pandoc -o chapter2.docx --filter pandoc-citeproc --reference-doc=../reference/final.docx chapter2.md

chapter2c.docx: chapter2c.md ../bib/merged.bib ../reference/draft.docx
	pandoc -o chapter2c.docx --filter pandoc-citeproc --reference-doc=../reference/draft.docx chapter2c.md

clean:
	rm -i chapter2.docx chapter2c.docx

