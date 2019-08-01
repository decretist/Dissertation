all: chapter5.docx six.docx

chapter5.docx: chapter5.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o chapter5.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx chapter5.md

six.docx: six.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o six.docx --filter pandoc-citeproc --reference-doc=../ref/draft.docx six.md

clean:
	rm -i chapter5.docx six.docx

