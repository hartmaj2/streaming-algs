# Misra Gries Algorithm

- it's variations can be used to find heavy hitters or indices of items for parameter $k$ s.t. their frequency is larger than $\frac{m}{k}$

## How it works

- we keep associative array with cap of keys at most $k$
- we use it normally except when we need to add a key when we already have $k$ keys, we subtract 1 from all keys in the associative array and then remove entries that became $0$

## Analysis

- good property is that the counted frequency in the array cannot be smaller by more than $\frac{m}{k}$ since each subtraction involves $k$ items from the stream and there is $m$ items in the stream total

## Use Cases

1.
- we can use this property to solve the problem of finding the items with frequency higher than $\frac{m}{k}$
  - after the first pass, we know that if item has $f_j$ (frequency) higher than $\frac{m}{k}$ then the value in the associative array has to be larger than zero (by using the bound)
  - but still some items might have value larger than zero in associative array and not have a big real frequency
  - we solve this by doing a second pass where we only look at the $k$ candidates and count their frequencies exactly

2.
- we can find heavy hitters for some epsilon that lie in the range $(\frac{\epsilon}{2},\epsilon)$ by running MG on $k \coloneqq \frac{\epsilon}{2}$ and then taking only the items where in the associative array they have value larger than $m \frac{\epsilon}{2}$
  - this works because of the bound again

## Exercises

- completed first 2/3 in the lecnotes