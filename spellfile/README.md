## spellfile
```
:set spell
:set spelllang=en_us
:set spellfile=$HOME/Work/Dissertation/spellfile/en.utf-8.add
```
If you hand-edit the .add spellfile,
you will have to re-generate the .spl database:
```
:1,$!sort --ignore-case
:mkspell! %
```
