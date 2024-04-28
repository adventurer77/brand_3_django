from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    icon_class = models.CharField(max_length=50, blank=True, null=True)  
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["sort"]

    def __str__(self):
        return self.title
    

class About(models.Model):
    date_heading = models.CharField(max_length=255)
    subheading = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="about/",blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Timeline "
        verbose_name_plural = "All Timeline"
        ordering = ["sort"]

    def __str__(self):
        return f"{self.date_heading} - {self.subheading}"
    

class Team(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/',blank=True, null=True)  
    social_media_links = models.JSONField(blank=True, default=dict)  
    sort = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Team"
        ordering = ["sort"]
    
    def __str__(self):
        return self.name
    

class Clients(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    image = models.ImageField(upload_to="clients/",blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['name']



# class Portfolio(models.Model):
#   title = models.CharField(max_length=255)
#   subheading = models.CharField(max_length=255, blank=True)
#   description = models.TextField()
#   image_title = models.ImageField(upload_to='portfolio/title/',blank=True, null=True)
#   image_full = models.ImageField(upload_to='portfolio/full/',blank=True, null=True)
#   date = models.CharField(max_length=255, blank=True)
#   client = models.CharField(max_length=255, blank=True)
#   category = models.CharField(max_length=255, blank=True)
#   is_visible = models.BooleanField(default=True)
#   sort = models.PositiveSmallIntegerField()

#   class Meta:
#         verbose_name = "Portfolio"
#         verbose_name_plural = "Portfolio"
#         ordering = ['sort']

#   def __str__(self):
#     return self.title

class Portfolio(models.Model):
  title = models.CharField(max_length=255)
  subheading = models.CharField(max_length=255, blank=True)
  image_title = models.ImageField(upload_to='portfolio/title/',blank=True, null=True)
  is_visible = models.BooleanField(default=True)
  sort = models.PositiveSmallIntegerField()

  def __str__(self):
        return self.title
  
  def __iter__(self):
        for item in self.portfolios.all(): # V3
            yield item
  
  class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"
        ordering = ['sort']


class PortfolioFilling(models.Model):

    title = models.CharField(max_length=255)
    subheading = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    image_full = models.ImageField(upload_to='portfolio/full/',blank=True, null=True)
    date = models.CharField(max_length=255, blank=True)
    client = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="portfolios")
    

    class Meta:
        verbose_name = "Info"
        verbose_name_plural = "Portfolio Filling"
        ordering = ['title']

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    phone_regex = RegexValidator(regex=r"^\+?(380)?\d{9,15}$",
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, validators=[phone_regex])
    comment = models.TextField(blank=True, null=True)
    
    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ["-date_created"]