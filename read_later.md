- how the distributions work
  - pareto distribution
  - gumbel distribution

- definition of uniform rank error for quantile using $q' = q \pm \eps$

- how do these work:
  - rewise GK
  - t-digest
  - MomentSketch

- look for textbook explanation of SplineSketch

- did anybody already try deletion for buckets & linear interpolation?

- Munro and Paterson
  - why we cannot answer exact median with less than linear space (communication complexity argument)

- implications of the paper [Matrix Factorization Approach in Turnstile Streaming](https://arxiv.org/html/2607.28819) on dynamic streams
  - what does it mean for me? does Pavel know about it?

- so the interpolation is called piecewise because we do not have to know the whole function to be able to interpolate
- do we compute the interpolation every time we perform a query?

- why the heuristic error uses the $l_i^2$ normalization factor?