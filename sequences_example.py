__author__ = 'Pavel'

def main():
  l = range(0, 10)
  print l[0:2]
  print l[1:-2]
  print l[1::2]
  print l[::-1]
  return

if __name__ == '__main__':
  main()