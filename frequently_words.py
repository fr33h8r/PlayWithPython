from urllib2 import urlopen

def main():
  html = urlopen('http://python.org')
  words = {}

  for line in html:
    line = line.strip(' \n')
    for word in line.split(' '):
      try:
        words[word] += 1
      except KeyError:
        words[word] = 1

  pairs = words.items()
  pairs.sort(key = lambda x: x[1], reverse=True)

  for pair in pairs[:10]:
    print pair[0], pair[1]

  return

if __name__ == '__main__':
  main()