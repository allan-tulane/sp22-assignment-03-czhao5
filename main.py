# assignment-03

# no other imports needed
from collections import defaultdict
import math

### PARENTHESES MATCHING

#### Iterative solution
def parens_match_iterative(mylist):

  if (iterate(parens_update, 0, mylist) == 0):
    return True
  else:
    return False
    pass


def parens_update(current_output, next_input):
  
  if (next_input == "("):
    current_output = current_output + 1
  if (current_output < 1 and next_input == ")"):
    current_output = -100
  if (next_input == ")"):
    current_output = current_output - 1
  return current_output

  
    
def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])
      
def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False


#### Scan solution
def parens_match_scan(mylist):
    funct = (lambda x:paren_map(x))
    for i in list(map(funct, mylist)):
        if i == -1:
            return False
        if i == 1:
            break
    reduce(min_f, 0,(scan(plus, 0, list(map(funct, mylist)))[0]))
    if reduce(min_f, 0,(scan(plus, 0, list(map(funct, mylist)))[0])) !=0:
        return False
    elif reduce(min_f, 0,(scan(plus, 0, list(map(funct, mylist)))[0])) == 0:
        return True
    else:
      return True
    pass
  
def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )
      
def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res
      
def paren_map(x):
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0
def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False

#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    if len(mylist) == 1 and mylist[0] == ")":
        return (1, 0)
    elif len(mylist) == 1 and mylist[0] == "(":
        return (0, 1)
    elif len(mylist) == 0 or len(mylist) == 1:
        return (0, 0)
    else: 
        (RR, RL) = parens_match_dc_helper(mylist[len(mylist)//2:])
        (LR, LL) = parens_match_dc_helper(mylist[:len(mylist)//2])
        if LL == 0 and RR == 0 and LR > 0 and RL > 0:
          return (LR, RL)
        return ( RR - LL, RL - LR)
    pass
  
def test_parens_match_dc():
  assert parens_match_dc(['(', ')']) == True
  assert parens_match_dc(['(']) == False
  assert parens_match_dc([')']) == False
  
def plus(x,y):
  return x + y