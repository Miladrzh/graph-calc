from django.db import models

# Create your models here.

generator_choices = [('SNAP_RMAT', 'SNAP_RMAT')]

class GeneratedGraph(models.Model):
    file_hash = models.CharField(max_length=16, primary_key=True)
    generate_method = models.CharField(max_length=30, choices=generator_choices, null=False)
    node_count = models.IntegerField(null=False, default=-1)
    edge_count = models.IntegerField(null=False, default=-1)
    OutDegCnt_mean = models.FloatField(null=False, default=-1)
    OutDegCnt_std = models.FloatField(null=False, default=-1)
    OutDegCnt_var = models.FloatField(null=False, default=-1)
    InDegCnt_mean = models.FloatField(null=False, default=-1)
    InDegCnt_std = models.FloatField(null=False, default=-1)
    InDegCnt_var = models.FloatField(null=False, default=-1)
    WccSzCnt_mean = models.FloatField(null=False, default=-1)
    WccSzCnt_std = models.FloatField(null=False, default=-1)
    WccSzCnt_var = models.FloatField(null=False, default=-1)
    n_triads = models.IntegerField(null=False, default=-1)
    clust_coef = models.FloatField(null=False, default=-1)

    def __str__(self):
        return str(self.file_hash) + '  ,  ' + str(self.generate_method) + '  ,  ' + str(self.node_count) + '  ,  ' \
               + str(self.edge_count)
