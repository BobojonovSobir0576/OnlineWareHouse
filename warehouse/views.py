from django.shortcuts import render
from warehouse.models import *
from django.db.models import Count,Sum

def barcode(request):
    list_scan_product = []
    msg = ''
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        try: filter_barcode = ProductBarcode.objects.get(barcode = barcode) 
        except ProductBarcode.DoesNotExist: filter_barcode = None
        print(filter_barcode)
        if filter_barcode == None:
            msg = 'Нет товаров с таким идентификатором штрих-кода, попробуйте еще раз и посмотрите другие товары'
            return render(request,'index.html',context={'products':list_scan_product,'msg':msg}) 
        create_new_scan_model = Scanproduct(name_product=filter_barcode.name_product,barcode=barcode).save()
    for i in ProductBarcode.objects.all():
        for k in Scanproduct.objects.filter(barcode = i.barcode).values('barcode').annotate(amount = Count('barcode')).values('name_product','barcode','amount'):
            list_scan_product.append({'name':i.name_product,'barcode':i.barcode,'warehouse':i.warehouse,'sums':i.input_price,'remain_product':i.number_remaining_stack , 'amount':k['amount'],'separate_amount':i.number_remaining_stack - k['amount']})
            excel_download = ProductBarcode.objects.filter(barcode = i.barcode).update(amount = k['amount'])
    return render(request,'index.html',context={'products':list_scan_product,'msg':msg})