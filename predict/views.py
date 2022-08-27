import pickle
from django.shortcuts import render

# Create your views here.
def predictor(request):
    if request.method=='POST':
        model=pickle.load(open('sih.sav','rb'))
        #prediction=model.predict([tlr,rs,go,oi,pr])
#      return prediction
# def result(request):
        ss=float(request.POST['SS'])
        fsr=float(request.POST['FSR'])
        fqe=float(request.POST['FQE'])
        fru=float(request.POST['FRU'])
        pu=float(request.POST['PU'])
        qp=float(request.POST['QP'])
        ipr=float(request.POST['IPR'])
        fppp=float(request.POST['FPPP'])
        gph=float(request.POST['GPH'])
        gue=float(request.POST['GUE'])
        ms=float(request.POST['MS'])
        gphd=float(request.POST['GPHD'])
        rd=float(request.POST['RD'])
        wd=float(request.POST['WD'])
        escs=float(request.POST['ESCS'])
        pcs=float(request.POST['PCS'])
        pr=float(request.POST['PR'])
        ss=ss*0.3*0.2
        fsr=fsr*0.3*0.3
        fqe=fqe*0.3*0.2
        fru=fru*0.3*0.3
        tlr=ss+fsr+fqe+fru
        pu=pu*0.3*0.35
        qp=qp*0.4*0.3
        ipr=ipr*0.3*0.15
        fppp=fppp*0.3*0.2
        rs=pu+qp+ipr+fppp
        gph=gph*0.2*0.4
        gue=gue*0.2*0.15
        ms=ms*0.2*0.25
        gphd=gphd*0.2*0.2
        go=gph+gue+ms+gphd
        rd=rd*0.1*0.3
        wd=wd*0.1*0.3
        escs=escs*0.1*0.2
        pcs=pcs*0.1*0.2
        oi=rd+wd+escs+pcs
        pr=pr*0.1
        prediction=model.predict([[tlr,rs,go,oi,pr]])
        return render(request,'predict.html',{'result':prediction})
    return render(request,'predict.html')
