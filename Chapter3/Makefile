all: chapter3.docx chapter3a.docx chapter3b.docx chapter3m.docx

chapter3.docx: chapter3.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter3.docx --citeproc --reference-doc=../ref/final.docx chapter3.md

chapter3a.docx: chapter3a.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o chapter3a.docx --citeproc --reference-doc=../ref/draft.docx chapter3a.md

chapter3b.docx: chapter3b.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o chapter3b.docx --citeproc --reference-doc=../ref/draft.docx chapter3b.md

chapter3m.docx: chapter3m.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o chapter3m.docx --citeproc --reference-doc=../ref/draft.docx chapter3m.md

clean:
	rm -i chapter3.docx chapter3a.docx chapter3b.docx chapter3m.docx

