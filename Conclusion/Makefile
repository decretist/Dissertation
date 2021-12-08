all: conclusion.docx conclusion.markdown

conclusion.docx: alt-conclusion.md ../bib/merged.bib ../ref/deposit.docx
	pandoc -o conclusion.docx --citeproc --reference-doc=../ref/deposit.docx alt-conclusion.md

conclusion.markdown: alt-conclusion.md ../bib/merged.bib
	pandoc -o conclusion.markdown --citeproc -f markdown-smart -t gfm alt-conclusion.md
	cat ../lic/license.html >> conclusion.markdown

clean:
	rm -i conclusion.docx conclusion.markdown

