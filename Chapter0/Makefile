all: chapter0.docx chapter0.markdown

chapter0.docx: chapter0.md ../bib/merged.bib ../ref/deposit.docx
	pandoc -o chapter0.docx --citeproc --reference-doc=../ref/deposit.docx chapter0.md

chapter0.markdown: chapter0.md ../bib/merged.bib
	pandoc -o chapter0.markdown --citeproc -f markdown-smart -t gfm chapter0.md
	cat ../lic/license.html >> chapter0.markdown

clean:
	rm -i chapter0.docx chapter0.markdown

