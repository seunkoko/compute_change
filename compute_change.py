
"""
-------------------
1 penny = 1 penny |
-------------------
1 nickel = 5 pennies
1 dime = 10 pennies
1 quarter = 25 pennies
1 dollar = 100 pennies
5 dollars = 500 pennies
10 dollars = 1000 pennies
20 dollars = 2000 pennies

Compute change for $34.36
**convert in terms of pennies 3436
  3436/2000 = 1 
  3436%2000 = 1436

  1436/1000 = 1
  1436%1000 = 436

  436/500 = 0
  436%500 = 436

  436/100 = 4
  436%100 = 36

  36/25 = 1
  36%25 = 11

  11/10 = 1
  11%10 = 1

  1/5 = 0
  1%5 = 1

  1/1 = 1
  1%1 = 0
"""

def compute_change(change):
  dict = {2000: "twenties", 1000: "tens", 500: "fives", 100: "ones", 25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}
  change_convert = change*100
  #print "converted change: %d" % change_convert 

  for key in reversed(sorted(dict)):
    #print "change_convert: %f and %s" % (change_convert, key)
    print str(int(compute_value(change_convert, key))) + " " + dict[key]
    change_convert = compute_remainder(change_convert, key) 

def compute_remainder(val, mod):
  #print (val%mod)
  return (val%mod)

def compute_value(val, div):
  #print (val/div)
  return (val/div)


print compute_change(34.36)