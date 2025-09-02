# Для систем счисления <=10
def cc(x):
    s=''
    while x>0:
        s=str(x%3) + s
        x=x//3
    return s

