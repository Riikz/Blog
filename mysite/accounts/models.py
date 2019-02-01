from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
from django.core.mail import send_mail
from django.template.loader import get_template
from blog.models import Blog


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	follow = models.ManyToManyField(User, related_name='owner')
	followers = models.ManyToManyField(User, related_name='followers')
	profile_image = models.ImageField(default='default.png', upload_to='profile_pics')
	subscribe = models.ManyToManyField(User, related_name='subscribed')

	def __str__(self):
		return self.user.username

	def save(self, **kwargs):
		super().save()

		img = Image.open(self.profile_image.path)

		if img.height > 250 or img.width > 250:
			output_size = (250, 250)
			img.thumbnail(output_size)
			img.save(self.profile_image.path)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.userprofile.save()


@receiver(post_save, sender=Blog)
def send_email(sender, instance, created, **kwargs):
	if created:
		user = instance.author
		subscribers = user.userprofile.subscribe.all()
		context = {
			'author': instance.author,
			'title': instance.blog_title,
		}

		contact_message = get_template('accounts/contact_message.txt').render(context)
		subject = 'New Post on EPC'
		from_email = user.email
		for user1 in subscribers:
			to_email = [user1.email]
			send_mail(subject, contact_message, from_email, to_email)




