
"""
Name: Craig Brooks
PHSX 815 Spring 2023
HW # 5
Due Date 2/17/2023
This code performs Accept/Reject sampling for a function, and defines the region which is a "hit" and which is a "miss"
"""

import matplotlib.pyplot as plt
import numpy as np
import sys

if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
  if '-h' in sys.argv or '--help' in sys.argv:
    print ("Usage: %s [-seed -size -reg (0 or 1) ]" % sys.argv[0])
    print
    sys.exit(1)

  if '-seed' in sys.argv:
    p = sys.argv.index('-seed')
    seed = int(sys.argv[p+1])
  else:
    seed = 666
  if '-size' in sys.argv:
    p = sys.argv.index('-size')
    size = int(sys.argv[p+1])
  else:
    size = 100
  if '-reg' in sys.argv:
    p = sys.argv.index('-reg')
    reg = int(sys.argv[p+1])
  else:
    reg = 0

  def f(x):
      return x**4 - 2*x**3 +1
  def g(x):
      return np.full(x.shape, 1)
  
  np.random.seed(seed)
  
  print(seed)
  print(size)
  print(reg)

  xs = np.linspace(0,1,1000)

  y1 = f(xs)
  y2 = g(xs)
  plt.plot(xs, y1, label = "f(x)")
  plt.plot(xs, y2, label = "g(x)")
  plt.xlabel("x")

  plt.ylabel("y")
  plt.fill_between(xs, y1, reg, alpha = .2)
  plt.legend()
  x_samp = np.random.uniform(low=0, high=1, size=int(size))
  y_samp = np.random.uniform(low=0, high=1, size=int(size))
  
  if reg == 0:
    accept = (y_samp < f(x_samp)).astype(int)
  else:
    accept = (y_samp > f(x_samp)).astype(int)
  
  plt.scatter(x_samp, y_samp, c=accept, cmap='RdYlGn')
  plt.text(.2, 1.75, f'Sample Size {str(size)}' + '\n' + f'Efficency: {accept.mean():.2f}')
  plt.xlim(0, 1)
  plt.ylim(0, 2)
  plt.show()

