import struct

fn = input ('imput you file:')
fn = repr(fn)[1:-1]
f = open(fn, mode='rb')
s = f.read(30)
print s

st = struct.unpack('>ccIIIIIIHH', s)
print st