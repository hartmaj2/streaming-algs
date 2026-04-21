# Big picture of streaming algs
- we have lots of data and we want to capture some statistic

- sources of big data
  - sensors
  - medical data - genomes, vital signs
  - electronic activities - site visits, emails
  - business data - items purchased by customers etc.

- main questions:
  - what features/statistics do we want to capture (what should be preserved)
  - how accurate do we need to be

- compression vs summaries
  - compression - uses redundancy in data to reduce size
    - does not guarantee any reduction
    - we want to be able to reconstruct the object without any loss
  - summary 
    - we will not even be able reconstruct the data stream

- examples of summaries
  - sum + count $\to$ retrieve average
  - min + max $\to$ range of temperatures
  - how to retrieve the median?

## Data models

- summaries can be built upon various types of data
  - sets, multisets, weighted sets (represented as one vector), vectors (stored together in a vector of vectors -> a matrix), geometric data, graphs, 

## Operations on summaries

- initialize - how the data structure will look at start (can involve randomized stuff)
- update 
- merge - to allow parallel processing
- construct - create the summary from given data in offline setting (to save time then repeating update calls)
- compress - when a summary grows over time, this operation tries to reduce its size

## Models of computation

- streaming model - we just need the ability to UPDATE
- parallel processing 
  - how to assign which machine gets which data?
  - we can use MERGE to construct the final summary
- distributed processing 

## Implementation of summaries

- nothing important (implementation details)

## Guarantees

- if we were able to answer every possible query exactly $\rarr$ we could construct a sequence of questions to find out what the original data were
  - this leads to lower bounds on size of every summary which provides such guarantees
- to provide compact summary $\rarr$ we must lose some accuracy
  - randomization vs approximation

### Approximation

- when data is numerical
  - relative approximation
    - we can guarantee that we are within $\epsilon$ relative error from the true answer
  - additive approximation
    - we're within some fixed $\delta$ from the true answer

### Randomization

- we claim that we give a correct answer with some probability

### Combining

- we can combine the two above to claim a guarantee in form
  - with some probability, we give an $\epsilon$ approximation of the correct answer

## Summaries in applications

### Data center

- monitor statistics in a big data center
  - problem: we need to keep track of hundreds of GB of data and be able to send this data per second for evaluation
  - we can use Count-Min Sketch or SpaceSaving

### Network Scanning Detection

- want to detect if somebody performs a port scan
- we can use a counter alongside a Bloom Filter to count only distinct addresses accessed

### Service Quality Management

- we have SLA such as k percent of responses are made within t milliseconds
  - we want to check if we adhere to this agreements precisely but sometimes we want just a quick estimate which will allow us to see if there is a risk of not adhering and that we should make a proper checkup
- if we had fixed x and t, we could just have counters but we want flexibility in parameter k and t
  - we will use GK or Q-Digest
- Q-Digest - bounded space no matter how many items summarized
- GK - grows logarithmically with size of input
- moving window of response times
  - we divide the times into buckets and have a summary for each bucket, if a window goes over multiple buckets, we merge all of them together

### Query optimization

- in databases operation takes time different times if we perform them in different orders
- to find out the best order, we need to estimate, how many items are there with given key for example 
- usually focus on selectivity of a predicate - how many items of the given predicate satisfy a given property
  - use RandomSample to estimate this

- technique - equi depth histogram
  - separate n data into k buckets s.t. each bucket has around n/k elements
  - then the buckets correspond to quantiles, we just takes as many buckets as we can and then take part of the last bucket

### Ad Impression Monitoring and Audience Analysis

- goal - see how many distinct people have seen our ad
  - we can use KMV or HLL
- interesting question
  - have summary for views by attributes - female, age 18-35, university educated etc.
  - we can combine these using KMV or HLL to get approximation of the views by people in the intersection

## Computational and Mathematical tools

- tail bounds
  - Markov and proof (we want to use the formulation with $\mathbb{E}[X]$ in the fraction, where do we need the assumption $X \geq 0$)
  - Chebyshev inequality 
    - use markov on $Y = (X - \mathbb{E}[X])^2$
    - then substitute $k$ for $k^2$
    - then use the fact that $\Pr[ X^2 \geq k^2] = \Pr[|X| \geq k]$
  - Chernoff bounds
    - skipped - how to arrive at picking $t = \frac{2}{5}\rho$

- variance and covariance formulas

- union bound
  - we can use it when we have $n$ bad events and the probability of each event is some small function w.r.t. $n$, like $\frac{1}{n^2}$.

- principle of deferred decisions
  - scenario: we want to sample uniformly at random from disjoint sets $S_1$ an $S_2$ of sizes $n_1$ and $n_2$
  - we can do this by choosing an element from the union with prob $\frac{1}{n_1+n_2}$
  - but we can achieve the same by first picking a set from which we will sample and then choose uniformly from the selected set
    - rule: pick $S_1$ with prob $\frac{n_1}{n_1+n_2}$.
    - instead of having to pick the item right away, we instead first pick the set
    - we do the decision, which specific element to pick later

- Chernoff bounds argument
  - scenario: 
    - we want to estimate quantity $Q$
    - we can measure to get result $x$ which is close enough to the real value with probability $p$
  - we can estimate this quantity by taking the median of $n$ measurements
  - observation: 
    - if less than $\frac{1}{2}$ of the estimates is bad, then the median is a good estimate
  - the estimates are just bernoulli variables with prob $p$
  - we can calculate, that $(1-p)$ fraction of estimates is bad (by binomial distribution)
    - thus we know that the median estimate is bad only if $(1-p) \cdot k \geq \frac{1}{2}$
      - so the number of bad events must exceed its expected value by a fraction of $\frac{1}{2(1-p)}$
  - we can solve the point above by applying Chernoff bound

- Hash functions
  - t-wise independence
    - small probability that any $t$-tuple of distinct values maps to a chosen $t$-tuple of images
  - cryptographic hash functions
    - hard to invert - only possibility is to try evaluating all values
    - are 10 times slower than the fastest non-cryptographic functions
  - popular non-cryptographic hashing function - murmurhash from 2008