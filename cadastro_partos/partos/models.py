from django.db import models

class Parto(models.Model):
    BRINCO_CHOICES = [(str(i), str(i)) for i in range(10000)]  # Substitua conforme necessário
    SEXO_CHOICES = [('Ab', 'Aborto'), ('Na', 'Natimorto'), ('M', 'Macho'), ('F', 'Fêmea')]
    TIPO_CHOICES = [('S', 'Simples'), ('D', 'Duplo'), ('T', 'Três ou Mais')]

    brinco = models.CharField(max_length=10, choices=BRINCO_CHOICES)
    data_prov = models.DateField('Data Provável')
    data = models.DateField('Data')
    ecc = models.CharField('ECC', max_length=10)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)

    sexo_cria1 = models.CharField(max_length=2, choices=SEXO_CHOICES)
    peso_cria1 = models.DecimalField(max_digits=5, decimal_places=2)
    
    sexo_cria2 = models.CharField(max_length=2, choices=SEXO_CHOICES, blank=True, null=True)
    peso_cria2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    sexo_cria3 = models.CharField(max_length=2, choices=SEXO_CHOICES, blank=True, null=True)
    peso_cria3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    sexo_cria4 = models.CharField(max_length=2, choices=SEXO_CHOICES, blank=True, null=True)
    peso_cria4 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    manejo = models.TextField('Manejo', blank=True, null=True)

    def __str__(self):
        return f"Brinco: {self.brinco} - Data: {self.data}"