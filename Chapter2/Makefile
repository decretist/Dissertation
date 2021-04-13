chapter2.markdown: chapter2.md ../bib/merged.bib
	pandoc -o chapter2.markdown --citeproc -f markdown-smart -t gfm chapter2.md

chapter2.docx: chapter2.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter2.docx --citeproc --reference-doc=../ref/final.docx chapter2.md

presentation.docx: presentation.md ../bib/merged.bib ../ref/final.docx
	pandoc -o presentation.docx --citeproc --reference-doc=../ref/final.docx presentation.md

organization.docx: organization.md ../bib/merged.bib ../ref/final.docx
	pandoc -o organization.docx --citeproc --reference-doc=../ref/final.docx organization.md

clean:
	rm -i chapter2.markdown chapter2.docx presentation.docx organization.docx

