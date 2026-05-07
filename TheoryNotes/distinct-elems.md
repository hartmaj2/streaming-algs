# Estimating number of distinct elements

## Tidemark algorithm

1. let h be a hash function from 2-universal family (! from the universe back to the universe)
2. let z = 0
3. for each element j in the stream:
4.   if zeroes h(j) > z, set z to zeroes h(j)
5. return 2^{z + 1/2}

## Analysis

IMPORTANT: by 2-universality, the author means 2-independence!

- we denote $X_{r,j}$ the indicator, that $h(j)$ has at least $r$ zeroes at the end
- the interesting variable is $Y_{r}$ which is the sum of indicators $X_{r,j}$ over all $j$
  - we would like to bound $Y_{r}$ from being too far from the real value
- for this we will need to bound $\Pr[Y_r > 0]$ and $\Pr[Y_r = 0]$
  - for these bound we will need Markov and Chebyshev (so we need to calculate expected value and variance of $Y_r$)

- then we let $d$ be the number of distinct elements we have really seen and let $\hat{d} = 2^{T+\frac{1}{2}}$
  - then we let $a$ be smallest integer such that $2^{a+\frac{1}{2}} \geq 3d$
  - similarly $b$ largest integer s.t. $2^{b+\frac{1}{2}} \leq \frac{d}{3}$
- the choices of $a$ and $b$ above are nice since they connect event $\hat{d} \geq 3d$ with $Y_a > 0$ on which we have bound (similarly for $b$)

## Median trick

- uses Chernoff bound and the fact, that the bound states that for a fixed relative deviation $\delta$ from the mean $\mu$, the probability that $\Pr[X > (1+\delta)\mu] \leq \exp(-\Theta(\mu))$

- in practice, we have probability $p > \frac{1}{2}$ (just sligtly >) that our algorithm outputs value in the correct range
- we run our algorithm $k$ times and then notice, that if we take the median, then the median is out of range only if at least $\frac{k}{2}$ values are out of range (imagine the sorted outputs as dots next to each other, if we mark as correct at least half of them s.t. we can only mark a contiguous segment, we must always hit the median)
  
- now we want to bound probability that $\Pr[X \geq \frac{k}{2}]$ where $X$ tracks how many bad results we encountered
  - here we have constant relative error $\delta$ but $\mu = k\frac{\sqrt{2}}{3}$ so as we increase $k$ then the probability of bad result decreases exponentially with $k$