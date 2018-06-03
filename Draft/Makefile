draft.docx:	draft.md project.bib reference.docx
	pandoc -o draft.docx --filter pandoc-citeproc --reference-doc=reference.docx draft.md

reference.docx:
	pandoc --print-default-data-file reference.docx > reference.docx

clean:
	rm -i draft.docx

