conclusion.markdown: conclusion.md ../bib/merged.bib
	pandoc -o conclusion.markdown --citeproc -f markdown-smart -t gfm conclusion.md
	cat ../lic/license.html >> conclusion.markdown

conclusion.docx: conclusion.md ../bib/merged.bib ../ref/final.docx
	pandoc -o conclusion.docx --citeproc --reference-doc=../ref/final.docx conclusion.md

clean:
	rm -i conclusion.markdown

