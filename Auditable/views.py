from django.shortcuts import render
from IT_Dashboard.models import Userdetail

# Create your views here.
modified_sub_score = 1
modified_score = 2
created_sub_score = 3
created_score = 5

class AuditableCategoryMixin(object,):
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
            user = Userdetail.objects.get(pk=self.request.user.id)
            user.credit+=created_score
            user.save()
        form.instance.modified_by = self.request.user
        user = Userdetail.objects.get(pk=self.request.user.id)
        user.credit+=modified_score
        user.save()
        return super(AuditableCategoryMixin, self).form_valid(form)

class AuditableIntroductionMixin(object,):
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
            user = Userdetail.objects.get(pk=self.request.user.id)
            user.credit+=created_score
            user.save()
        form.instance.modified_by = self.request.user
        user = Userdetail.objects.get(pk=self.request.user.id)
        user.credit+=modified_score
        user.save()
        return super(AuditableIntroductionMixin, self).form_valid(form)        
class AuditableSubintroductionMixin(object,):
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
            user = Userdetail.objects.get(pk=self.request.user.id)
            user.credit+=created_sub_score
            user.save()
        form.instance.modified_by = self.request.user
        user = Userdetail.objects.get(pk=self.request.user.id)
        user.credit+=modified_sub_score
        user.save()
        return super(AuditableSubintroductionMixin, self).form_valid(form)

class AuditableTaskMixin(object,):
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
            user = Userdetail.objects.get(pk=self.request.user.id)
            user.credit+=created_score
            user.save()
        form.instance.modified_by = self.request.user
        user = Userdetail.objects.get(pk=self.request.user.id)
        user.credit+=modified_score
        user.save()
        return super(AuditableTaskMixin, self).form_valid(form)                
class AuditableSubtaskMixin(object,):
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
            user = Userdetail.objects.get(pk=self.request.user.id)
            user.credit+=created_sub_score
            user.save()
        form.instance.modified_by = self.request.user
        user = Userdetail.objects.get(pk=self.request.user.id)
        user.credit+=modified_sub_score
        user.save()
        return super(AuditableSubtaskMixin, self).form_valid(form)        

class AuditableTroubleshootMixin(object,):
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
            user = Userdetail.objects.get(pk=self.request.user.id)
            user.credit+=created_score
            user.save()
        form.instance.modified_by = self.request.user
        user = Userdetail.objects.get(pk=self.request.user.id)
        user.credit+=modified_score
        user.save()
        return super(AuditableTroubleshootMixin, self).form_valid(form)   

class AuditableSubtroubleshootMixin(object,):
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
            user = Userdetail.objects.get(pk=self.request.user.id)
            user.credit+=created_sub_score
            user.save()
        form.instance.modified_by = self.request.user
        user = Userdetail.objects.get(pk=self.request.user.id)
        user.credit+=modified_sub_score
        user.save()
        return super(AuditableSubtroubleshootMixin, self).form_valid(form)
        
class AuditableFpeMixin(object,):
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(AuditableFpeMixin, self).form_valid(form)                

class AuditableWorklocationMixin(object,):
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(AuditableWorklocationMixin, self).form_valid(form)                