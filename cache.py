'''
Created on 2012-9-7

@author: xuhong
'''
from functools import update_wrapper



def decorator(d):
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that caches the return value for each call 
    to f(args). Then when called again with same args, we can
    just look it up. """
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # Some element of args can't be a dict key (unhashable)
            return f(*args)
    return _f

@decorator
def countcalls(f):
    
    def _f(*args):
        callcounts[_f] += 1
        return f(*args)
    callcounts[_f] = 0
    return _f

callcounts = {}

@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print '%s--> %s' % (trace.level*indent, signature)
        trace.level += 1
        try:
            result = f(*args) #your code here
            print '%s<-- %s == %s' % ((trace.level-1)*indent, 
                                      signature, result)
        finally:
            trace.level -= 1# your code here
        return result # your code here
    trace.level = 0
    return _f

@trace
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)

def print_test(n):
    print "n\tfib(n)\tNo. of calls\tcall ratio"
    prevcalls = 1
    for i in range(n+1):
        @countcalls
        @memo
        def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)

        result, calls = fib(i), callcounts[fib]
        print "%d\t%d\t%-8d\t%f" % (i, result, calls, float(calls)/prevcalls)
        prevcalls = calls
        #callcounts[fib] = 0 #need to clear it before next call!
        
#print_test(15)
fib(5)

