#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import *
import sys

if len(sys.argv) != 3:
  print("Syntax : draw.py <filename> <number>")
  exit(0)
filename = sys.argv[1]
try:
  f = open(filename)
  addresses = f.readlines()
  addresses = [ a.strip('\n') for a in addresses ]
  f.close()
except IOError:
  print('File not found')
  exit(0)

nb_winner = int(sys.argv[2])
total_mails = len(addresses)
print('Total number of emails: ',total_mails)
winners = []
print("The winner is :")
while len(winners) < nb_winner:
  n = randint(0,total_mails-1)
  if addresses[n] not in winners:
    if 'orange.com' in addresses[n] or 'orangecyberdefense.com' in addresses[n] or 'sofrecom.com' in addresses[n]:
      winners.append(addresses[n])
      print(n,addresses[n])