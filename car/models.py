from django.db import models
from django.core.validators import RegexValidator
class Region(models.Model):
    name=models.CharField(max_length=250,verbose_name="Viloyat nomi",unique=True)
    status=models.BooleanField(default=True,verbose_name="Holati")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Yaratilgan vaqti")
    def __str__(self):
        return self.name
    
    
class Company(models.Model):
    name=models.CharField(max_length=250,verbose_name="Kompaniya nomi",unique=True)
    logo=models.ImageField(upload_to="company/",verbose_name="Kompaniya logotipi")
    status=models.BooleanField(default=True,verbose_name="Holati")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Yaratilgan vaqti")
    def __str__(self):
        return self.name


class Car(models.Model):
    PR=RegexValidator(regex="^[+]998[0-9]{9}$",message="Telefon raqami +998991232323 formatida bo'lishi kerak")
    FUELS=(
        ("Benzin","Benzin"),
        ("Dizel","Dizel"),
        ("Gaz","Gaz"),
        ("Hibrid","Hibrid"),
        ("Elektr","Elektr"),
    )
    COLORS=(
        ("Qora","Qora"),
        ("Oq","Oq"),
        ("Qizil","Qizil"),
        ("Yashil","Yashil"),
        ("Kulrang","Kulrang"),
        ("Sariq","Sariq"),
        ("Jigarrang","Jigarrang"),
        ('Boshqa','Boshqa'),
    )

    T_BOX=(
        ("Avtomatic","Avtomat"),
        ("Mechanic","Mexanika"),
    )

    BODY_TYPES=(
        ("Sedan","Sedan"),
        ("Krossover","Krossover"),
        ("Other","Other"))
    
    km=models.IntegerField(verbose_name="Yurgan masofasi")
    body_type=models.CharField(max_length=250,verbose_name="Kuzov turi",choices=BODY_TYPES,default="Sedan")
    model=models.CharField(max_length=250,verbose_name="Model nomi",unique=True)
    price=models.PositiveIntegerField(verbose_name="Narxi")
    engine=models.CharField(max_length=250,verbose_name="Dvigatel hajmi")
    km=models.IntegerField(verbose_name="Yurgan masofasi")
    vin=models.CharField(max_length=250,verbose_name="VIN raqami",unique=True)
    year=models.IntegerField(verbose_name="Ishlab chiqarilgan yili")
    region=models.ForeignKey(Region,on_delete=models.CASCADE,verbose_name="Viloyat")
    t_box=models.CharField(max_length=250,verbose_name="Uzatmalar qutisi",default="Avtomatic",choices=T_BOX)
    phone=models.CharField(max_length=13,verbose_name="Telefon raqami",validators=[PR])
    company=models.ForeignKey(Company,on_delete=models.CASCADE,verbose_name="Kompaniya")
    image=models.ImageField(upload_to="car/",verbose_name="Avtomobil rasmi")
    color=models.CharField(max_length=250,verbose_name="Rangi",choices=COLORS,default="Boshqa")
    fuel_type=models.CharField(max_length=250,verbose_name="Yoqilg'i turi",choices=FUELS,default="Benzin")

    status=models.BooleanField(default=True,verbose_name="Holati")
    about=models.TextField(verbose_name="Batafsil ma'lumot",null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Yaratilgan vaqti")

    def __str__(self):
        return self.model
    
