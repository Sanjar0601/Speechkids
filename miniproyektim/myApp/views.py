from django.shortcuts import render

from .models import Harflar
id = 0
def home(request):
   
    context={}
    return render(request,"myApp/index.html",context)
def extra(request):
    harflar = Harflar.objects.all()
    context={'harflar': harflar}
    return render(request,"myApp/extra.html",context)
def unver(request):
    harflar = Harflar.objects.all()
    context={'harflar': harflar}
    return render(request,"myApp/unversal.html",context)
def qoshim(request,pk):
    harflar = Harflar.objects.get(id=pk)
    context={}
    context={'harflar': harflar}
    context['jura'] = id
    return render(request,"myApp/qoshim.html",context)
def error1(request):
    context={}
    return render(request,"myApp/error-404.html",context)
def about1(request):
    context={}
    return render(request,"myApp/about-1.html",context)
def mashq1(request):
    context={}
    return render(request,"myApp/mashq.html",context)
def contact1(request):
    context={}
    return render(request,"myApp/contact-1.html",context)
def login1(request):
    context={}
    return render(request,"myApp/login.html",context)
def dharf(request):
    c = 'D'
    a = ['dangasa', 'dazmol', 'dunyo', 'dasturxon', 'dala','dengiz']
    b = []
    context={}
    context['jb'] = c
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/D/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)

def dharf0(request):
    c = 'D'
    a = 'dangasa'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/D5"
    context['javob4'] = "/D1"
            
    return render(request,"myApp/bayroq.html",context)
def dharf1(request):
    c = 'D'
    a = 'dazmol'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/D0"
    context['javob4'] = "/D2"
       
    return render(request,"myApp/bayroq.html",context)
def dharf2(request):
    c = 'D'
    a = 'dunyo'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/D1"
    context['javob4'] = "/D3"
       
    return render(request,"myApp/bayroq.html",context)
def dharf3(request):
    c = 'D'
    a = 'dasturxon'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/D2"
    context['javob4'] = "/D4"
       
    return render(request,"myApp/bayroq.html",context)
def dharf4(request):
    c = 'D'
    a = 'dala'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/D3"
    context['javob4'] = "/D5"
       
    return render(request,"myApp/bayroq.html",context)
def dharf5(request):
    c = 'D'
    a = 'dengiz'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/D4"
    context['javob4'] = "/D0"
       
    return render(request,"myApp/bayroq.html",context)
def eharf(request):
    c = 'E'
    a = ['echki', 'everest', 'ehson', 'ertak', 'erka','eshak']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def eharf0(request):
    c = 'E'
    a = 'echki'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/E5"
    context['javob4'] = "/E1"
    
    return render(request,"myApp/bayroq.html",context)
def eharf1(request):
    c = 'E'
    a = 'everest'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/E0"
    context['javob4'] = "/E2"
       
    return render(request,"myApp/bayroq.html",context)
def eharf2(request):
    c = 'E'
    a = 'ehson'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/E1"
    context['javob4'] = "/E3"
       
    return render(request,"myApp/bayroq.html",context)
def eharf3(request):
    c = 'E'
    a = 'ertak'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/E2"
    context['javob4'] = "/E4"
       
    return render(request,"myApp/bayroq.html",context)
def eharf4(request):
    c = 'E'
    a = 'erka'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/E3"
    context['javob4'] = "/E5"
       
    return render(request,"myApp/bayroq.html",context)
def eharf5(request):
    c = 'E'
    a = 'eshak'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/E4"
    context['javob4'] = "/E0"
       
    return render(request,"myApp/bayroq.html",context)

#######################################################F
def fharf(request):
    c = 'F'
    a = ['fursat', 'forum', 'faqat', 'fonus', 'farishta','foyda']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def fharf0(request):
    c = 'F'
    a = 'fursat'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/F5"
    context['javob4'] = "/F1"
       
    return render(request,"myApp/bayroq.html",context)
def fharf1(request):
    c = 'F'
    a = 'forum'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/F0"
    context['javob4'] = "/F2"
       
    return render(request,"myApp/bayroq.html",context)
def fharf2(request):
    c = 'F'
    a = 'faqat'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/F1"
    context['javob4'] = "/F3"
       
    return render(request,"myApp/bayroq.html",context)
