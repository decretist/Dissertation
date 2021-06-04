all: chapter3.markdown decretists.markdown

chapter3.markdown: chapter3.md ../bib/merged.bib
	pandoc -o chapter3.markdown --citeproc -f markdown-smart -t gfm chapter3.md
	cat ../lic/license.html >> chapter3.markdown

decretists.markdown: decretists.md ../bib/merged.bib
	pandoc -o decretists.markdown --citeproc -f markdown-smart -t gfm decretists.md
	cat ../lic/license.html >> decretists.markdown

chapter3.docx: chapter3.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter3.docx --citeproc --reference-doc=../ref/final.docx chapter3.md

decretists.docx: decretists.md ../bib/merged.bib ../ref/final.docx
	pandoc -o decretists.docx --citeproc --reference-doc=../ref/final.docx decretists.md

clean:
	rm -i chapter3.markdown decretists.markdown

