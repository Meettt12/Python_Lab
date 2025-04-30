def que():
    pri={"Shampoo":120,"Soap":20,"Rice":120}
    qua={"Shampoo":1,"Soap":2,"Rice":10}
    total=0
    for key in price.keys():
        total=total+pri[key]*qua[key]
    print(total)

que()