def fharf3(request):
    c = 'F'
    a = 'fonus'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/F2"
    context['javob4'] = "/F4"
       
    return render(request,"myApp/bayroq.html",context)
def fharf4(request):
    c = 'F'
    a = 'farishta'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/F3"
    context['javob4'] = "/F5"
       
    return render(request,"myApp/bayroq.html",context)
def fharf5(request):
    c = 'F'
    a = 'foyda'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/F4"
    context['javob4'] = "/F0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################G
def gharf(request):
    c = 'G'
    a = ['gul', 'gavhar', 'gap', 'guruch', 'gerb' ,'garaj']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def gharf0(request):
    c = 'G'
    a = 'gul'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/G5"
    context['javob4'] = "/G1"
       
    return render(request,"myApp/bayroq.html",context)
def gharf1(request):
    c = 'G'
    a = 'gavhar'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/G0"
    context['javob4'] = "/G2"
       
    return render(request,"myApp/bayroq.html",context)
def gharf2(request):
    c = 'G'
    a = 'gap'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/G1"
    context['javob4'] = "/G3"
       
    return render(request,"myApp/bayroq.html",context)
def gharf3(request):
    c = 'G'
    a = 'guruch'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/G2"
    context['javob4'] = "/G4"
       
    return render(request,"myApp/bayroq.html",context)
def gharf4(request):
    c = 'G'
    a = 'gerb'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/G3"
    context['javob4'] = "/G5"
       
    return render(request,"myApp/bayroq.html",context)
def gharf5(request):
    c = 'G'
    a = 'garaj'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/G4"
    context['javob4'] = "/G0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################H
def hharf(request):
    c = 'H'
    a = ['hayot', 'hisob', 'hissiyot', 'hovuz', 'hasis', 'halol']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def hharf0(request):
    c = 'H'
    a = 'hayot'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/H5"
    context['javob4'] = "/H1"
       
    return render(request,"myApp/bayroq.html",context)
def hharf1(request):
    c = 'H'
    a = 'hisob'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/H0"
    context['javob4'] = "/H2"
       
    return render(request,"myApp/bayroq.html",context)
def hharf2(request):
    c = 'H'
    a = 'hissiyot'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/H1"
    context['javob4'] = "/H3"
       
    return render(request,"myApp/bayroq.html",context)
def hharf3(request):
    c = 'H'
    a = 'hovuz'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/H2"
    context['javob4'] = "/H4"
       
    return render(request,"myApp/bayroq.html",context)
def hharf4(request):
    c = 'H'
    a = 'hasis'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/H3"
    context['javob4'] = "/H5"
       
    return render(request,"myApp/bayroq.html",context)
def hharf5(request):
    c = 'H'
    a = 'halol'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/H4"
    context['javob4'] = "/H0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################i
def iharf(request):
    c = 'I'
    a = ['ilon', 'istiqlol', 'ilhom', 'igna', 'iroda', 'ish']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def iharf0(request):
    c = 'I'
    a = 'ilon'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/I5"
    context['javob4'] = "/I1"
       
    return render(request,"myApp/bayroq.html",context)
def iharf1(request):
    c = 'I'
    a = 'istiqlol' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/I0"
    context['javob4'] = "/I2"
       
    return render(request,"myApp/bayroq.html",context)
def iharf2(request):
    c = 'I'
    a = 'ilhom' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/I1"
    context['javob4'] = "/I3"
       
    return render(request,"myApp/bayroq.html",context)
def iharf3(request):
    c = 'I'
    a = 'igna'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/I2"
    context['javob4'] = "/I4"
       
    return render(request,"myApp/bayroq.html",context)
def iharf4(request):
    c = 'I'
    a =  'iroda'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/I3"
    context['javob4'] = "/I5"
       
    return render(request,"myApp/bayroq.html",context)
def iharf5(request):
    c = 'I'
    a =  'ish'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/I4"
    context['javob4'] = "/I0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################j
def jharf(request):
    c = 'J'
    a = ['jasur', 'javohir', 'juft', 'jumla', 'jamila', 'juda']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def jharf0(request):
    c = 'J'
    a = 'jasur' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/J5"
    context['javob4'] = "/J1"
       
    return render(request,"myApp/bayroq.html",context)
