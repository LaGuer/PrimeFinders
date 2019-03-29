# PrimeFinders

 [![Generic badge](https://img.shields.io/badge/github-primefinders-blue.svg)](https://github.com/LaGuer/primefinders) 
 [![PyPI version](https://badge.fury.io/py/primefinders.svg)](https://badge.fury.io/py/primefinders) 
 [![Build Status](https://travis-ci.org/LaGuer/primefinders.svg?branch=master)](https://travis-ci.org/LaGuer/primefinders) 
 [![codecov](https://codecov.io/gh/LaGuer/primefinders/branch/master/graph/badge.svg)](https://codecov.io/gh/LaGuer/primefinders) 
 [![Codacy Badge](https://api.codacy.com/project/badge/Grade/)](https://www.codacy.com/app/LaGuer/primefinders?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LaGuer/primefinders&amp;utm_campaign=Badge_Grade)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LaGuer/PrimeFinders/master)

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/laguer/PrimeFinders/blob/master/PrimeFinders.ipynb)

[![nbviewer](https://img.shields.io/badge/view%20on-nbviewer-brightgreen.svg)](https://nbviewer.jupyter.org/github/LaGuer/PrimeFinders/blob/master/PrimeFinders.ipynb)


## Installation

To install the package use pip:

    pip install primefinders


## Introduction

Some algorithm on prime numbers. You can find all the functions in the file `primefinders/`

In this release the Algorithm uses : 

- Fermat's test (based on Fermat's theorem)

Future Algorithms will use :

- Eratosthenes sieve based
- Prime generating functions
- Miller-Rabin primality test
- Euler's phi(n) i.e., the number of integers less than n which have no common factor with n
- LCG


## Specifications

- Language: Python **3.6** (also works on 3.5 and 3.7)
- Package:
	- Basic python packages were preferred
	- Matplotlib v2.0 - graph and math

### Integration and pipeline

Code quality is monitored through [codacity](https://www.codacy.com/app/LaGuer/primefinders/dashboard).
For the tests coverage, there's [codecov](https://codecov.io/gh/LaGuer/primefinders) which is run during the [Travis CI](https://travis-ci.org/LaGuer/primefinders) pipeline.

## Math

Here are a bit of information to help understand some of the algorithms

### Congruence

 "`≡`" means congruent, `a ≡ b (mod m)` implies that 
`m / (a-b), ∃ k ∈ Z` that verifies `a = kn + b`
   
 which implies:

    a ≡ 0 (mod n) <-> a = kn <-> "a" is divisible by "n" 
    
See [Modular_arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic)
    
### Strong Pseudoprime

A strong [pseudoprime](http://mathworld.wolfram.com/StrongPseudoprime.html) to a base `a` is an odd composite number `n` 
with `n-1 = d·2^s` (for d odd) for which either `a^d = 1(mod n)` or `a^(d·2^r) = -1(mod n)` for some `r = 0, 1, ..., s-1` </br>


### Fermat's Theorem

#### How to use

A Probabilistic algorithm taking `t` randoms numbers `a` and testing the Fermat's theorem on number `n > 1`
Prime probability is right is `1 - 1/(2^t)`
Returns a boolean: True if `n` passes the tests.

```python
With (n)

from primefinders import primefinders

primefinders.about()

primefinders.calculate(1697)

# With n the number you want to test
fermat(n)
primefinders.fermat(1697)
```

#### Theory

If `n` is prime then `∀ a ∈[1, ..., n-1]`

```
    a^(n-1) ≡ 1 (mod n) ⇔ a^(n-1) = kn + 1
```
### Lucas-Lehmer

#### How to use

Implementation of the sieve of erathostenes that discover the primes and their composite up to a limit.
It returns a dictionary:
  - the key are the primes up to n
  - the value is the list of composites of these primes up to n

```python
from primefinders import toolkit
>>>

from primefinders import lucas_lehmer

# With as a parameter the upper limit
lucas_lehmer(10)
>>> 
```

### Sieve of Eratosthenes

#### How to use

Implementation of the sieve of erathostenes that discover the primes and their composite up to a limit.
It returns a dictionary:
  - the key are the primes up to n
  - the value is the list of composites of these primes up to n

```python

from primefinders import sieve_eratosthenes

# With as a parameter the upper limit
sieve_eratosthenes(10)
>> {2: [4, 6, 8], 3: [6, 9], 5: [], 7: []}
```

#### Theory

This sieve mark as composite the multiple of each primes. It is an efficient way to find primes.
For `n ∈ N` with `n > 2` and for `∀ a ∈[2, ..., √n]` then `n/a ∉ N` is true.

[![Erathostene example](https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif)](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)



