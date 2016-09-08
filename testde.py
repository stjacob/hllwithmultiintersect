from treeset import TreeSet
import numpy
from hllcounter import HllCounter
import pickle

hcpk=open('hc.pk','rb')
hc1pk=open('hc1.pk','rb')
hc=pickle.load(hcpk)
hc1=pickle.load(hc1pk)
print hc.size()
print hc1.size()
hcarray=[hc,hc1]
print "first:",HllCounter.intersect(hcarray)
print "second:",HllCounter.intersect(hcarray)
