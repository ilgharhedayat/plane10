from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class SiteSetting(SingletonModel):
    title = models.CharField(max_length=125, verbose_name="عنوان سایت")
    logo = models.ImageField(upload_to='', verbose_name="لوگو")
    address = models.CharField(max_length=500, verbose_name="آدرس")
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    instagram = models.URLField(verbose_name="اینستاگرام", blank=True)
    linkedin = models.URLField(verbose_name="لینکدین", blank=True)
    twitter = models.URLField(verbose_name="واتساپ", blank=True)
    facebook = models.URLField(verbose_name='فیس بوک', blank=True)
    copyrights = models.CharField(max_length=500, verbose_name="کپی رایت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تنظیمات سایت'


class AboutUs(SingletonModel):
    title = models.CharField(max_length=255)
    description = models.TextField()


class ContactUs(models.Model):
    TITLE = (
        ('', ''),
    )
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    title = models.CharField(max_length=15)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
