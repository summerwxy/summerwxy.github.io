#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import glob
import datetime

def main():
  fns = glob.glob('./_posts/*.*')
  tags = [] # tag prepare
  for fn in fns:
    mfloat = None
    with open(fn, 'rt', encoding="utf-8") as f:
      ctime = datetime.datetime.fromtimestamp(os.path.getctime(fn))
      mfloat = os.path.getmtime(fn)
      mtime = datetime.datetime.fromtimestamp(mfloat)
      newlines = []
      for line in f.readlines():
        if line.startswith("created:"):
          newlines.append("created: " + str(ctime)[0:19] + " +08:00\n")
        elif line.startswith("modified:"):
          newlines.append("modified: " + str(mtime)[0:19] + " +08:00\n")
        else:
          newlines.append(line)
        # tags prepare
        if line.startswith("tags"):
          result = re.match(r'.*\[(.*)\]', line)
          if (result):
            for word in [w.strip() for w in result.group(1).split(',')]:
              if not word in tags:
                tags.append(word)

    with open(fn, 'wt', encoding="utf-8") as f:
      for line in newlines:
        f.write(line)    

    os.utime(fn, (mfloat, mfloat))

  # auto generate tags file.
  for tag in tags:
    fn = "./tags/" + tag + ".html"
    if not os.path.isfile(fn):
      with open(fn, 'wt', encoding="utf-8") as f:
        f.write('---\n')
        f.write('layout: tag\n')
        f.write('tag: ' + tag + '\n')
        f.write('---\n')

  print(">>>>> created date, modified date, tag files okay!! <<<<<")

if __name__ == '__main__':
  main()

