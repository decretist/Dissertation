---
author: Paul Evans
date: February 6, 2020
title: Stylometry
subtitle: Introductory 2-dimensional visualization
---
Let's take a first look at how this kind of stylometric analysis
works in practice with some actual data from the first- and
second-recension *dicta*, excluding the *dicta* from *de Penitentia*.[^6]
"*In*" is the most frequently occurring word in the *dicta*. There
are 1,450 occurrences of "*in*" out of 56,713 words in the
first-recension *dicta* (2.56%). There are 411 occurrences of "*in*"
out of 14,255 words in the second-recension *dicta* (2.88%). "*In*"
therefore occurs 13% more frequently in the second-recension *dicta*
than it does in the first-recension *dicta*.

"*Non*" is the second most frequently occurring word in the *dicta*.
There are 1,360 occurrences of "*non*" in the first-recension *dicta*
(2.40%). There are 306 occurrences of "*non*" in the second-recension
*dicta* (2.15%). "*Non*" therefore occurs 12% more frequently in
the first-recension *dicta* than in the second-recension *dicta*.

13% for "*in*" and 12% for "*non*" are significant variations for
such common words---it's not like we're talking about low-frequency
words where a small difference in the count can make for a big
difference in percentage.

We could graph the number of occurrences of "*in*" and "*non*" per
100 words of the two samples (from the first- and second-recension
*dicta*), with the percentage frequency of "*in*" on the horizontal
axis, and the percentage frequency of "*non*" on the vertical axis,
and we would have an extremely simplistic visualization of the total
variation between the two samples. Now, we are obviously not going
to make an attribution of authorship based on the frequencies of
only two function words.

![Figure 0a updated  6 Feb 2020](PNGs/Figure_0_frequency_excluding_de_Pen.png)

![Figure 0b updated  6 Feb 2020](PNGs/Figure_0_z-score_excluding_de_Pen.png)

![Figure 0c updated  6 Feb 2020](PNGs/Figure_0_frequency_including_de_Pen.png)

![Figure 0d updated  6 Feb 2020](PNGs/Figure_0_z-score_including_de_Pen.png)

[^6]: Including the *dicta* from *de Penitentia* skews the results
of this analysis significantly. **Changes come overwhelmingly from
first-recension *de Pen.* *dicta* (9525 words) vs. second-recension
*de Pen.* *dicta* (556 words).**

    "*In*" is the most frequently occurring word in the *dicta*.
    There are 1,682 occurrences of "in" out of 66,238 words in the
    first-recension *dicta* (2.54%). There are 431 occurrences of
    "in" out of 14,811 words in the second-recension *dicta* (2.91%).
    "*In*" therefore occurs 14.6% more frequently in the second-recension
    *dicta* than it does in the first-recension *dicta*.

    "Non" is the second most frequently occurring word in the
    *dicta*. There are 1,622 occurrences of "non" in the first-recension
    *dicta* (2.45%). There are 314 occurrences of "non" in the
    second-recension *dicta* (2.12%). "Non" therefore occurs 15.5%
    more frequently in the first-recension *dicta* than in the
    second-recension *dicta*.

