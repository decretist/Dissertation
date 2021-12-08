all: chapter4.docx chapter4.markdown

chapter4.docx: chapter4.md ../bib/merged.bib ../ref/deposit.docx
	pandoc -o chapter4.docx --citeproc --reference-doc=../ref/deposit.docx chapter4.md

chapter4.markdown: chapter4.md ../bib/merged.bib
	pandoc -o chapter4.markdown --citeproc -f markdown-smart -t gfm chapter4.md
	cat ../lic/license.html >> chapter4.markdown

clean:
	rm -i chapter4.docx chapter4.markdown

