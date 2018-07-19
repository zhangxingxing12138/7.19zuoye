
name=str(input('姓名'))
weight=float(input('体重'))
height=float(input('%s的身高:'%name))   
def function_bim(name,height,weight):
   
    BMI=weight/(height*height)
    print('%s的BMI指数为%s'%(name,BMI))
    if BMI<18.5:
        print('您的体重过轻')
    elif 18.5<BMI<24.9:
        print('正常')
    elif 24.9<BMI<29.9:
        print('过重')
    elif BMI>29.9:
        print('肥胖')
function_bim(name,height,weight)
