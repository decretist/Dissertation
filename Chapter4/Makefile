all: chapter4.markdown successes.markdown pca.markdown

chapter4.markdown: chapter4.md ../bib/merged.bib
	pandoc -o chapter4.markdown --citeproc -f markdown-smart -t gfm chapter4.md
	cat ../lic/license.html >> chapter4.markdown

successes.markdown: successes.md ../bib/merged.bib
	pandoc -o successes.markdown --citeproc -f markdown-smart -t gfm successes.md
	cat ../lic/license.html >> successes.markdown

pca.markdown: pca.md ../bib/merged.bib
	pandoc -o pca.markdown --citeproc -f markdown-smart -t gfm pca.md
	cat ../lic/license.html >> pca.markdown

chapter4.docx: chapter4.md ../bib/merged.bib ../ref/final.docx
	pandoc -o chapter4.docx --citeproc --reference-doc=../ref/final.docx chapter4.md

successes.docx: successes.md ../bib/merged.bib ../ref/final.docx
	pandoc -o successes.docx --citeproc --reference-doc=../ref/final.docx successes.md

pca.docx: pca.md ../bib/merged.bib ../ref/draft.docx
	pandoc -o pca.docx --citeproc --reference-doc=../ref/draft.docx pca.md

ICMCL.docx: ICMCL.md project.bib ../ref/reference.docx
	pandoc -o ICMCL.docx --citeproc --reference-doc=../ref/reference.docx ICMCL.md

Rem_Non_Novam.docx: Rem_Non_Novam.md project.bib ../ref/reference.docx
	pandoc -o Rem_Non_Novam.docx --citeproc --reference-doc=../ref/reference.docx Rem_Non_Novam.md

clean:
	rm -i chapter4.markdown successes.markdown pca.markdown chapter4.docx successes.docx pca.docx

