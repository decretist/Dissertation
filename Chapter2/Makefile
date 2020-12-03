all: chapter2.docx presentation.docx organization.docx chapter2c.docx

chapter2.docx: chapter2.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter2.docx --citeproc --reference-doc=../ref/final.docx chapter2.md

presentation.docx: presentation.md ../bib/merged.bib ../ref/final.docx
	pandoc -o presentation.docx --citeproc --reference-doc=../ref/final.docx presentation.md

organization.docx: organization.md ../bib/merged.bib ../ref/final.docx
	pandoc -o organization.docx --citeproc --reference-doc=../ref/final.docx organization.md

chapter2c.docx: chapter2c.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter2c.docx --citeproc --reference-doc=../ref/final.docx chapter2c.md

clean:
	rm -i chapter2.docx presentation.docx organization.docx chapter2c.docx

