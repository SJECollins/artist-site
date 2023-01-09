from django.db import models


class Collection(models.Model):
    collection_name = models.CharField(max_length=280)
    slug = models.CharField(max_length=140)
    year = models.PositiveIntegerField(null=True, blank=True)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ('collection_name',)

    def __str__(self):
        return self.collection_name


class Piece(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True)
    piece_name = models.CharField(max_length=280)
    slug = models.CharField(max_length=140)
    size = models.CharField(max_length=140, null=True, blank=True)
    price = models.models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='uploads/', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        ordering = ('collection',)

    def __str__(self):
        return self.piece_name

    def get_image(self):
        if self.image:
            return 'https://8000-sjecollins-artistsite-qk15k8czxo7.ws-eu81.gitpod.io/' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'https://8000-sjecollins-artistsite-qk15k8czxo7.ws-eu81.gitpod.io/' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'https://8000-sjecollins-artistsite-qk15k8czxo7.ws-eu81.gitpod.io/' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
