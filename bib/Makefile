biblio.markdown: biblio.md merged.bib
	pandoc -o biblio.markdown --citeproc -f markdown-smart -t gfm biblio.md
	cat ../lic/license.html >> biblio.markdown

biblio.docx: biblio.md merged.bib ../ref/final.docx
	pandoc -o biblio.docx --citeproc --reference-doc=../ref/final.docx biblio.md

clean:
	rm -i biblio.markdown biblio.docx

