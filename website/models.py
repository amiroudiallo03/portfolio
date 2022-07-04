from tkinter import N
from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Website(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    photoProfil = models.FileField(upload_to="website_file")
    photoCouverture = models.FileField(upload_to="website_file")
    telephone = models.CharField(max_length=255)
    email = models.EmailField()
    adresse = models.CharField(max_length=255)
    localisation = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Site Webs"

    def __str__(self):
        return self.nom


class Configuration(models.Model):
    descriptionAPropos = models.TextField()
    descriptionFait = models.TextField()
    descriptionCompetence = models.TextField()
    descriptionResume = models.TextField()
    descriptionDiplome = models.TextField(blank=True, null=True)
    descriptionPortfolio = models.TextField()
    descriptionService = models.TextField()
    descriptionTemoignage = models.TextField()
    descriptionContact = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Configurations"

    def __str__(self):
        return f"{self.descriptionAPropos}"


class Apropos(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    option = models.ManyToManyField(
        "website.Optionapropos", related_name="detailApropos"
    )
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "A Propos"

    def __str__(self):
        return self.titre


class Optionapropos(models.Model):
    titre = models.CharField(max_length=255)
    information = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Options A Propos"

    def __str__(self):
        return self.titre


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    sujet = models.CharField(max_length=255)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.nom


class Travail(models.Model):
    liste = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Travails"

    def __str__(self):
        return self.liste


class Resume(models.Model):
    titre = models.CharField(max_length=255)
    option = models.ManyToManyField("website.Optionresume", related_name="optionResume")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Résumes"

    def __str__(self):
        return self.titre


class Optionresume(models.Model):
    titre = models.CharField(max_length=255)
    nomStructure = models.CharField(max_length=255)
    periode = models.CharField(max_length=255)
    description = HTMLField(blank=True, null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Options Résumes"
        ordering = ['-date_add']

    def __str__(self):
        return self.titre


class Competence(models.Model):
    titre = models.CharField(max_length=255)
    pourcentage = models.IntegerField(default=0)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Compétences"

    def __str__(self):
        return self.titre


class Certificat(models.Model):
    titre = models.CharField(max_length=255)
    image = models.FileField(upload_to="Certificat_file")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Certificats"

    def __str__(self):
        return self.titre


class Socialicone(models.Model):
    nom = models.CharField(max_length=255)
    icone = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Icones Réseaux Sociaux"

    def __str__(self):
        return self.nom


class Reseauxsocial(models.Model):
    lien = models.CharField(max_length=255)
    sociaux = models.ForeignKey(
        "website.Socialicone", related_name="social_icon", on_delete=models.CASCADE
    )
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Réseaux Sociaux"

    def __str__(self):
        return self.lien


class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.nom


class Imageprojet(models.Model):
    image = models.FileField(upload_to="Imageprojet_file")
    projet = models.ForeignKey(
        "Projet", related_name="imageProjet", on_delete=models.CASCADE
    )
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Image De Projets"

    def __str__(self):
        return f"{self.image}"


class Projet(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to="Projet_file")
    url = models.URLField(null=True, blank=True)
    dateProjet = models.DateField()
    client = models.CharField(max_length=255)
    categorie = models.ForeignKey(
        "Categorie", related_name="categorieProjet", on_delete=models.CASCADE
    )
    technologie = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.nom


class Fait(models.Model):
    titre = models.CharField(max_length=255)
    nombre = models.IntegerField(default=0)
    icone = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Faits"

    def __str__(self):
        return self.titre


class Temoignage(models.Model):
    nom = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    photo = models.FileField(upload_to="Temoignage_file")
    temoignage = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Témoignages"

    def __str__(self):
        return self.nom


class Service(models.Model):
    titre = models.CharField(max_length=255)
    icone = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.titre