def lcg(modulus, a, c, seed):
  while True:
    seed = (a * seed + c) % modulus
    yield seed
