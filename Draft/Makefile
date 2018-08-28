draft.docx: draft.md ../bib/merged.bib ../reference/draft.docx
	pandoc -o draft.docx --filter pandoc-citeproc --reference-doc=../reference/draft.docx draft.md

clean:
	rm -i draft.docx

