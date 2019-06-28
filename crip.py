def crip(senha):
    k = ''
    for i in senha:
        print(i)
        k += chr(ord(i) + 10)
        senha = k
    return senha



m = 'abcd'
print(m)
crip(m)
print(m)
