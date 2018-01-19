from point import PointOfEC, search_order
from sign import SignatureGenerator
from verify import SignatureVerificator

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if i * i > n:
                break
            elif n % i == 0:
                return False
        return True


def search_base_point(p, a, b):
    """
    the function return maximum prime order.
    """
    lam = -1
    neu = -1
    max_order = -1
    for x in xrange(p):
        for y in xrange(p):
            if (y * y) % p == ((x ** 3) + (a * x) + b) % p:
                point = PointOfEC(p, a, b, x, y)
                point.order = search_order(point)
                print 'NOT prime order..., Search Next Point'
                if is_prime(point.order):
                    if max_order < point.order:
                        print 'Prime order is found!'
                        print 'order : ', point.order
                        print 'x : ', x
                        print 'y : ', y
                        lam = x
                        neu = y
                        max_order = point.order
    
    assert lam > -1 and neu > -1 and max_order > -1, "ERROR : Search is Failed"
    return lam, neu


def calculate_cofactor(p, a, b, order):
    z = 0
    for x in xrange(p):
        for y in xrange(p):
            if (y * y) % p == ((x ** 3) + (a * x) + b) % p:
                z += 1
    print z
    print 'cofactor: ', z / order

def main():
    p = 9999991
    a = -3
    b = 10
    m = "Hallo, Alice! I'm Shota!"
    x, y = search_base_point(p, a, b)
    
    point = PointOfEC(p, a, b, x, y)
    point.order = search_order(point)
    calculate_cofactor(p,a,b,point.order)
    
    sg = SignatureGenerator(point, m)
    pk = sg.get_public_key()
    print 'Q :', pk
    
    r, s = sg.get_signature()
   
    sv = SignatureVerificator(point, m)
    sv.verify_message(r, s, pk)


if __name__ == '__main__':
    main()