obicitur.markdown: obicitur.md ../bib/merged.bib
	pandoc -o obicitur.markdown --citeproc -f markdown-smart -t gfm obicitur.md

obicitur.docx: obicitur.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o obicitur.docx --citeproc --reference-doc=../ref/draft.docx obicitur.md

draft.docx: draft.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o draft.docx --citeproc --reference-doc=../ref/draft.docx draft.md

clean:
	rm -i obicitur.docx

