#!/usr/bin/python3
#
# If you need to test out IR signals, you can use a script like this to
# generate the signals for lircd.conf. Try to find a semi-working remote
# config first (http://lirc.sourceforge.net/remotes/), look for patterns
# and test similar signals.

hexnums = range(0,16)
index = 1
for a in hexnums:
    for b in hexnums:
        for c in hexnums:
            for d in [1,2,3,5,7]:
                ahex = hex(a)[2:]
                bhex = hex(b)[2:]
                chex = hex(c)[2:]
                dhex = hex(d)[2:]
                print("          TEST_{index}                  0x{a}{b}{c}{d}".format(index=index, a=ahex, b=bhex, c=chex, d=dhex))
                index +=1

