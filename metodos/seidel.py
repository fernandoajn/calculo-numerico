import math

print("Metodo de Gauss Seidel")

def coluna(m, c):
  return [m[i][c] for i in range(len(m))]
 
def linha(m, r):
  return m[r][:]
  
def altura(m):
  return len(m)
  
def largura(m):
  return len(m[0])

def gauss_seidel(m, x0=None, eps=1e-5, max_iteration=100):
  n  = altura(m)
  x0 = [0] * n if x0 == None else x0
  x1 = x0[:]

  for __ in range(max_iteration):
    for i in range(n):
      s = sum(-m[i][j] * x1[j] for j in range(n) if i != j) 
      x1[i] = (m[i][n] + s) / m[i][i]
    if all(abs(x1[i]-x0[i]) < eps for i in range(n)):
      return x1 
    x0 = x1[:]    
  raise ValueError('Solucao nao converge!')

if __name__ == '__main__':
  # matriz fixa, so altera com hard code
  m = [[4,3.2,0.5,9.2], [2.2,3,-0.3,0.9], [-3.1,-0.2,4,7]]
  print(gauss_seidel(m))