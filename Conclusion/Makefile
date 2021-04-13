conclusion.markdown: conclusion.md ../bib/merged.bib
	pandoc -o conclusion.markdown --citeproc -f markdown-smart -t gfm conclusion.md

conclusion.docx: conclusion.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o conclusion.docx --citeproc --reference-doc=../ref/draft.docx conclusion.md

clean:
	rm -i conclusion.markdown

