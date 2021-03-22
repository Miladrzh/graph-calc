from django.db import models

# Create your models here.

generator_choices = [('SNAP_RMAT', 'SNAP_RMAT')]
workload_choices = [('2HOP', '2HOP')]
ordering_choices = [('default', 'default'), ('shuffle_random', 'shuffle_random')]


class GeneratedGraph(models.Model):
    file_hash = models.CharField(max_length=16, primary_key=True)
    generate_method = models.CharField(max_length=30, choices=generator_choices, null=False)
    node_count = models.IntegerField(null=False, default=-1)
    edge_count = models.IntegerField(null=False, default=-1)
    ordering = models.CharField(max_length=30, null=False, default='default', choices=ordering_choices)
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
    # BfsFullDiam = models.IntegerField(null=False, default=-1)

    def __str__(self):
        return str(self.file_hash) + '  ,  ' + str(self.generate_method) + '  ,  ' + str(self.node_count) + '  ,  ' \
               + str(self.edge_count)


class WorkloadResult(models.Model):
    file_hash = models.ForeignKey(GeneratedGraph, on_delete=models.DO_NOTHING)
    experiment = models.CharField(max_length=30, choices=generator_choices)
    exp_num = models.IntegerField(null=False, default=-1)
    duration = models.FloatField(null=False, default=-1)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        unique_together = (('file_hash', 'experiment', 'exp_num'),)
        # constraints = [
        #     models.UniqueConstraint(fields=['file_hash_id', 'experiment', 'exp_num'])
        # ]

    def __str__(self):
        return str(self.file_hash) + ' , ' + str(self.experiment)

