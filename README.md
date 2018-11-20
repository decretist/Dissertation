# the Gratian project

![Gratian](img/Gratian.jpg)

## Dissertation

### Chapter 1
```
pandoc -f docx -t markdown "Evans-HIGR 295 Draft-SC Accept Changes.docx" -o higr295.md
```

### Chapter 3
```
pandoc -f docx -t markdown "Chapter 3 - Gratian.docx" -o chapter3-gratian.md
```

### spellfile
```
:set spell
:set spelllang=en_us
:set spellfile=$HOME/Work/Dissertation/spl/en.utf-8.add
```
If you hand-edit the .add spellfile,
you will have to re-generate the .spl database:
```
:1,$!sort --ignore-case
:mkspell! %
```
