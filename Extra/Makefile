all: n-grams.markdown barthes.markdown correctores.markdown

n-grams.markdown: n-grams.md ../bib/merged.bib
	pandoc -o n-grams.markdown --citeproc -f markdown-smart -t gfm n-grams.md

barthes.markdown: barthes.md ../bib/merged.bib
	pandoc -o barthes.markdown --citeproc -f markdown-smart -t gfm barthes.md

correctores.markdown: correctores.md ../bib/merged.bib
	pandoc -o correctores.markdown --citeproc -f markdown-smart -t gfm correctores.md

clean:
	rm -i n-grams.markdown barthes.markdown correctores.markdown

