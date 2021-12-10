all: appendix1.docx appendix2.docx appendix3.docx

appendix1.markdown: appendix1.md
	pandoc -o appendix1.markdown -f markdown -t gfm appendix1.md
	cat ../lic/license.html >> appendix1.markdown

appendix2.markdown: appendix2.md
	pandoc -o appendix2.markdown -f markdown -t gfm appendix2.md
	cat ../lic/license.html >> appendix2.markdown

appendix3.markdown: appendix3.md
	pandoc -o appendix3.markdown -f markdown -t gfm appendix3.md
	cat ../lic/license.html >> appendix3.markdown

appendix1.docx:	appendix1.md ../ref/appendix.docx
	pandoc -o appendix1.docx --reference-doc=../ref/appendix.docx appendix1.md

appendix2.docx:	appendix2.md ../ref/appendix.docx
	pandoc -o appendix2.docx --reference-doc=../ref/appendix.docx appendix2.md

appendix3.docx:	appendix3.md ../ref/appendix.docx
	pandoc -o appendix3.docx --reference-doc=../ref/appendix.docx appendix3.md

clean:
	rm -i appendix1.docx appendix2.docx appendix3.docx

