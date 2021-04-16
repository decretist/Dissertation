all: n-grams.markdown correctores.markdown

n-grams.markdown: n-grams.md ../bib/merged.bib
	pandoc -o n-grams.markdown --citeproc -f markdown-smart -t markdown n-grams.md

correctores.markdown: correctores.md ../bib/merged.bib
	pandoc -o correctores.markdown --citeproc -f markdown-smart -t markdown correctores.md

clean:
	rm -i n-grams.markdown correctores.markdown

