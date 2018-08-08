all: chapter2a.docx chapter2b.docx chapter2c.docx

chapter2a.docx: chapter2a.md ../bib/merged.bib ../reference/draft.docx
	pandoc -o chapter2a.docx --filter pandoc-citeproc --reference-doc=../reference/draft.docx chapter2a.md

chapter2b.docx: chapter2b.md ../bib/merged.bib ../reference/draft.docx
	pandoc -o chapter2b.docx --filter pandoc-citeproc --reference-doc=../reference/draft.docx chapter2b.md

chapter2c.docx: chapter2c.md ../bib/merged.bib ../reference/draft.docx
	pandoc -o chapter2c.docx --filter pandoc-citeproc --reference-doc=../reference/draft.docx chapter2c.md

clean:
	rm -i chapter2a.docx chapter2b.docx chapter2c.docx

