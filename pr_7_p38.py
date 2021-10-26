s=str(input('dati sirul de caractere '))
print('sirul initial',s)
a=s.count('A')
b=s.replace("A",'*')
c=s.replace('B','')
d=s.count('MA')
e=s.replace('MA','TA')
f=s.replace('TO','')
g=s[::-1]
print('nr de aparitii ale caracterului A in sirul s ',a)
print('sirul obtinut prin substituirea caracterului A prin caracterul* ',b)
print('sirul obtinut prin radierea din sirul s a tuturor aparitiilor caracterului B ',c)
print('nr de aparitii ale silabei MA in sirul s ',d)
print('sirul obtinut prin substituirea silabei MA prin silaba TA ',e)
print('sirul obtinut prin radierea din sirul s a tuturor aparitiilor silabei TO ',f)
print('scrierea iversa a sirului s ',g)
# daca e gresit ceva, cer scuze, eu cred ca iar nu am inteles, dar credeam ca lucra

