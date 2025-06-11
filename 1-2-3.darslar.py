#ism='qayum'
#familya='xudayarov'
#yangi=f"Salom\nmening ismim {ism}.  Familyam {familya}!"
#print(yangi)
#ism=input("ismingiz:")
#sharif="bond"
#ism_sharf=f"{ism} {sharif}"
#ism_sharf=ism_sharf.upper()
#print(ism_sharf.capitalize())
#salom="      olmani   "
#print("Men mevalardan"+salom.strip()+"yaxshi ko'raman")

#ism='Dostonbek'
#print("salom",ism.upper())
#print("Salom",ism.lower())
#print("Salom",ism.title())
#print("salom",ism.capitalize())
#meva='   olma   '
#print("Yaxshi",meva)
#print("\"nexsia\",\"tico\",'damas'  ko'rganlar qilaq xavas")
#print("22 ni 4 ga bo'lganda natija:",22%4)
#yuzi=125*125
#per=4*125
#print("tomonlari 125 ga teng kvadratning yuzi",yuzi,"perimetri:",per , "ga teng!")
#print("diametri 12 ga teng doirani yuzi:",12/2**2*3.14)
#print("katetlari 6 va 7 bo'lgan uchburchak  yuzi=",(6**2+7**2)/2)
# fructs=["aplle",'orange','melon','greep']
# narxi=[12000,20000,30000,40000]
# # ismlar=[]#bo'sh ro'yxat
# print(fructs[0].upper())
# cars=['nexi1','nexia2']
# cars.append('malibu')
# del cars[0]
# print(cars)
# cars.insert(1,'lacetti')
# print(cars)

# del cars[0]
# print(cars)
# cars.remove('malibu')
# print(cars)
# bozorlik=['olma','banan','gul','ananas']
# mahsulot=bozorlik.pop(2)#indeksni  sug'uriboladi
# print(bozorlik)
# print("olingan maxsulotlar",mahsulot)

# mahsulot2=bozorlik.pop(1)
# print(mahsulot2)
# # pop()#orasidan sug'uriboladi
# narxi[0]=narxi[0]+5000
# print(narxi)
# print(narxi.index(30000))
# son=int(input("istalgan sonni  kiriting:"))#floatdan  foydalansa ham bo'ladi
# kvadrati=int(son**2)
# kubi=int(son**3)
# print(kvadrati,kubi,sep='\n')#   sep=separator xar bir o'zgaruvchni yangi qatorda yozadi
# yosh=int(input("yoshingizni kiriting:"))
# t_yil=2025-yosh
# print("tugilgan yilingiz",t_yil,"- yil ekan!")


# son1=float(input("1-sonni kiriting:"))
# son2=float(input("2-sonni kiriting:"))
# print(f"{son1}+{son2}=",int(son1+son2))
# print(f"{son1}-{son2}=",int(son1-son2))
# print(f"{son1}*{son2}=",int(son1*son2))
# print(f"{son1}/{son2}=",int(son1/son2))


               #list,.sort(),sorted(),.reverse(),len()
# davlat=['qozoq','kirgiz','tojik','turk'] #[] bu  list    
# print(len(davlat)  )        #len(o'zgaruvchi) elementlar soni
# davlat.sort()               #.sort() alfabet bo'yicha tartiblidi

# print(sorted(davlat,reverse=True))   #reverse=True teskari sartirofka
# davlat.reverse()     #listni  teskari  qilisg uchun
# print(davlat)
                        # list(),renge()    
# sonlar=list(range(0,21))  #range bu belgilangan sonlar oralig'idagi barchasini oladi
# print(sonlar)
                      #min(),max(),sum()
# narxlar=[10000,20000,40000,150000]      
# arzon=min(narxlar)               
# qimmat=max(narxlar)
# xammasi=sum(narxlar)
# print("arzoni:",arzon,"qimmati",qimmat,"xammasi:",xammasi)

                 #ro'yxat kesish
# cars=['koblt','nexia','matiz','damas']
# print(cars[0:3])
# print(cars[:3])        #o'zi noldan deb oladi        
                 #ro'yxatdan nusxa  olish
# sonlar=[1,2,3,4,5,66,77,85,90]                 
# yangi=sonlar[:]
# yangi.append(150)
# print(yangi)
# print(sonlar)
                   #TUPLES  a=() bo'lsa o'zgarmas bo'lar ekan
# toys=('ayiq','maymun','panda','ot','it')           
# toys=list(toys)  
# type(toys)              
# toys.append('loshad')
# print(toys)
# toys=tuple(toys)
# type(toys)
                     #vazifalar
# sonlar=list(range(120,1201,2))   
# a=max(sonlar)
# b=min(sonlar)
# print(a-b)
# bosh=sonlar[0:20]
# oxir=sonlar[-20:]
# ortasi=sonlar[270:320]
# print(bosh,oxir,ortasi,sep=('\n'))


# royxat=['manti','osh',"sho'rva",'lagmon']
# nonushta=royxat[:]
# nonushta.append('shakar')
# nonushta.append('novvot')
# nonushta.remove('manti')
# nonushta.remove('lagmon')
# nonunshta=tuple(nonushta)
# nonushta[0]="meva"
# print(nonunshta)

                     #for mehmon in mehmonlar  uchun  ishlimiz
# mehmonlar=['ali','vali','tesha','ketmon','bolta']   
# for mehmon in mehmonlar:
#        print(f'Salom aziz {mehmon},xush kelibsiz') 
#        print(f"xayr {mehmon},xush kelibsiz")         
                      #for siklini  sonlar ustida  ishlatamiz
# sonlar=list(range(1,15))  
# for son in sonlar:
#      print(f'{son} ning  kvadrati  {son**2}  ga  teng') 

                      #for  siklini sonlar  bilan  islash
# sonlar=list(range(10))
# kal=[]
# for son in sonlar:
#     kal.append(son**2)
# print(kal)    
                        
                        #for sikli  uchun input  bilan  ishlimiz
# doslar=[]                        
# print("5ta eng  yaqin  do'stingiz kim")                        
# for n in range(5):
#     doslar.append(input(f"{n+1}- do'stingizning  ismini  kiriting: "))
# print(doslar)    



