def jharf1(request):
    c = 'J'
    a = 'javohir'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/J0"
    context['javob4'] = "/J2"
       
    return render(request,"myApp/bayroq.html",context)
def jharf2(request):
    c = 'J'
    a =  'juft'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/J1"
    context['javob4'] = "/J3"
       
    return render(request,"myApp/bayroq.html",context)
def jharf3(request):
    c = 'J'
    a =  'jumla' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/J2"
    context['javob4'] = "/J4"
       
    return render(request,"myApp/bayroq.html",context)
def jharf4(request):
    c = 'J'
    a = 'jamila'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/J3"
    context['javob4'] = "/J5"
       
    return render(request,"myApp/bayroq.html",context)
def jharf5(request):
    c = 'J'
    a =  'juda'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/J4"
    context['javob4'] = "/J0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################k
def kharf(request):
    c = 'K'
    a = ['kam', 'kampot', 'kampir', 'kilo', 'kino', 'kim']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def kharf0(request):
    c = 'K'
    a = 'kam' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/K5"
    context['javob4'] = "/K1"
       
    return render(request,"myApp/bayroq.html",context)
def kharf1(request):
    c = 'K'
    a = 'kampot' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/K0"
    context['javob4'] = "/K2"
       
    return render(request,"myApp/bayroq.html",context)
def kharf2(request):
    c = 'K'
    a = 'kampir' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/K1"
    context['javob4'] = "/K3"
       
    return render(request,"myApp/bayroq.html",context)
def kharf3(request):
    c = 'K'
    a = 'kilo' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/K2"
    context['javob4'] = "/K4"
       
    return render(request,"myApp/bayroq.html",context)
def kharf4(request):
    c = 'K'
    a = 'kino' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/K3"
    context['javob4'] = "/K5"
       
    return render(request,"myApp/bayroq.html",context)
def kharf5(request):
    c = 'K'
    a = 'kim'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/K4"
    context['javob4'] = "/K0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################l
def lharf(request):
    c = 'L'
    a = ['laylak', 'lola', 'lekin', 'lahza', 'lol', 'lotin']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def lharf0(request):
    c = 'L'
    a = 'laylak' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/L5"
    context['javob4'] = "/L1"
       
    return render(request,"myApp/bayroq.html",context)
def lharf1(request):
    c = 'L'
    a = 'lola' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/L0"
    context['javob4'] = "/L2"
       
    return render(request,"myApp/bayroq.html",context)
def lharf2(request):
    c = 'L'
    a = 'lekin' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/L1"
    context['javob4'] = "/L3"
       
    return render(request,"myApp/bayroq.html",context)
def lharf3(request):
    c = 'L'
    a = 'lahza' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/L2"
    context['javob4'] = "/L4"
       
    return render(request,"myApp/bayroq.html",context)
def lharf4(request):
    c = 'L'
    a = 'lol' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/L3"
    context['javob4'] = "/L5"
       
    return render(request,"myApp/bayroq.html",context)
def lharf5(request):
    c = 'L'
    a = 'lotin'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/L4"
    context['javob4'] = "/L0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################m
def mharf(request):
    c = 'M'
    a = ['mashina', 'mumkin', 'masala', 'muhokama', 'maymun', 'mushuk']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def mharf0(request):
    c = 'M'
    a = 'mashina' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/M5"
    context['javob4'] = "/M1"
       
    return render(request,"myApp/bayroq.html",context)
def mharf1(request):
    c = 'M'
    a = 'mumkin' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/M0"
    context['javob4'] = "/M2"
       
    return render(request,"myApp/bayroq.html",context)
def mharf2(request):
    c = 'M'
    a = 'masala' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/M1"
    context['javob4'] = "/M3"
       
    return render(request,"myApp/bayroq.html",context)
def mharf3(request):
    c = 'M'
    a = 'muhokama'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/M2"
    context['javob4'] = "/M4"
       
    return render(request,"myApp/bayroq.html",context)
def mharf4(request):
    c = 'M'
    a =  'maymun' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/M3"
    context['javob4'] = "/M5"
       
    return render(request,"myApp/bayroq.html",context)
def mharf5(request):
    c = 'M'
    a = 'mushuk'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/M4"
    context['javob4'] = "/M0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################N
