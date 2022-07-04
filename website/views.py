from urllib import request
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from . import models

# Create your views here.


def index(request):
    websites = models.Website.objects.filter(status=True).first()
    configuration = models.Configuration.objects.filter(status=True).first()
    apropos = models.Apropos.objects.filter(status=True).first()
    travaux = models.Travail.objects.filter(status=True)
    sociaux = models.Reseauxsocial.objects.filter(status=True)
    certificats = models.Certificat.objects.filter(status=True)
    resumes = models.Resume.objects.filter(status=True).order_by('-date_add')
    competences = models.Competence.objects.filter(status=True)

    categories = models.Categorie.objects.filter(status=True)
    imageprojets = models.Imageprojet.objects.filter(status=True)
    projets = models.Projet.objects.filter(status=True)
    faits = models.Fait.objects.filter(status=True)
    temoignages = models.Temoignage.objects.filter(status=True)
    services = models.Service.objects.filter(status=True)

    return render(request,'index.html',locals())



def portfoliodetail(request, id_projet):
    projet = get_object_or_404(models.Projet, id=id_projet)
    return render(request, "portfolio-details", locals())
