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