def nharf(request):
    c = 'N'
    a = ['non', 'nam', 'nisbatan' ,'navbat','nur', 'nima']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def nharf0(request):
    c = 'N'
    a = 'non' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/N5"
    context['javob4'] = "/N1"
       
    return render(request,"myApp/bayroq.html",context)
def nharf1(request):
    c = 'N'
    a = 'nam' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/N0"
    context['javob4'] = "/N2"
       
    return render(request,"myApp/bayroq.html",context)
def nharf2(request):
    c = 'N'
    a = 'nisbatan' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/N1"
    context['javob4'] = "/N3"
       
    return render(request,"myApp/bayroq.html",context)
def nharf3(request):
    c = 'N'
    a = 'navbat'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/N2"
    context['javob4'] = "/N4"
       
    return render(request,"myApp/bayroq.html",context)
def nharf4(request):
    c = 'N'
    a = 'nur' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/N3"
    context['javob4'] = "/N5"
       
    return render(request,"myApp/bayroq.html",context)
def nharf5(request):
    c = 'N'
    a = 'nima'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/N4"
    context['javob4'] = "/N0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################o
def oharf(request):
    c = 'O'
    a = ['olim', 'ota', 'ohak', 'orom', 'oyoq', 'oymoma']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def oharf0(request):
    c = 'O'
    a = 'olim' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/O5"
    context['javob4'] = "/O1"
       
    return render(request,"myApp/bayroq.html",context)
def oharf1(request):
    c = 'O'
    a = 'ota' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/O0"
    context['javob4'] = "/O2"
       
    return render(request,"myApp/bayroq.html",context)
def oharf2(request):
    c = 'O'
    a = 'ohak'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/O1"
    context['javob4'] = "/O3"
       
    return render(request,"myApp/bayroq.html",context)
def oharf3(request):
    c = 'O'
    a =  'orom' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/O2"
    context['javob4'] = "/O4"
       
    return render(request,"myApp/bayroq.html",context)
def oharf4(request):
    c = 'O'
    a = 'oyoq'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/O3"
    context['javob4'] = "/O5"
       
    return render(request,"myApp/bayroq.html",context)
def oharf5(request):
    c = 'O'
    a =  'oymoma'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/O4"
    context['javob4'] = "/O0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################p
def pharf(request):
    c = 'P'
    a = ['paxta',  'paypoq',  'pirog', 'pirashka', 'pul', 'paynet']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def pharf0(request):
    c = 'P'
    a = 'paxta'  
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/P5"
    context['javob4'] = "/P1"
       
    return render(request,"myApp/bayroq.html",context)
def pharf1(request):
    c = 'P'
    a = 'paypoq' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/P0"
    context['javob4'] = "/P2"
       
    return render(request,"myApp/bayroq.html",context)
def pharf2(request):
    c = 'P'
    a =  'pirog'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/P1"
    context['javob4'] = "/P3"
       
    return render(request,"myApp/bayroq.html",context)
def pharf3(request):
    c = 'P'
    a = 'pirashka' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/P2"
    context['javob4'] = "/P4"
       
    return render(request,"myApp/bayroq.html",context)
def pharf4(request):
    c = 'P'
    a = 'pul' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/P3"
    context['javob4'] = "/P5"
       
    return render(request,"myApp/bayroq.html",context)
def pharf5(request):
    c = 'P'
    a = 'paynet'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/P4"
    context['javob4'] = "/P0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################q
def qharf(request):
    c = 'Q'
    a = ['quyosh', 'qirmiz',  'qiz', 'qolip', 'qachon', 'qaysar']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def qharf0(request):
    c = 'Q'
    a = 'quyosh'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Q5"
    context['javob4'] = "/Q1"
       
    return render(request,"myApp/bayroq.html",context)
def qharf1(request):
    c = 'Q'
    a =  'qirmiz' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Q0"
    context['javob4'] = "/Q2"
       
    return render(request,"myApp/bayroq.html",context)
def qharf2(request):
    c = 'Q'
    a =  'qiz'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Q1"
    context['javob4'] = "/Q3"
       
    return render(request,"myApp/bayroq.html",context)
def qharf3(request):
    c = 'Q'
    a =  'qolip' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Q2"
    context['javob4'] = "/Q4"
       
    return render(request,"myApp/bayroq.html",context)
