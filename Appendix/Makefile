appendix.docx:	appendix.md reference.docx
	pandoc -o appendix.docx --reference-doc=reference.docx appendix.md

reference.docx:
	pandoc --print-default-data-file reference.docx > reference.docx

clean:
	rm -i appendix.docx

