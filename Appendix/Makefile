all: appendix1.docx appendix2.docx

appendix1.docx:	appendix1.md ../reference/appendix.docx
	pandoc -o appendix1.docx --reference-doc=../reference/appendix.docx appendix1.md

appendix2.docx:	appendix2.md ../reference/appendix.docx
	pandoc -o appendix2.docx --reference-doc=../reference/appendix.docx appendix2.md

clean:
	rm -i appendix1.docx appendix2.docx