def qharf4(request):
    c = 'Q'
    a = 'qachon'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Q3"
    context['javob4'] = "/Q5"
       
    return render(request,"myApp/bayroq.html",context)
def qharf5(request):
    c = 'Q'
    a =  'qaysar'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Q4"
    context['javob4'] = "/Q0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################r
def rharf(request):
    c = 'R'
    a = ['randa',  'radio',   'rom', 'rahmat', 'rayhon', 'rim']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def rharf0(request):
    c = 'R'
    a = 'randa' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/R5"
    context['javob4'] = "/R1"
       
    return render(request,"myApp/bayroq.html",context)
def rharf1(request):
    c = 'R'
    a =  'radio'  
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/R0"
    context['javob4'] = "/R2"
       
    return render(request,"myApp/bayroq.html",context)
def rharf2(request):
    c = 'R'
    a =  'rom'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/R1"
    context['javob4'] = "/R3"
       
    return render(request,"myApp/bayroq.html",context)
def rharf3(request):
    c = 'R'
    a =  'rahmat'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/R2"
    context['javob4'] = "/R4"
       
    return render(request,"myApp/bayroq.html",context)
def rharf4(request):
    c = 'R'
    a =  'rayhon'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/R3"
    context['javob4'] = "/R5"
       
    return render(request,"myApp/bayroq.html",context)
def rharf5(request):
    c = 'R'
    a =  'rim'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/R4"
    context['javob4'] = "/R0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################s
def sharf(request):
    c = 'S'
    a = ['salon',  'sevgi', 'suv', 'sinf', 'savdo', 'sovun']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def sharf0(request):
    c = 'S'
    a = 'salon'  
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/S5"
    context['javob4'] = "/S1"
       
    return render(request,"myApp/bayroq.html",context)
def sharf1(request):
    c = 'S'
    a ='sevgi'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/S0"
    context['javob4'] = "/S2"
       
    return render(request,"myApp/bayroq.html",context)
def sharf2(request):
    c = 'S'
    a =  'suv' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/S1"
    context['javob4'] = "/S3"
       
    return render(request,"myApp/bayroq.html",context)
def sharf3(request):
    c = 'S'
    a = 'sinf' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/S2"
    context['javob4'] = "/S4"
       
    return render(request,"myApp/bayroq.html",context)
def sharf4(request):
    c = 'S'
    a = 'savdo'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/S3"
    context['javob4'] = "/S5"
       
    return render(request,"myApp/bayroq.html",context)
def sharf5(request):
    c = 'S'
    a =  'sovun'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/S4"
    context['javob4'] = "/S0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################t
def tharf(request):
    c = 'T'
    a = ['tam','tandir',  'tarafdor', 'tentak', 'til', 'taom']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def tharf0(request):
    c = 'T'
    a = 'tam'  
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/T5"
    context['javob4'] = "/T1"
       
    return render(request,"myApp/bayroq.html",context)
def tharf1(request):
    c = 'T'
    a ='tandir' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/T0"
    context['javob4'] = "/T2"
       
    return render(request,"myApp/bayroq.html",context)
def tharf2(request):
    c = 'T'
    a =  'tarafdor' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/T1"
    context['javob4'] = "/T3"
       
    return render(request,"myApp/bayroq.html",context)
def tharf3(request):
    c = 'T'
    a = 'tentak' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/T2"
    context['javob4'] = "/T4"
       
    return render(request,"myApp/bayroq.html",context)
def tharf4(request):
    c = 'T'
    a = 'til' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/T3"
    context['javob4'] = "/T5"
       
    return render(request,"myApp/bayroq.html",context)
def tharf5(request):
    c = 'T'
    a = 'taom'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/T4"
    context['javob4'] = "/T0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################u
def uharf(request):
    c = 'U'
    a = ['umid',   'urmoq',   'umra', 'uyat', 'usta', 'usul']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def uharf0(request):
    c = 'U'
    a = 'umid'  
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/U5"
    context['javob4'] = "/U1"
       
    return render(request,"myApp/bayroq.html",context)
def uharf1(request):
    c = 'U'
    a =  'urmoq'  
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/U0"
    context['javob4'] = "/U2"
       
    return render(request,"myApp/bayroq.html",context)
