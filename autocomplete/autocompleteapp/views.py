from django.shortcuts import render , redirect
from django.http import HttpResponse ,JsonResponse
from .models import Shortcuts
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
x=datetime.now()
y=x.strftime('%Y-%m-%d')
from django.forms.models import model_to_dict



# Main Page
# @login_required(login_url='/login')
def home_page(request): 
    return render(request,'home_page.html')

#------------------------------------------------------------------------
# Accounts
#------------------------------------------------------------------------
# shortcut page call
# @login_required(login_url='/login')
def shortcut(request):
    return render(request,'Shortcuts/shortcuts.html')

# shortcut Insert
def shortcut_insert(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Description = request.POST['Description']
        Is_Enable=1
        if Name=='' or Description=='' :
            return JsonResponse('Plese Fill Required Fields',safe=False)
        else:
            insert_shortcut = Shortcuts( Name = Name , Description = Description , Is_Enable=1 , Created_on = y)
            insert_shortcut.save()
            return JsonResponse("Shortcut Created",safe=False)

# shortcut select
def shortcut_select(request):
    # shortcut_select = Shortcuts.objects.filter(Is_Enable=1)
    shortcut_select = Shortcuts.objects.filter(Is_Enable=1)
    return render(request,'Shortcuts/shortcut_select.html' , {'shortcut_select':shortcut_select})

# shortcut load data for update
def shortcut_load_for_update(request , shortcut_id):
    data = Shortcuts.objects.get(Shortcut_id = shortcut_id)
    return JsonResponse(model_to_dict(data))

# shortcut Update
def shortcut_update(request):
    if request.method == 'POST':
        Shortcut_id = request.POST['edit_Shortcut_id']
        Name = request.POST['edit_Name']
        Description = request.POST['edit_Description']
        Is_Enable=1
        if Name == '' or Description== '':
            return JsonResponse('Please Enter Required fields' , safe = False)
        else:
            update = Shortcuts.objects.get(Shortcut_id = Shortcut_id)
            update.Name = Name
            update.Description = Description
            update.Is_Enable = Is_Enable
            update.Updated_on = y
            update.save()
            return JsonResponse('Shortcut Updated',safe=False)
        
def shortcut_disable(request):
    if request.method == 'POST':
        Shortcut_id = request.POST['id']
        Is_Enable=0
        update = Shortcuts.objects.get(Shortcut_id = Shortcut_id)
        update.Is_Enable = Is_Enable
        update.Updated_on = y
        update.save()
        return JsonResponse('Shortcut Updated',safe=False)
    
def shortcut_search(request):
    if request.method == 'POST':
        Shortcut = request.POST['shortcut']
        shortcut_select = Shortcuts.objects.filter(Name__icontains=Shortcut)
        return render(request,'Shortcuts/shortcut_select.html' , {'shortcut_select':shortcut_select})
        # return JsonResponse(model_to_dict(search))
        
def search_shortcut(request):
    return render(request,'Shortcuts/search_shortcut.html')

# def load_all_accounts(request):
#     select_accounts = Shortcuts.objects.all()
#     return render(request,'Shortcuts/other/shortcutlist.html',{'select_accounts':select_accounts})


def sell_item_load(request):
    if request.method == 'POST':
        item_id = request.POST['item_id']
    # shortcut_select = Shortcuts.objects.get(Name__icontains=item_id)
    shortcut_select = Shortcuts.objects.get(Name=item_id)
    # shortcut_select = Shortcuts.objects.raw('Select Description From autocompleteapp_shortcuts where Name LIKE "ddl"')
    return JsonResponse(model_to_dict(shortcut_select))