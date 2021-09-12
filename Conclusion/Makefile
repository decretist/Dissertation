conclusion.markdown: alt-conclusion.md ../bib/merged.bib
	pandoc -o conclusion.markdown --citeproc -f markdown-smart -t gfm alt-conclusion.md
	cat ../lic/license.html >> conclusion.markdown

conclusion.docx: alt-conclusion.md ../bib/merged.bib ../ref/final.docx
	pandoc -o conclusion.docx --citeproc --reference-doc=../ref/final.docx alt-conclusion.md

clean:
	rm -i conclusion.markdown

