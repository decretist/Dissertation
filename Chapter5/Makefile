all: sg.docx chapter5.docx

sg.docx: sg.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o sg.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx sg.md

chapter5.docx: chapter5.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o chapter5.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx chapter5.md

clean:
	rm -i sg.docx chapter5.docx

