all: chapter2.markdown chapter2o.markdown

chapter2.markdown: chapter2.md ../bib/merged.bib
	pandoc -o chapter2.markdown --citeproc -f markdown-smart -t gfm chapter2.md
	cat ../lic/license.html >> chapter2.markdown

chapter2o.markdown: chapter2o.md ../bib/merged.bib
	pandoc -o chapter2o.markdown --citeproc -f markdown-smart -t gfm chapter2o.md
	cat ../lic/license.html >> chapter2o.markdown

chapter2.docx: chapter2.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o chapter2.docx --citeproc --reference-doc=../ref/draft.docx chapter2.md

chapter2o.docx: chapter2o.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o chapter2o.docx --citeproc --reference-doc=../ref/draft.docx chapter2o.md

clean:
	rm -i chapter2.markdown chapter2o.markdown chapter2.docx presentation.docx chapter2o.docx

