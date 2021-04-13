chapter1.markdown: chapter1.md ../bib/merged.bib
	pandoc -o chapter1.markdown --citeproc -f markdown-smart -t gfm chapter1.md

chapter1.docx: chapter1.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter1.docx --citeproc --reference-doc=../ref/final.docx chapter1.md

school-faculty-university.docx: school-faculty-university.md ../bib/merged.bib ../ref/final.docx
	pandoc -o school-faculty-university.docx --citeproc --reference-doc=../ref/final.docx school-faculty-university.md

clean:
	rm -i chapter1.docx school-faculty-university.docx

