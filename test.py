from string import Template
class myTemplate(Template):
       delimiter='#'
def main():
    cart=[];
    cart.append(dict(item='Cocke',price=6.8,qylt=1))
    cart.append(dict(item='Cack',price=12.8,qylt=3))
    cart.append(dict(item='Fish',price=23,qylt=4))
    t=myTemplate('#item X #qylt = #price')
    total=0
    print('cart:')
    for data in cart:
        print(t.substitute(data))
        total +=data["price"]
    print('Total:' + str(total))
if __name__=='__main__':
    main()        


b = bytes('pythön', encoding='utf-8')

print(str(b, encoding='ascii', errors='ignore'))


