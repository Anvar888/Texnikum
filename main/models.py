from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="news/")
    created_at = models.DateField("Sana")  # admin orqali qo‘yiladi

    def __str__(self):
        return self.title


class Rahbariyat(models.Model):
    LAVOZIM_TANLOV = (
        ('director', 'Direktor'),
        ('deputy', 'Direktor o‘rinbosari'),
    )

    full_name = models.CharField(max_length=200, verbose_name="F.I.Sh")
    position = models.CharField(max_length=20, choices=LAVOZIM_TANLOV, verbose_name="Lavozim turi")
    job_title = models.CharField(max_length=200, verbose_name="Lavozimi")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Telefon")
    email = models.EmailField(blank=True, verbose_name="Email")
    image = models.ImageField(upload_to='rahbariyat/', verbose_name="Rasm")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
class Oqituvchi(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="F.I.Sh")
    subject = models.CharField(max_length=200, verbose_name="Fan nomi")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Telefon")
    email = models.EmailField(blank=True, verbose_name="Email")
    image = models.ImageField(upload_to='oqituvchilar/', verbose_name="Rasm")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
