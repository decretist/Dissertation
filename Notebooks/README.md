## Dissertation/Notebooks

It looks like Jupyter Notebooks are increasingly going to be part
of the dissertation workflow.

```
sudo -H pip3 install jupyter
sudo -H pip3 install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable python-markdown/main
jupyter notebook --no-browser

jupyter trust Notebook.ipynb

jupyter nbconvert --to html Notebook.ipynb
```

### Install IRkernel
```
install.packages('IRkernel')
IRkernel::installspec()
```
This has to be done from Terminal, not R or RStudio.

This will need to be redone the week of 27 April, after the release
of R 4.0.0.
