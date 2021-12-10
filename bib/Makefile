all: biblio.docx biblio.markdown

biblio.docx: biblio.md merged.bib ../ref/biblio.docx
	pandoc -o biblio.docx --citeproc --reference-doc=../ref/biblio.docx biblio.md

biblio.markdown: biblio.md merged.bib
	pandoc -o biblio.markdown --citeproc -f markdown-smart -t gfm biblio.md
	cat ../lic/license.html >> biblio.markdown

clean:
	rm -i biblio.docx biblio.markdown

