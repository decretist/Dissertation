chapter1.markdown: chapter1.md ../bib/merged.bib
	pandoc -o chapter1.markdown --citeproc -f markdown-smart -t gfm chapter1.md
	cat ../lic/license.html >> chapter1.markdown

chapter1.docx: chapter1.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter1.docx --citeproc --reference-doc=../ref/final.docx chapter1.md

clean:
	rm -i chapter1.markdown chapter1.docx

