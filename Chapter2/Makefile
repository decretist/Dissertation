all: chapter2.markdown chapter2.docx

chapter2.markdown: chapter2.md ../bib/merged.bib
	pandoc -o chapter2.markdown --citeproc -f markdown-smart -t gfm chapter2.md
	cat ../lic/license.html >> chapter2.markdown

chapter2.docx: chapter2.md ../bib/merged.bib ../ref/deposit.docx
	pandoc -o chapter2.docx --citeproc --reference-doc=../ref/deposit.docx chapter2.md

clean:
	rm -i chapter2.markdown chapter2.docx

