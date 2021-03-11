restart.docx: restart.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o restart.docx --citeproc --reference-doc=../ref/draft.docx restart.md

draft.docx: draft.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o draft.docx --citeproc --reference-doc=../ref/draft.docx draft.md

clean:
	rm -i restart.docx

