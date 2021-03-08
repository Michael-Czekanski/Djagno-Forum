from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):
    """Custom User class."""
    
    email = models.EmailField(unique=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        self._remove_old_image()
        super().save(*args, **kwargs)
        self._resize_image()

    def _remove_old_image(self):
        """Removes old profile image.

        Removes old profile image before saving newly updated profile image.
        """

        try:
            this = Profile.objects.get(pk=self.pk)
            if this.image != self.image and this.image.name != 'default.jpg':
                this.image.delete(save=False)
        except Profile.DoesNotExist:
            pass

    def _resize_image(self):
        """Checks if profile image is too big and resizes it if neccessary"""

        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
