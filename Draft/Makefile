draft.docx: draft.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o draft.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx draft.md

table.docx: table.md ../ref/draft.docx
	pandoc -o table.docx --reference-doc=../ref/draft.docx table.md
clean:
	rm -i draft.docx

