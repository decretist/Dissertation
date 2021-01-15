chapter3a.docx: chapter3a.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o chapter3a.docx --citeproc --reference-doc=../ref/draft.docx chapter3a.md

chapter3.docx: chapter3.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter3.docx --citeproc --reference-doc=../ref/final.docx chapter3.md

clean:
	rm -i chapter3.docx

