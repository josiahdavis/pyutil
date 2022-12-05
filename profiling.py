import numpy as np
import argparse

from line_profiler import LineProfiler

@profile
def f(a, b):
  x = np.empty(shape=(a, b))
  for i in range(a):
    for j in range(b):
      x[i, j] = np.random.random()
  return x

if __name__ == "__main__":
  """
  # Run the following from CLI
  kernprof -l -v pyutil/profiling.py --a 1000 --b 1000000
  """
  parser = argparse.ArgumentParser(description="My description")
  parser.add_argument("--a", default=10000)
  parser.add_argument("--b", default=10000)
  args = parser.parse_args()
  f(args.a, args.b)
