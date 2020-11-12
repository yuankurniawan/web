from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from . import models, forms
from django.db.models import Q


# Create your views here.
def page_login(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    form = forms.CustomUserLogin()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        post = request.POST
        email = post['email']
        password = post['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html', context)
    
def dashboardForm(request):

    form = forms.inputFileInfo()
    context = {
        'form': form,
    }

    if request.method == 'POST':
            form = forms.inputFileInfo(request.POST, request.FILES)
            if form.is_valid():
                form.save()

    return render(request, 'editForm.html', context)

def dashboardFolderForm(request):

    form = forms.inputFolderInfo()
    context = {
        'form': form,
    }

    if request.method == 'POST':
            post = request.POST
            nama_folder = post['nama_folder']
            desc_folder = post['desc_folder']
            baseFolder_nama = models.baseFolder.objects.get(id = post['baseFolder_nama'])
            prodi_name = models.listProdi.objects.get(id = post['prodi_name'])
            new_file = models.baruFolder(
                nama_folder = nama_folder,
                desc_folder = desc_folder,
                baseFolder_nama = baseFolder_nama,
                prodi_name = prodi_name
            )
            new_file.save()
    return render(request, 'editFolderForm.html', context)

def homepage(request):
    folder = models.FolderUtama.objects.all()

    if request.user.is_authenticated == False:
        return redirect('login')

    if request.user.prodi == 'DBT':
        
        context = {
            'Prodi' : 'Digital Business Technology',
            'folder': folder,
        }
        return render(request, 'card.html', context)
    
    elif request.user.prodi == 'FBT':
        context = {
            'folder': folder,
            'Prodi' : 'Food Business Technology'
        }
        return render(request, 'card.html', context)
    
    elif request.user.prodi == 'BM':
        context = {
            'folder': folder,
            'Prodi' : 'Business Mathematics'
        }
        return render(request, 'card.html', context)

    elif request.user.prodi == 'PDE':
        context = {
            'folder': folder,
            'Prodi' : 'Product Design Engineering'
        }
        return render(request, 'card.html', context)

    elif request.user.prodi == 'REE':
        context = {
            'folder': folder,
            'Prodi' : 'Renewable Energy Engineering'
        }
        return render(request, 'card.html', context)

    elif request.user.prodi == 'CSE':
        context = {
            'folder': folder,
            'Prodi' : 'Computer System Engineering'
        }
        return render(request, 'card.html', context)

def informasiUmum(request):

    folder = models.baruFolder.objects.filter(baseFolder_nama = 1)
    # print(folder.baseFolder_nama, '#####')
    context = {
        'folder': folder,
        'id': 1,
        "informasi_umum": "active"
    }

    return render(request, 'card01.html', context)

def akreditasiUmum(request):

    folder = models.baruFolder.objects.filter(baseFolder_nama = 7)
    # print(folder.baseFolder_nama, '#####')
    context = {
        'folder': folder,
        'id': 7,
        "akreditasi": "active"
    }

    return render(request, 'card01.html', context)

def auditUmum(request):

    folder = models.baruFolder.objects.get(nama_folder = 'Audit Umum')
    files = models.baruFile.objects.filter(nama_folder = folder)

    context = {
        'files': files,
        "audit": "active"
    }
    return render(request, 'list.html', context)

def auditProdi(request):

    folder = models.baruFolder.objects.filter(baseFolder_nama = 25)
    # print(folder.baseFolder_nama, '#####')
    context = {
        'folder': folder,
        'id': 25,
        "audit": "active"
    }

    return render(request, 'card01.html', context)

def akreditasiProdi(request):

    folder = models.baruFolder.objects.filter(baseFolder_nama = 19)
    # print(folder.baseFolder_nama, '#####')
    context = {
        'folder': folder,
        'id': 1,
        "akreditasi": "active"
    }

    return render(request, 'card01.html', context)

def updateFile(request, file_id, folder_id):

    form = forms.inputFileInfo()
    files = models.baruFile.objects.get(id = file_id)

    form.nama_file = files.nama_file
    form.desc_file = files.desc_file
    form.upload_file = files.upload_file
    form.nama_folder = files.nama_folder

    context = {
        'form' : form,
    }

    return render(request, 'editForm.html', context)

def update_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(models.baruFile, id = id) 
  
    # pass the object as instance in form 
    form = forms.inputFileInfo(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return redirect('homepage') 
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "editForm.html", context)

def logout_user(request):
    logout(request)
    return redirect('homepage')

def delete_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(models.baruFile, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return redirect('homepage')
  
    return render(request, "delete_view.html", context) 

def update_folder_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(models.baruFolder, id = id) 
  
    # pass the object as instance in form 
    form = forms.inputFolderInfo(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return redirect('homepage')
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "editFolderForm.html", context)

def delete_folder_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(models.baruFolder, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return redirect('homepage')
  
    return render(request, "delete_view.html", context) 

def informasiUmumDetailView(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={"informasi_umum": "active"} 
    print(id)

    # fetch the object related to passed id 
    obj = get_object_or_404(models.FolderUtama, id = id)
    x = str(obj)

    if x == "Informasi Umum":
        return informasiUmum(request)
    elif x == "Audit Umum":
        return auditUmum(request)
    elif x == "Audit Prodi":
        return auditProdi(request)
    elif x == "Akreditasi Prodi":
        return akreditasiProdi(request)
    elif x == "Akreditasi Umum":
        return akreditasiUmum(request)
    else:
        return render(request, 'card.html')

def informasiUmumDetailView1(request, id): 
    # dictionary for initial data with  
    # field names as keys
    is_search = request.method=='POST' 
    context ={
                "informasi_umum": "active",
            } 
    
    # fetch the object related to passed id 
    obj = get_object_or_404(models.baruFolder, id = id)
    x = str(obj)
    print(obj)
    if x == "Peraturan - Peraturan":
        folder = models.baruFolder.objects.get(nama_folder = 'Peraturan - Peraturan')
        print(folder, '####')
        files = models.baruFile.objects.filter(nama_folder = folder)
        if is_search:
            search = request.POST['search']
            files = models.baruFile.objects.filter(Q(nama_folder = folder) & Q(nama_file__contains = search) | Q(desc_file__contains = search))
            print(search)
        print(files, '#####')
        context = {
            'files': files,
        }
        return render(request, 'list.html', context)

    elif x == "Standar Universitas":
        folderUtama = models.baseFolder.objects.get(nama_baseFolder = 'Standar Universitas')
        folder = models.baruFolder.objects.filter(baseFolder_nama = folderUtama)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'folder': folder,
            'id': 32
        }
        return render(request, 'card01.html', context)

    elif x == "Standar Sekolah":
        folder = models.StandarSekolah.objects.all()
        # print(folder.baseFolder_nama, '#####')
        context = {
            'folder': folder,
            'id': 33
        }
        return render(request, 'card01.html', context)
    elif x == "Buku Panduan":
        folder = models.baruFolder.objects.get(nama_folder = 'Buku Panduan')
        files = models.baruFile.objects.filter(nama_folder = folder)
        # print(folder.baseFolder_nama, '#####')
        if is_search:
            search = request.POST['search']
            files = models.baruFile.objects.filter(Q(nama_folder = folder) & Q(nama_file__contains = search) | Q(desc_file__contains = search))
            print(search)
        context = {
            'files': files,
        }
        return render(request, 'list.html', context)

    elif x == "Lain - Lain":
        folder = models.baruFolder.objects.get(nama_folder = 'Lain - Lain')
        files = models.baruFile.objects.filter(nama_folder = folder)
        # print(folder.baseFolder_nama, '#####')
        if is_search:
            search = request.POST['search']
            files = models.baruFile.objects.filter(Q(nama_folder = folder) & Q(nama_file__contains = search) | Q(desc_file__contains = search))
            print(search)
        context = {
            'files': files,
        }
        return render(request, 'list.html', context)

    elif x == "AMI 20182":
        folder = models.baruFolder.objects.get(nama_folder = 'AMI 20182')
        files = models.baruFile.objects.filter(nama_folder = folder)
        # print(folder.baseFolder_nama, '#####')
        if is_search:
            search = request.POST['search']
            files = models.baruFile.objects.filter(Q(nama_folder = folder) & Q(nama_file__contains = search) | Q(desc_file__contains = search))
            print(search)
        context = {
            'files': files,
        }
        return render(request, 'list.html', context)
    
    elif x == "AMI 20191":
        folder = models.baruFolder.objects.get(nama_folder = 'AMI 20191')
        files = models.baruFile.objects.filter(nama_folder = folder)
        if is_search:
            search = request.POST['search']
            files = models.baruFile.objects.filter(Q(nama_folder = folder) & Q(nama_file__contains = search) | Q(desc_file__contains = search))
            print(search)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'files': files,
        }
        return render(request, 'list.html', context)

    elif x == "AMI 20192":
        folder = models.baruFolder.objects.get(nama_folder = 'AMI 20192')
        files = models.baruFile.objects.filter(nama_folder = folder)
        if is_search:
            search = request.POST['search']
            files = models.baruFile.objects.filter(Q(nama_folder = folder) & Q(nama_file__contains = search) | Q(desc_file__contains = search))
            print(search)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'files': files,
            'id': 8
        }
        return render(request, 'list.html', context)

    elif x == "AMI 20201":
        folder = models.baruFolder.objects.get(nama_folder = 'AMI 20201')
        files = models.baruFile.objects.filter(nama_folder = folder)
        # print(folder.baseFolder_nama, '#####')
        if is_search:
            search = request.POST['search']
            files = models.baruFile.objects.filter(Q(nama_folder = folder) & Q(nama_file__contains = search) | Q(desc_file__contains = search))
            print(search)
        context = {
            'files': files,
        }
        return render(request, 'list.html', context)

    elif x == "AMI 20202":
        folder = models.baruFolder.objects.get(nama_folder = 'AMI 20202')
        files = models.baruFile.objects.filter(nama_folder = folder)
        # print(folder.baseFolder_nama, '#####')
        if is_search:
            search = request.POST['search']
            files = models.baruFile.objects.filter(Q(nama_folder = folder) & Q(nama_file__contains = search) | Q(desc_file__contains = search))
            print(search)
        context = {
            'files': files,
        }
        return render(request, 'list.html', context)

    elif x == "Instrumen IAPS4.0 BAN PT":
        folder = models.baruFolder.objects.get(nama_folder = 'Instrumen IAPS4.0 BAN PT')
        files = models.baruFile.objects.filter(nama_folder = folder)
        # print(folder.baseFolder_nama, '#####')
        if is_search:
            search = request.POST['search']
            files = models.baruFile.objects.filter(Q(nama_folder = folder) & Q(nama_file__contains = search) | Q(desc_file__contains = search))
            print(search)
        context = {
            'files': files,
        }
        return render(request, 'list.html', context)

    elif x == "Sosialisasi IAPS4.0":
        folder = models.baruFolder.objects.get(nama_folder = 'Sosialisasi IAPS4.0')
        files = models.baruFile.objects.filter(nama_folder = folder)
        # print(folder.baseFolder_nama, '#####')
        if is_search:
            search = request.POST['search']
            files = models.baruFile.objects.filter(Q(nama_folder = folder) & Q(nama_file__contains = search) | Q(desc_file__contains = search))
            print(search)
        context = {
            'files': files,
        }
        return render(request, 'list.html', context)

    elif x == "MoM Komite Akreditasi":
        folder = models.baruFolder.objects.get(nama_folder = 'MoM Komite Akreditasi')
        files = models.baruFile.objects.filter(nama_folder = folder)
        # print(folder.baseFolder_nama, '#####')
        if is_search:
            search = request.POST['search']
            files = models.baruFile.objects.filter(Q(nama_folder = folder) & Q(nama_file__contains = search) | Q(desc_file__contains = search))
            print(search)
        context = {
            'files': files,
        }
        return render(request, 'list.html', context)

    elif x == "Kriteria 1":
        folderUtama = models.baseFolder.objects.get(nama_baseFolder = 'Kriteria 1')
        folder = models.baruFolder.objects.filter(baseFolder_nama = folderUtama)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'folder': folder,
            'id': 34
        }
        return render(request, 'card01.html', context)

    elif x == "Kriteria 2":
        folderUtama = models.baseFolder.objects.get(nama_baseFolder = 'Kriteria 2')
        folder = models.baruFolder.objects.filter(baseFolder_nama = folderUtama)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'folder': folder,
            'id': 35
        }
        return render(request, 'card01.html', context)

    elif x == "Kriteria 3":
        folderUtama = models.baseFolder.objects.get(nama_baseFolder = 'Kriteria 3')
        folder = models.baruFolder.objects.filter(baseFolder_nama = folderUtama)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'folder': folder,
            'id': 36
        }
        return render(request, 'card01.html', context)

    elif x == "Kriteria 4":
        folderUtama = models.baseFolder.objects.get(nama_baseFolder = 'Kriteria 4')
        folder = models.baruFolder.objects.filter(baseFolder_nama = folderUtama)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'folder': folder,
            'id': 37
        }
        return render(request, 'card01.html', context)

    elif x == "Kriteria 5":
        folderUtama = models.baseFolder.objects.get(nama_baseFolder = 'Kriteria 5')
        folder = models.baruFolder.objects.filter(baseFolder_nama = folderUtama)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'folder': folder,
            'id': 38
        }
        return render(request, 'card01.html', context)

    elif x == "Kriteria 6":
        folderUtama = models.baseFolder.objects.get(nama_baseFolder = 'Kriteria 6')
        folder = models.baruFolder.objects.filter(baseFolder_nama = folderUtama)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'folder': folder,
            'id': 39
        }
        return render(request, 'card01.html', context)

    elif x == "Kriteria 7":
        folderUtama = models.baseFolder.objects.get(nama_baseFolder = 'Kriteria 7')
        folder = models.baruFolder.objects.filter(baseFolder_nama = folderUtama)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'folder': folder,
            'id': 40
        }
        return render(request, 'card01.html', context)

    elif x == "Kriteria 8":
        folderUtama = models.baseFolder.objects.get(nama_baseFolder = 'Kriteria 8')
        folder = models.baruFolder.objects.filter(baseFolder_nama = folderUtama)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'folder': folder,
            'id': 41
        }
        return render(request, 'card01.html', context)

    elif x == "Kriteria 9":
        folderUtama = models.baseFolder.objects.get(nama_baseFolder = 'Kriteria 9')
        folder = models.baruFolder.objects.filter(baseFolder_nama = folderUtama)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'folder': folder,
            'id': 42
        }
        return render(request, 'card01.html', context)

    elif x == "LKPT dan LED":
        folderUtama = models.baseFolder.objects.get(nama_baseFolder = 'LKPT dan LED')
        folder = models.baruFolder.objects.filter(baseFolder_nama = folderUtama)
        # print(folder.baseFolder_nama, '#####')
        context = {
            'folder': folder,
            'id': 43
        }
        return render(request, 'card01.html', context)

    else:
        return render(request, 'list.html')


def informasiUmum_add_folder(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
    
    # fetch the object related to passed id
    obj = get_object_or_404(models.baseFolder, id = id)
    print(obj)
    print(id)
    # pass the object as instance in form 
    form = forms.InformasiUmumForm()
    context = {
        'form': form,
        'id' : id,
    }

    if request.method == 'POST':
            post = request.POST
            nama_folder = post['nama_folder']
            desc_folder = post['desc_folder']
            baseFolder_nama = obj
            prodi_name = models.listProdi.objects.get(id = post['prodi_name'])
            new_file = models.baruFolder(
                nama_folder = nama_folder,
                desc_folder = desc_folder,
                baseFolder_nama = baseFolder_nama,
                prodi_name = prodi_name
            )
            new_file.save()
  
    return render(request, "editFolderForm.html", context)
