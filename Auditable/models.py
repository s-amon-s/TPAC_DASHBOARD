from django.conf import settings
from django.db import models

class Auditable_Category(models.Model):
	created_on = models.DateTimeField(auto_now_add = True, null = True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='c_created_by', null = True)
	modified_on = models.DateTimeField(auto_now = True, null = True)
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='c_modified_by', null = True)

	class Meta:
		abstract = True

class Auditable_Introduction(models.Model):
	created_on = models.DateTimeField(auto_now_add = True, null = True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='i_created_by', null = True)
	modified_on = models.DateTimeField(auto_now = True, null = True)
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='i_modified_by', null = True)

	class Meta:
		abstract = True

class Auditable_Subintroduction(models.Model):
	created_on = models.DateTimeField(auto_now_add = True, null = True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='si_created_by', null = True)
	modified_on = models.DateTimeField(auto_now = True, null = True)
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='si_modified_by', null = True)

	class Meta:
		abstract = True		

class Auditable_Task(models.Model):
	created_on = models.DateTimeField(auto_now_add = True, null = True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='ts_created_by', null = True)
	modified_on = models.DateTimeField(auto_now = True, null = True)
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ts_modified_by', null = True)

	class Meta:
		abstract = True

class Auditable_Subtask(models.Model):
	created_on = models.DateTimeField(auto_now_add = True, null = True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='sts_created_by', null = True)
	modified_on = models.DateTimeField(auto_now = True, null = True)
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sts_modified_by', null = True)

	class Meta:
		abstract = True				

class Auditable_Troubleshoot(models.Model):
	created_on = models.DateTimeField(auto_now_add = True, null = True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='tr_created_by', null = True)
	modified_on = models.DateTimeField(auto_now = True, null = True)
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tr_modified_by', null = True)

	class Meta:
		abstract = True

class Auditable_Subtroubleshoot(models.Model):
	created_on = models.DateTimeField(auto_now_add = True, null = True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='str_created_by', null = True)
	modified_on = models.DateTimeField(auto_now = True, null = True)
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='str_modified_by', null = True)

	class Meta:
		abstract = True					

class Auditable_Fpe(models.Model):
	created_on = models.DateTimeField(auto_now_add = True, null = True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='fpe_created_by', null = True)
	modified_on = models.DateTimeField(auto_now = True, null = True)
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='fpe_modified_by', null = True)

	class Meta:
		abstract = True		

class Auditable_Worklocation(models.Model):
	created_on = models.DateTimeField(auto_now_add = True, null = True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='worklocation_created_by', null = True)
	modified_on = models.DateTimeField(auto_now = True, null = True)
	modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='worklocation_modified_by', null = True)

	class Meta:
		abstract = True		