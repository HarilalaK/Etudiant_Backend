from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()

class Cours(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    etudiants = models.ManyToManyField(Etudiant, related_name='cours')

class Professeur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cours = models.ForeignKey(Cours, related_name='professeur', on_delete=models.CASCADE)