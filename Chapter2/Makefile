all: chapter2.markdown organization.markdown

chapter2.markdown: chapter2.md ../bib/merged.bib
	pandoc -o chapter2.markdown --citeproc -f markdown-smart -t gfm chapter2.md

organization.markdown: organization.md ../bib/merged.bib
	pandoc -o organization.markdown --citeproc -f markdown-smart -t gfm organization.md

chapter2.docx: chapter2.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter2.docx --citeproc --reference-doc=../ref/final.docx chapter2.md

organization.docx: organization.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o organization.docx --citeproc --reference-doc=../ref/draft.docx organization.md

clean:
	rm -i chapter2.markdown organization.markdown chapter2.docx presentation.docx organization.docx

