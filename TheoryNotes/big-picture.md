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

TODO: sometimes read 1.3.5 (page 25) and the rest