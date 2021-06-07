all: chapter3.docx chapter3.markdown

chapter3.markdown: chapter3.md ../bib/merged.bib
	pandoc -o chapter3.markdown --citeproc -f markdown-smart -t gfm chapter3.md
	cat ../lic/license.html >> chapter3.markdown

chapter3.docx: chapter3.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter3.docx --citeproc --reference-doc=../ref/final.docx chapter3.md

clean:
	rm -i chapter3.docx chapter3.markdown

