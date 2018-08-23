school-faculty-university.docx: school-faculty-university.md ../bib/merged.bib ../reference/final.docx
	pandoc -o school-faculty-university.docx --filter pandoc-citeproc --reference-doc=../reference/final.docx school-faculty-university.md

draft.docx: draft.md ../bib/merged.bib ../reference/draft.docx
	pandoc -o draft.docx --filter pandoc-citeproc --reference-doc=../reference/draft.docx draft.md

clean:
	rm -i draft.docx school-faculty-university.docx

