draft.docx:	draft.md project.bib ../reference/reference.docx
	pandoc -o draft.docx --filter pandoc-citeproc --reference-doc=../reference/reference.docx draft.md

clean:
	rm -i draft.docx

