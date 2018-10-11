all: chapter2.docx presentation.docx organization.docx chapter2c.docx

chapter2.docx: chapter2.md ../bib/merged.bib ../reference/final.docx
	pandoc -o chapter2.docx --filter pandoc-citeproc --reference-doc=../reference/final.docx chapter2.md

presentation.docx: presentation.md ../bib/merged.bib ../reference/draft.docx
	pandoc -o presentation.docx --filter pandoc-citeproc --reference-doc=../reference/draft.docx presentation.md

organization.docx: organization.md ../bib/merged.bib ../reference/draft.docx
	pandoc -o organization.docx --filter pandoc-citeproc --reference-doc=../reference/draft.docx organization.md

chapter2c.docx: chapter2c.md ../bib/merged.bib ../reference/draft.docx
	pandoc -o chapter2c.docx --filter pandoc-citeproc --reference-doc=../reference/draft.docx chapter2c.md

clean:
	rm -i chapter2.docx presentation.docx organization.docx chapter2c.docx