def uharf2(request):
    c = 'U'
    a = 'umra' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/U1"
    context['javob4'] = "/U3"
       
    return render(request,"myApp/bayroq.html",context)
def uharf3(request):
    c = 'U'
    a = 'uy' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/U2"
    context['javob4'] = "/U4"
       
    return render(request,"myApp/bayroq.html",context)
def uharf4(request):
    c = 'U'
    a = 'umid' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/U3"
    context['javob4'] = "/U5"
       
    return render(request,"myApp/bayroq.html",context)
def uharf5(request):
    c = 'U'
    a = 'usul'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/U4"
    context['javob4'] = "/U0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################v
def vharf(request):
    c = 'V'
    a = ['vanna',  'vajohat', 'vertikal', 'video', 'vaqt', 'varrak']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"
    return render(request,"myApp/dharf.html",context)
def vharf0(request):
    c = 'V'
    a = 'vanna'  
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/V5"
    context['javob4'] = "/V1"
       
    return render(request,"myApp/bayroq.html",context)
def vharf1(request):
    c = 'V'
    a = 'vajohat' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/V0"
    context['javob4'] = "/V2"
       
    return render(request,"myApp/bayroq.html",context)
def vharf2(request):
    c = 'V'
    a = 'vertikal' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/V1"
    context['javob4'] = "/V3"
    return render(request,"myApp/bayroq.html",context)
def vharf3(request):
    c = 'V'
    a = 'video' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/V2"
    context['javob4'] = "/V4"
       
    return render(request,"myApp/bayroq.html",context)
def vharf4(request):
    c = 'V'
    a = 'vaqt'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/V3"
    context['javob4'] = "/V5"
       
    return render(request,"myApp/bayroq.html",context)
def vharf5(request):
    c = 'V'
    a =  'varrak'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/V4"
    context['javob4'] = "/V0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################x
def xharf(request):
    c = 'X'
    a = ['xayo' ,  'xursand' ,'xumor' ,'xohish', 'xurmo', 'xalqaro']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def xharf0(request):
    c = 'X'
    a = 'xayo'  
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/X5"
    context['javob4'] = "/X1"
       
    return render(request,"myApp/bayroq.html",context)
def xharf1(request):
    c = 'X'
    a =  'xursand' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/X0"
    context['javob4'] = "/X2"
       
    return render(request,"myApp/bayroq.html",context)
def xharf2(request):
    c = 'X'
    a = 'xumor' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/X1"
    context['javob4'] = "/X3"
       
    return render(request,"myApp/bayroq.html",context)
def xharf3(request):
    c = 'X'
    a = 'xohish'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/X2"
    context['javob4'] = "/X4"
       
    return render(request,"myApp/bayroq.html",context)
def xharf4(request):
    c = 'X'
    a =  'xurmo'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/X3"
    context['javob4'] = "/X5"
       
    return render(request,"myApp/bayroq.html",context)
def xharf5(request):
    c = 'X'
    a =  'xalqaro'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/X4"
    context['javob4'] = "/X0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################y
def yharf(request):
    c = 'Y'
    a = ['yaxshi','yaqin', 'yer' ,'yaramas', 'yuk', 'yomon']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def yharf0(request):
    c = 'Y'
    a = 'yaxshi' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Y5"
    context['javob4'] = "/Y1"
       
    return render(request,"myApp/bayroq.html",context)
def yharf1(request):
    c = 'Y'
    a = 'yaqin' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Y0"
    context['javob4'] = "/Y2"
       
    return render(request,"myApp/bayroq.html",context)
def yharf2(request):
    c = 'Y'
    a = 'yer' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Y1"
    context['javob4'] = "/Y3"
       
    return render(request,"myApp/bayroq.html",context)
def yharf3(request):
    c = 'Y'
    a = 'yaramas' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Y2"
    context['javob4'] = "/Y4"
    return render(request,"myApp/bayroq.html",context)
def yharf4(request):
    c = 'Y'
    a = 'yuk'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Y3"
    context['javob4'] = "/Y5"   
    return render(request,"myApp/bayroq.html",context)
def yharf5(request):
    c = 'Y'
    a =  'yomon'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Y4"
    context['javob4'] = "/Y0"
       
    return render(request,"myApp/bayroq.html",context)
