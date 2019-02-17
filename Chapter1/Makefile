chapter1.docx: chapter1.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter1.docx --filter pandoc-citeproc --reference-doc=../ref/final.docx chapter1.md

school-faculty-university.docx: school-faculty-university.md ../bib/merged.bib ../ref/final.docx
	pandoc -o school-faculty-university.docx --filter pandoc-citeproc --reference-doc=../ref/final.docx school-faculty-university.md

clean:
	rm -i chapter1.docx school-faculty-university.docx

