from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist


class HitCount(models.Model):
	try:
		created = models.DateTimeField(_('Created'), auto_now_add=True, editable=False)
		modified = models.DateTimeField(_('Modified'), auto_now=True, editable=False)
		url = models.CharField(_('URL'), max_length=2000)
		hits = models.PositiveIntegerField(_('Hits'), default=0)

	except ObjectDoesNotExist:
		print("problem with an expected db column(s)")


	class Meta:
		ordering = ('-created', '-modified')
		get_latest_by = 'created'
