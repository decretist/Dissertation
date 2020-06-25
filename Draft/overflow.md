---
author: Paul Evans
date: June 6, 2020
title: Overflow
---
The two-dimensional visualization above proceeded from the traditional
assumption that Gratian's *dicta*---defined as the hypothetical
case statements (*themata*) plus the first- and second-recension
*dicta* including the *dicta* from *de Pen*.---are the work of a
unitary author, the eponymous Gratian. The consequence of that
assumption for the purpose of experimental design (the design of
that demonstration) is that we can treat the corpus of texts analyzed
in that test/demonstration as the entire population of words
attributable to the author Gratian. Population standard deviation
was therefore the appropriate statistical technique to apply to
visualize word frequency variations among/between samples within
that population.

---

That does not mean that we cannot apply the established techniques
of authorship attribution to Gratian's *dicta*, but it does mean
that we have to make careful decisions about experimental design.

---

First I'm going to discuss in general terms the use of stylometry
for authorship attribution. Then, I'm going to discuss the methodology
and the software that I am using for this project. Finally, I am
going to show the results of stylometric analysis of the case
statements, the first-recension *dicta*, and the second-recension
*dicta* (first without, then with, the *dicta* from *de Penitentia*),
and discuss some possible interpretations of those results.

In theory, that means that you ought to be able to make a list of
every function word in a language, although in practice, that's not
easy to do.

---

Increasing the number of function words also introduces a new
problem. We were able to represent our stylometric analysis of the
frequency of *in* and *non* in the samples from the first- and
second-recension *dicta* on a two-dimensional graph. But there will
be as many dimensions on the graph as there are function words for
which we collect data. And because human beings are not good at
visualizing quantitative data in more than three dimensions, we
need to find a way to reduce the number of dimensions. This is where
the technique of principal component analysis, or PCA, becomes
useful.

[^a]: As of 10 February 2020, there is a bug in the `pstdev()` function
in the standard Python 3 statistics library such that the optional
`mu =` keyword argument to override the value of mean does not work.
Thanks to Saturnino Garcia (University of San Diego Department of
Computer Science) and James Krooskos (UC San Diego Alzheimer's
Disease Cooperative Study) for help reproducing this bug.

    ~~~ {python}
    import math
    import statistics
    def pstdev(data, **kwargs):
        '''Temporary replacement for statistics.pstdev()'''
        mu = None
        if 'mu' in kwargs: mu = kwargs['mu'] # type check: int, float, or None
        if mu == None: mu = statistics.mean(data)
        sum = 0
        for i in range(len(data)):
            sum += (data[i] - mu) ** 2
        return(math.sqrt(sum / len(data)))
    ~~~

