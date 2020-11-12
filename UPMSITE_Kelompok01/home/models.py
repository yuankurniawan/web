from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.

class listProdi(models.Model):
    nama_prodi = models.CharField(default='', max_length=256)

    def __str__(self):
        return '{}'.format(self.nama_prodi)

class baseFolder(models.Model):
    nama_baseFolder = models.CharField(default='', max_length=256)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_baseFolder)

class baruFolder(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_folder = models.CharField(default='', max_length=256)
    desc_folder = models.TextField(default='', max_length=256)
    baseFolder_nama = models.ForeignKey(baseFolder, on_delete=models.CASCADE)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_folder)
    
class baruFile(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_file = models.CharField(default='', max_length=256)
    desc_file = models.TextField()
    upload_file = models.FileField(max_length=50, null=True)
    nama_folder = models.ForeignKey(baruFolder, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_file)

class UserManager(BaseUserManager):
    def _create_user(self, email, fullname, prodi, status, is_staff, is_active, password, **extra_fields):

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          fullname=fullname,
                          prodi=prodi,
                          status=status,
                          is_staff=is_staff,
                          is_active=is_active,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,  email, fullname, prodi, status, is_staff, is_active, password=None, **extra_fields):
        return self._create_user(email, fullname, prodi, status, is_staff, True, password, **extra_fields)

    def create_superuser(self, email, fullname, prodi, status, is_staff, is_active, password=None, **extra_fields):
        return self._create_user(email, fullname, prodi, "Admin", True, True, password,  **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    STATUS_USER = (
        ('Admin', 'Admin'),
        ('FM', 'FM'),
        ('PS', 'PS'),
    )
    created_on = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=255)
    # Prodi ini harusnya Foreign Key ke model Prodi
    prodi = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS_USER, blank=True, null=True, default='Admin')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'status', 'prodi', 'is_active', 'is_staff']

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return '{} / {}'.format(self.fullname, self.email)
    
class FolderUtama(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_folder = models.CharField(default='', max_length=256)
    desc_folder = models.TextField(default='', max_length=256)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_folder)

class InformasiUmum(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_folder = models.CharField(default='', max_length=256)
    desc_folder = models.TextField(default='', max_length=256)
    baseFolder_nama = models.ForeignKey(FolderUtama, on_delete=models.CASCADE)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_folder)

class Peraturan(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_folder = models.CharField(default='', max_length=256)
    desc_folder = models.TextField(default='', max_length=256)
    baseFolder_nama = models.ForeignKey(FolderUtama, on_delete=models.CASCADE)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_folder)

class StandarUniv(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_folder = models.CharField(default='', max_length=256)
    desc_folder = models.TextField(default='', max_length=256)
    baseFolder_nama = models.ForeignKey(FolderUtama, on_delete=models.CASCADE)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_folder)

class StandarSekolah(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_folder = models.CharField(default='', max_length=256)
    desc_folder = models.TextField(default='', max_length=256)
    baseFolder_nama = models.ForeignKey(FolderUtama, on_delete=models.CASCADE)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_folder)

class BukuPanduan(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_folder = models.CharField(default='', max_length=256)
    desc_folder = models.TextField(default='', max_length=256)
    baseFolder_nama = models.ForeignKey(FolderUtama, on_delete=models.CASCADE)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_folder)

class InfoUmumLain(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_folder = models.CharField(default='', max_length=256)
    desc_folder = models.TextField(default='', max_length=256)
    baseFolder_nama = models.ForeignKey(FolderUtama, on_delete=models.CASCADE)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_folder)

class AuditUmum(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_folder = models.CharField(default='', max_length=256)
    desc_folder = models.TextField(default='', max_length=256)
    baseFolder_nama = models.ForeignKey(FolderUtama, on_delete=models.CASCADE)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_folder)

class AkreditasiUmum(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_folder = models.CharField(default='', max_length=256)
    desc_folder = models.TextField(default='', max_length=256)
    baseFolder_nama = models.ForeignKey(FolderUtama, on_delete=models.CASCADE)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_folder)

class AuditProdi(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_folder = models.CharField(default='', max_length=256)
    desc_folder = models.TextField(default='', max_length=256)
    baseFolder_nama = models.ForeignKey(FolderUtama, on_delete=models.CASCADE)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_folder)

class AkreditasiProdi(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    nama_folder = models.CharField(default='', max_length=256)
    desc_folder = models.TextField(default='', max_length=256)
    baseFolder_nama = models.ForeignKey(FolderUtama, on_delete=models.CASCADE)
    prodi_name = models.ForeignKey(listProdi, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nama_folder)