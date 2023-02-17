from 

class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
