all:	draft.docx

draft.docx:	draft.md
	pandoc -o draft.docx --filter pandoc-citeproc --reference-doc=myref.docx draft.md

myref.docx:
	pandoc --print-default-data-file reference.docx > myref.docx

clean:
	rm -i draft.docx

