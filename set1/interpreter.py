def main():
    k = cont(input('Expression: '))
    if type(k) == 'float':
        print(f'{k:.1f}') 
    else: print(k)

def cont(st):
    st = st.split(' ')
    if st[1] == '+': return float(st[0]) + float(st[2])
    elif st[1] == '-': return float(st[0]) - float(st[2])
    elif st[1] == '*': return float(st[0]) * float(st[2])
    elif st[1] == '/' and st[2]!='0': return float(st[0]) / float(st[2])
    else: return 'not correct operation or division by zero'

main()