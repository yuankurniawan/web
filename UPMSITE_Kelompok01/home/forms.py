from django import forms
from . import models


class CustomUserLogin(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = {'email', 'password'}

        '''
        widgets = {
            'email' : forms.EmailInput(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'password' : forms.Password(attrs={'class': 'form-control', 'placeholder' : 'you@email.com'}),
        }
        '''

class inputFileInfo(forms.ModelForm):
    class Meta:
        model = models.baruFile
        fields = {'nama_file', 'desc_file', 'upload_file', 'nama_folder'}

        '''
        widgets = {
            'nama_file' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'fileName'}),
            'desc_file' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'link_file' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'nama_folder' : forms.Select(attrs=('class': 'form-control'))
        }
        '''

class inputFolderInfo(forms.ModelForm):
    class Meta:
        model = models.baruFolder
        fields = {'nama_folder', 'desc_folder', 'baseFolder_nama', 'prodi_name'}

        '''
        widgets = {
            'nama_folder' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'fileName'}),
            'desc_folder' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'prodi_name' : forms.Select(attrs=('class': 'form-control'))
            'baseFolder_nama' : forms.Select(attrs=('class': 'form-control'))

        }
        '''

class InformasiUmumForm(forms.ModelForm):
    class Meta:
        model = models.InformasiUmum
        fields = {'nama_folder', 'desc_folder', 'prodi_name'}

        '''
        widgets = {
            'nama_folder' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'fileName'}),
            'desc_folder' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'prodi_name' : forms.Select(attrs=('class': 'form-control'))

        }
        '''

class AuditUmumForm(forms.ModelForm):
    class Meta:
        model = models.AuditUmum
        fields = {'nama_folder', 'desc_folder', 'prodi_name'}

        '''
        widgets = {
            'nama_folder' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'fileName'}),
            'desc_folder' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'prodi_name' : forms.Select(attrs=('class': 'form-control'))

        }
        '''

class AuditProdiForm(forms.ModelForm):
    class Meta:
        model = models.AuditProdi
        fields = {'nama_folder', 'desc_folder', 'prodi_name'}

        '''
        widgets = {
            'nama_folder' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'fileName'}),
            'desc_folder' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'prodi_name' : forms.Select(attrs=('class': 'form-control'))

        }
        '''

class AkreditasiUmumForm(forms.ModelForm):
    class Meta:
        model = models.AkreditasiUmum
        fields = {'nama_folder', 'desc_folder', 'prodi_name'}

        '''
        widgets = {
            'nama_folder' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'fileName'}),
            'desc_folder' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'prodi_name' : forms.Select(attrs=('class': 'form-control'))

        }
        '''

class AkreditasiProdiForm(forms.ModelForm):
    class Meta:
        model = models.AkreditasiProdi
        fields = {'nama_folder', 'desc_folder', 'prodi_name'}

        '''
        widgets = {
            'nama_folder' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'fileName'}),
            'desc_folder' : forms.CharField(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'prodi_name' : forms.Select(attrs=('class': 'form-control'))

        }
        '''