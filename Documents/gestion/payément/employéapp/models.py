from django.db import models
class Personne(models.Model):
    Status = (
    ('Ancien', ('ancien')),
    ('Nouveau', ('nouveau')),
    ('Autre', ('autre')),
    )
    Genre = (
    ('M', ('masculin')),
    ('F', ('feminin')),
    ('Autre', ('autre')),
    )
    nom = models.CharField(max_length=200)
    naissance = models.DateTimeField('date de naisssance')
    genre = models.CharField(max_length=32, choices=Genre)
    status = models.CharField(max_length=32, choices=Status)
    nationalite = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="photo",blank=True)
    poste = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Employé(Personne):
    matricule = models.CharField(max_length=20,unique=True)
    service = models.CharField(max_length=100)
    contrat = models.FloatField(max_length=15,blank=True)

    def __str__(self):
        return self.matricule

class Adresse(models.Model):
    telephone = models.CharField(max_length=20,blank=True,unique=True)
    email = models.CharField(max_length=250,unique=True)
    quartier = models.CharField(max_length=150)
    ville = models.CharField(max_length=150)
    def __str__(self):
        return self.email

class Gestionnaire(Personne):
    matricule = models.CharField(max_length=20,unique=True)
    grade = models.CharField(max_length=20,unique=True)


    def __str__(self):
        return self.matricule

class Reçu_payément(models.Model):
    date=models.DateTimeField('date de naisssance')
    montant=models.CharField(max_length=200)
    reste=models.CharField(max_length=200)
    numero=models.CharField(max_length=120)
    employé = models.ForeignKey(Employé, on_delete=models.CASCADE)

    def __str__(self):
        return self.montant

class Banque(models.Model):
    nom=models.CharField(max_length=150)
    montant=models.CharField(max_length=200)
    validation= models.FloatField(max_length=15,blank=True)

    def __str__(self):
        return self.nom

