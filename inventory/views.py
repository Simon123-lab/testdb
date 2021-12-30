from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.

def insertdata(request):
   if request.method=='POST':
      namedata=request.POST['name']
      phonedata=request.POST['phone']
      addressdata=request.POST['address']
      customerdata=Customer.objects.create(name=namedata,phone=phonedata,address=addressdata)



      customerdata.save()
      return render(request,'Customer.html',{"msg":"Data Inserted"})

   else:
      return render(request,'Customer.html')

def checkuser(request):
   saud = Customer.objects.all().filter(name='zohaib')
   print(saud)
   return render(request, 'Customerdata.html')

def register(request):
   if request.method=='POST':
      username=request.POST['name']
      userpassword=request.POST['password']
      hashpassword=make_password(userpassword)
      userphone = request.POST['phone']
      userdata=Register.objects.create(user_name=username,user_password=hashpassword,user_phone=userphone)
      userdata.save()
      return render(request,'UserRegistration.html')


   else:
      return render(request,'UserRegistration.html')

def viewcustomer(request):
   mydata=Customer.objects.all()
   return render(request,'ViewCustomer.html',{"data":mydata})

def delete(request,id):
   mydata=Customer.objects.get(id=id)
   mydata.delete()
   return redirect('/viewcustomer')

def list(request):
   if request.method == 'POST':
      namedata = request.POST['name']
      phonedata = request.POST['phone']
      addressdata = request.POST['address']
      imaged=request.FILES['image']
      customerdata = Customer.objects.create(name=namedata, phone=phonedata, address=addressdata,image_data=imaged)

      customerdata.save()
      return render(request, 'ViewCustomer.html', {"msg": "Data Inserted"})

   else:

      return render(request, 'mycustomerlist.html')


def pro(request):
   if request.method == 'POST':
      productname = request.POST['name']
      productprice = request.POST['price']
      productdate = request.POST['date']
      #data1 = Customer.objects.filter(cust_id=ordfk)
      user = Category.objects.only('id').get(id=request.POST['data'])

      data = Product.objects.create(product_name=productname, product_price=productprice,expriy_date=productdate,fk_cat=user)


      data.save()
      prod = Category.objects.all()
      return render(request, 'Product.html', {"msg": "Datainserted"})

   else:
      prod = Category.objects.all()
      return render(request, 'Product.html',{"prod":prod})