#######################################################z
def zharf(request):
    c = 'Z'
    a = ['zarur' , 'zarda', 'zarba', 'zanjir', 'ziyod', 'zona']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def zharf0(request):
    c = 'Z'
    a = 'zarur' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Z5"
    context['javob4'] = "/Z1"
       
    return render(request,"myApp/bayroq.html",context)
def zharf1(request):
    c = 'Z'
    a =  'zarda' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Z0"
    context['javob4'] = "/Z2"
       
    return render(request,"myApp/bayroq.html",context)
def zharf2(request):
    c = 'Z'
    a = 'zarba'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Z1"
    context['javob4'] = "/Z3"
       
    return render(request,"myApp/bayroq.html",context)
def zharf3(request):
    c = 'Z'
    a =  'zanjir'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Z2"
    context['javob4'] = "/Z4"
       
    return render(request,"myApp/bayroq.html",context)
def zharf4(request):
    c = 'Z'
    a =  'ziyod' 
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Z3"
    context['javob4'] = "/Z5"
       
    return render(request,"myApp/bayroq.html",context)
def zharf5(request):
    c = 'Z'
    a = 'zona'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/Z4"
    context['javob4'] = "/Z0"
       
    return render(request,"myApp/bayroq.html",context)
########################################################A
def aharf(request):
    c = 'A'
    a = ['alla', 'archa', 'arava', 'ashula', 'arzon','asal']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def aharf0(request):
    c = 'A'
    a = 'alla'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/A5"
    context['javob4'] = "/A1"
    
    
    return render(request,"myApp/bayroq.html",context)
def aharf1(request):
    c = 'A'
    a = 'archa'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/A0"
    context['javob4'] = "/A2"
       
    return render(request,"myApp/bayroq.html",context)
def aharf2(request):
    c = 'A'
    a = 'arava'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/A1"
    context['javob4'] = "/A3"
       
    return render(request,"myApp/bayroq.html",context)
def aharf3(request):
    c = 'A'
    a = 'ashula'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/A2"
    context['javob4'] = "/A4"
       
    return render(request,"myApp/bayroq.html",context)
def aharf4(request):
    c = 'A'
    a = 'arzon'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/A3"
    context['javob4'] = "/A5"
       
    return render(request,"myApp/bayroq.html",context)
def aharf5(request):
    c = 'A'
    a = 'asal'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/A4"
    context['javob4'] = "/A0"
       
    return render(request,"myApp/bayroq.html",context)

#######################################################B
def bharf(request):
    c = 'B'
    a = ['bola', 'bastakor', 'beshik', 'bayroq', 'baqlajon','banan']
    b = []
    context={}
    context['jb'] = c
    
    for i in range (6):
        context['harf'+str(i)]="/"+c+str(i)
        context['jb'+str(i)] = a[i]
        context['javob'+str(i)] = "/static/assets/images/blog/"+c+"/"+a[i]+".jpg"

    return render(request,"myApp/dharf.html",context)
def bharf0(request):
    c = 'B'
    a = 'bola'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/B5"
    context['javob4'] = "/B1"
    
    return render(request,"myApp/bayroq.html",context)
def bharf1(request):
    c = 'B'
    a = 'bastakor'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/B0"
    context['javob4'] = "/B2"
       
    return render(request,"myApp/bayroq.html",context)
def bharf2(request):
    c = 'B'
    a = 'beshik'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/B1"
    context['javob4'] = "/B3"
       
    return render(request,"myApp/bayroq.html",context)
def bharf3(request):
    c = 'B'
    a = 'bayroq'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/B2"
    context['javob4'] = "/B4"
       
    return render(request,"myApp/bayroq.html",context)
def bharf4(request):
    c = 'B'
    a = 'baqlajon'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/B3"
    context['javob4'] = "/B5"
       
    return render(request,"myApp/bayroq.html",context)
def bharf5(request):
    c = 'B'
    a = 'banan'
    b = "/static/assets/images/blog/"+c+"/"+a+".jpg"
    d = "/static/assets/audios/"+c+"/"+a+".wav"
    context={}
    context['javob'] = a
    context['javob1'] = b
    context['javob2'] = d
    context['javob3'] = "/B4"
    context['javob4'] = "/B0"
       
    return render(request,"myApp/bayroq.html",context)

#######################################################F
    

