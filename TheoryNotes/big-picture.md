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