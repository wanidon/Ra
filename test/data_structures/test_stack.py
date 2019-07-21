from z3 import *
from data_structures import Stack
gpdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(gpdir)

s = Stack()
t = BitVecVal(100+ 2**1024-1,256)
print(t)
s.push(t)
print(s.pop())
print(s.pop())
s.push(BitVecVal(1,256))
s.push(BitVecVal(2,256))
s.push(BitVec("hoge", 256))
s.push(BitVecVal(4,256))
s.swapx(1)
s.dupx(1)
s.dupx(5)
s.swapx(4)
s.show_data()
print()
s2 = s.duplicate(1)
s3 = s.duplicate(2)
s4 = s.duplicate(3)
s.show_data()
print()

s2.show_data()
print()

s3.swapx(4)
s3.show_data()
print()
s3.swapx(1)
s3.show_data()

s3.swapx(6)
s3.show_data()

print()
s4.show_data()
print()
s4.dupx(1)
s4.show_data()
print()

s4.dupx(10)
s4.show_data()
sym1 = s4.pop()
s4.pop()
s4.pop()
s4.pop()
s4.pop()
s4.pop()
s4.pop()
s4.pop()
s4.pop()
s4.pop()
sym2 = s4.pop()
print()
s.show_data()
print(sym1,sym2,simplify(sym1==sym2))
s.push(7) # this cause error