#if-else determine statements
#jude wheater u can buy wine or not
age=input("pls input your age:")
#强制转换变量类型
age_nmu=int(age)
if age_nmu >=20:
    print("you can buy wine at LCBO at%d"%age_nmu)
else:
    print("you canot buy wine at LCBO at age%d"%age_nmu)