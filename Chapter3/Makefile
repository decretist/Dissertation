all: authorship.markdown chapter3.markdown

authorship.markdown: authorship.md ../bib/merged.bib
	pandoc -o authorship.markdown --citeproc -f markdown-smart -t gfm authorship.md
	
chapter3.markdown: chapter3.md ../bib/merged.bib
	pandoc -o chapter3.markdown --citeproc -f markdown-smart -t gfm chapter3.md

authorship.docx: authorship.md ../bib/merged.bib ../ref/final.docx
	pandoc -o authorship.docx --citeproc --reference-doc=../ref/final.docx authorship.md

chapter3.docx: chapter3.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter3.docx --citeproc --reference-doc=../ref/final.docx chapter3.md

chapter3a.docx: chapter3a.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o chapter3a.docx --citeproc --reference-doc=../ref/draft.docx chapter3a.md

clean:
	rm -i authorship.markdown chapter3.markdown

