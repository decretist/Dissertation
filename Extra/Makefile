all: causa4.markdown n-grams.markdown sg.markdown correctores.markdown

causa4.markdown: causa4.md
	pandoc -o causa4.markdown -f markdown-smart -t gfm causa4.md
	cat ../lic/license.html >> causa4.markdown

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
	rm -i causa4.markdown n-grams.markdown sg.markdown correctores.markdown

