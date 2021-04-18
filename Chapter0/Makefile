chapter0.markdown: chapter0.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter0.markdown --citeproc -f markdown-smart -t gfm chapter0.md
	cat ../lic/license.html >> chapter0.markdown

chapter0.docx: chapter0.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter0.docx --citeproc --reference-doc=../ref/final.docx chapter0.md

clean:
	rm -i chapter0.markdown chapter0.docx

