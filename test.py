from string import Template

def main():
    cart=[];
    cart.append(dict(item='cocke',price=6.8,qylt=1))
    cart.append(dict(item='cacke',price=12.8,qylt=3))
    cart.append(dict(item='fish',price=23,qylt=4))
    t=Template('$item * $qylt = $price')
    total=0
    print('cart:')
    for data in cart:
        print(t.substitute(data))
        total +=data['price']
        print('total:' + str(total))
if __name__=='__main__':
    main()        



