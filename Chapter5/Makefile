sg.docx: sg.md ../bib/merged.bib ../reference/draft.docx
	pandoc -o sg.docx --filter pandoc-citeproc --reference-doc=../reference/draft.docx sg.md

chapter5.docx: chapter5.md ../bib/merged.bib ../reference/draft.docx
	pandoc -o chapter5.docx --filter pandoc-citeproc --reference-doc=../reference/draft.docx chapter5.md

clean:
	rm -i chapter5.docx

