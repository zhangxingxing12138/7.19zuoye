money_list=[]
def fun_checkout():
    print('开始计算----->')
        
    while True:
        money=float(input('输入商品金额(输入0表示输入完毕)：'))
        money_list.append(money)
        if money == 0:
            break
sum_money = 0.0
fun_checkout()
for count in money_list:
    sum_money+=count
print('合计金额：%.2f'%sum_money)
if sum_money>=500 and sum_money<1000:

    totle=sum_money*0.9
    print('应付金额：%.2f'%totle)
elif sum_money>=1000 and sum_money<2000:
    totle=sum_money*0.8
    print('应付金额：%.2f'%totle)
elif sum_money>=2000 and sum_money<3000:
    totle=sum_money*0.7
    print('应付金额：%.2f'%totle)
elif sum_money>=3000:
    totle=sum_money*0.6
    print('应付金额：%.2f'%totle)
        
    
