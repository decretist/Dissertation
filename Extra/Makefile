all: n-grams.markdown sg.markdown correctores.markdown

n-grams.markdown: n-grams.md ../bib/merged.bib
	pandoc -o n-grams.markdown --citeproc -f markdown-smart -t gfm n-grams.md
	cat ../lic/license.html >> n-grams.markdown

sg.markdown: sg.md
	pandoc -o sg.markdown -f markdown-smart -t gfm sg.md
	cat ../lic/license.html >> sg.markdown

correctores.markdown: correctores.md ../bib/merged.bib
	pandoc -o correctores.markdown --citeproc -f markdown-smart -t gfm correctores.md
	cat ../lic/license.html >> correctores.markdown

clean:
	rm -i n-grams.markdown sg.markdown correctores.markdown

