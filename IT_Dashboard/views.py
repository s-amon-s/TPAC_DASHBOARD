from django.views import generic
from django.views.generic.edit import  CreateView,UpdateView,DeleteView
from django.http import HttpResponse		
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Category,Introduction,Subintroduction,Task,Subtask,Troubleshoot,Subtroubleshoot,Userdetail
from .forms import UserForm,ProfileForm,CategoryForm,IntroductionForm,SubintroductionForm,TaskForm,SubtaskForm,TroubleshootForm,SubtroubleshootForm,FpeForm
from Auditable.views import AuditableCategoryMixin,AuditableIntroductionMixin,AuditableSubintroductionMixin,AuditableTaskMixin,AuditableSubtaskMixin,AuditableTroubleshootMixin,AuditableSubtroubleshootMixin
from django.db.models import Avg,Sum
import reversion
from django.core import serializers

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def index(request):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				context = { "profile" : profile,"category":Category.objects.all()}
				return render(request,'IT_Dashboard/dashboard.html', context)
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')

#################################################################################################################### 
#											Login Registration Logic     										   #
#################################################################################################################### 

class LoginFormView(View):
	form_class = UserForm
	template_name = 'IT_Dashboard/login_registration.html'
	title = "Login / Register"
	# display a blank form

	def get(self, request):
		if not request.user.is_authenticated():
			form = self.form_class(None)
			return render(request,self.template_name,{'form':form,"title":"Login / Register"})
		else:
			return redirect('it:index')

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect('it:index')
			else:
				return HttpResponse("Your Account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return render(request,self.template_name,{"error_message":'Invalid login detail'})

class register_view(View):
	form_class = UserForm
	template_name = 'IT_Dashboard/addUser.html'
	# display a blank form
	def get(self, request):
		if request.user.is_authenticated():
			redirect('it:index')
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form,"title":"Login / Register"})


	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			# save locally
			user = form.save(commit=False)
			# normalize data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)	
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']	
			user.save()

			#returns User objects if credenctials are correct
			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('it:index')


		return render(request,self.template_name,{'form':form})

def user_logout(request):
	if request.user.is_authenticated():
		logout(request)
	return redirect('it:index')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse_lazy('it:login'))
        else:
            return redirect(reverse_lazy('it:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'IT_Dashboard/password_change.html', args)

#################################################################################################################### 
#											Profile Related Logic 												   #
#################################################################################################################### 
class ProfileCreate(CreateView):
	model = Userdetail
	form_class = ProfileForm

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
				if request.user.userdetail:
					return render(request,'IT_Dashboard/already_have_profile.html')
			except Exception as e:
				return super(ProfileCreate, self).dispatch(request, *args, **kwargs)
		else:
			return render(request,'IT_Dashboard/not_loggedIn.html')
	# fields =  ['user','id','full_name','ip','table','organization','department','designation','level','permission','is_under','work_at','joined_tpac','personal_contact','house_location','likes_to_play','likes_to_eat','is_incharge_of','is_responsible_to','nickname','birthday','selfie']

class ProfileUpdate(UpdateView):
	model = Userdetail
	form_class = ProfileForm
	# fields =  ['user','id','full_name','ip','table','organization','department','designation','level','permission','is_under','work_at','joined_tpac','personal_contact','house_location','likes_to_play','likes_to_eat','is_incharge_of','is_responsible_to','nickname','birthday','selfie']
	def get_queryset(self):
		base_qs = super(ProfileUpdate, self).get_queryset()
		return base_qs.filter(user=self.request.user)

class ProfileDelete(DeleteView):
	model = Userdetail
	form_class = ProfileForm
	success_url = reverse_lazy('it:index')
		
	def get_queryset(self):
		base_qs = super(ProfileDelete, self).get_queryset()
		return base_qs.filter(user=self.request.user)


def group_flow(request):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				context = { "profile" : profile,"category":Category.objects.all()}
				return render(request,'IT_Dashboard/extras/group_tasks_workflow_econsUse.html', context)
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')		

#################################################################################################################### 
#											Category Related Logic 												   #
#################################################################################################################### 
class CategoryCreate(AuditableCategoryMixin,CreateView):
	model = Category
	form_class = CategoryForm
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
				if request.user.userdetail:
					return super(CategoryCreate , self).dispatch(request, *args, **kwargs)
			except Exception as e:
				return redirect('it:profile-add')
		else:
			return render(request,'IT_Dashboard/not_loggedIn.html')	
			
class CategoryUpdate(AuditableCategoryMixin,UpdateView):
	model = Category
	form_class = CategoryForm
	def get_queryset(self):
		base_qs = super(CategoryUpdate, self).get_queryset()
		return base_qs.filter(user=self.request.user)

class CategoryDelete(AuditableCategoryMixin,DeleteView):
	model = Category
	form_class = CategoryForm
	success_url = reverse_lazy('it:index')
		
	def get_queryset(self):
		base_qs = super(CategoryDelete, self).get_queryset()
		return base_qs.filter(user=self.request.user)

def CategoryLanding(request,cid):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				context = { "profile" : profile,"category":Category.objects.get(pk=cid),"categorys":Category.objects.all()}
				return render(request,'IT_Dashboard/category_menu.html', context)
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')


#################################################################################################################### 
#											FPE-100 foRM Related Logic 											   #
#################################################################################################################### 
# class FpeCreate(AuditableFpeMixin,CreateView):
# 	model = Fpe
# 	form_class = FpeForm
# 	def dispatch(self, request, *args, **kwargs):
# 		if request.user.is_authenticated():
# 			try:
# 				if request.user.userdetail:
# 					return super(FpeCreate , self).dispatch(request, *args, **kwargs)
# 			except Exception as e:
# 				return redirect('it:profile-add')
# 		else:
# 			return render(request,'IT_Dashboard/not_loggedIn.html')	
			
# class FpeUpdate(AuditableFpeMixin,UpdateView):
# 	model = Fpe
# 	form_class = FpeForm
# 	def get_queryset(self):
# 		base_qs = super(FpeUpdate, self).get_queryset()
# 		return base_qs.filter(user=self.request.user)

# class FpeDelete(AuditableFpeMixin,DeleteView):
# 	model = Fpe
# 	form_class = FpeForm
# 	success_url = reverse_lazy('it:index')
		
# 	def get_queryset(self):
# 		base_qs = super(FpeDelete, self).get_queryset()
# 		return base_qs.filter(user=self.request.user)

# def FpeLanding(request,cid):
# 	if request.user.is_authenticated():
# 		try:
# 			if request.user.userdetail:
# 				profile = Userdetail.objects.get(pk=request.user.pk)
# 				context = { "profile" : profile,"category":Category.objects.get(pk=cid),"categorys":Category.objects.all()}
# 				return render(request,'IT_Dashboard/category_menu.html', context)
# 		except Exception as e:
# 			return redirect('it:profile-add')
# 	else:
# 		return redirect('it:login')



#################################################################################################################### 
#											Introduction Related Logic 											   #
#################################################################################################################### 
class IntroductionCreate(AuditableIntroductionMixin,CreateView):
	model = Introduction
	form_class = IntroductionForm
	
			
class IntroductionUpdate(AuditableIntroductionMixin,UpdateView):
	model = Introduction
	form_class = IntroductionForm
	def get_queryset(self):
		base_qs = super(IntroductionUpdate, self).get_queryset()
		return base_qs.filter(user=self.request.user)

class IntroductionDelete(AuditableIntroductionMixin,DeleteView):
	model = Introduction
	form_class = IntroductionForm
	success_url = reverse_lazy('it:index')
		
	def get_queryset(self):
		base_qs = super(IntroductionDelete, self).get_queryset()
		return base_qs.filter(user=self.request.user)

def IntroductionLanding(request,cid):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				category = Category.objects.get(pk=cid)
				context = { "profile" : profile,"category":category,"categorys":Category.objects.all(),"menuID":'introduction'}
				return render(request,'IT_Dashboard/menu_content.html', context)
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')


#                                   **********************************
#										Detail Page of introduction
#                                   **********************************

def IntroDetail(request,iid):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				introduction = Introduction.objects.get(pk=iid)
				context = { "profile" : profile,"category":Category.objects.all(),"introduction":introduction}
				return render(request,'IT_Dashboard/content_detail.html', context)
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')		

#                                   **********************************
#											Sub-Introduction Page 
#                                   **********************************

class SubIntroductionCreate(AuditableSubintroductionMixin,CreateView):
	model = Subintroduction
	form_class = SubintroductionForm
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
				if request.user.userdetail:
					return super(SubIntroductionCreate , self).dispatch(request, *args, **kwargs)
			except Exception as e:
				return redirect('it:profile-add')
		else:
			return render(request,'IT_Dashboard/not_loggedIn.html')	
			
class SubIntroductionUpdate(AuditableSubintroductionMixin,UpdateView):
	model = Subintroduction
	form_class = SubintroductionForm
	def get_queryset(self):
		base_qs = super(SubIntroductionUpdate, self).get_queryset()
		return base_qs.filter(user=self.request.user)

class SubIntroductionDelete(AuditableSubintroductionMixin,DeleteView):
	model = Subintroduction
	form_class = SubintroductionForm
	success_url = reverse_lazy('it:index')
		
	def get_queryset(self):
		base_qs = super(SubIntroductionDelete, self).get_queryset()
		return base_qs.filter(user=self.request.user)


####################################################################################################################
#										   Task Related Logic   												   #
####################################################################################################################
class TaskCreate(AuditableTaskMixin,CreateView):
	model = Task
	form_class = TaskForm
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
				if request.user.userdetail:
					return super(TaskCreate , self).dispatch(request, *args, **kwargs)
			except Exception as e:
				return redirect('it:profile-add')
		else:
			return render(request,'IT_Dashboard/not_loggedIn.html')	
			
class TaskUpdate(AuditableTaskMixin,UpdateView):
	model = Task
	form_class = TaskForm
	def get_queryset(self):
		base_qs = super(TaskUpdate, self).get_queryset()
		return base_qs.filter(user=self.request.user)

class TaskDelete(AuditableTaskMixin,DeleteView):
	model = Task
	form_class = TaskForm
	success_url = reverse_lazy('it:index')
		
	def get_queryset(self):
		base_qs = super(TaskDelete, self).get_queryset()
		return base_qs.filter(user=self.request.user)

def TaskLanding(request,cid):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				category = Category.objects.get(pk=cid)
				context = { "profile" : profile,"category":category,"categorys":Category.objects.all(),"menuID":'task'}
				return render(request,'IT_Dashboard/menu_content.html', context)
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')

def TaskDetail(request,cid,tid):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				context = { "profile" : profile,"category":Category.objects.all()}
				return render(request,'IT_Dashboard/dashboard.html', context)
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')		

class SubTaskCreate(AuditableSubtaskMixin,CreateView):
	model = Subtask
	form_class = SubtaskForm
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
				if request.user.userdetail:
					return super(SubTaskCreate , self).dispatch(request, *args, **kwargs)
			except Exception as e:
				return redirect('it:profile-add')
		else:
			return render(request,'IT_Dashboard/not_loggedIn.html')	
			
class SubTaskUpdate(AuditableTaskMixin,UpdateView):
	model = Subtask
	form_class = SubtaskForm
	def get_queryset(self):
		base_qs = super(SubTaskUpdate, self).get_queryset()
		return base_qs.filter(user=self.request.user)

class SubTaskDelete(AuditableTaskMixin,DeleteView):
	model = Subtask
	form_class = SubtaskForm
	success_url = reverse_lazy('it:index')
		
	def get_queryset(self):
		base_qs = super(SubTaskDelete, self).get_queryset()
		return base_qs.filter(user=self.request.user)


#################################################################################################################### 
#											Troubleshoot Related Logic 											   #
#################################################################################################################### 
class TroubleshootCreate(AuditableTroubleshootMixin,CreateView):
	model = Troubleshoot
	form_class = TroubleshootForm
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
				if request.user.userdetail:
					return super(TroubleshootCreate , self).dispatch(request, *args, **kwargs)
			except Exception as e:
				return redirect('it:profile-add')
		else:
			return render(request,'IT_Dashboard/not_loggedIn.html')	
			
class TroubleshootUpdate(AuditableTroubleshootMixin,UpdateView):
	model = Troubleshoot
	form_class = TroubleshootForm
	def get_queryset(self):
		base_qs = super(TroubleshootUpdate, self).get_queryset()
		return base_qs.filter(user=self.request.user)

class TroubleshootDelete(AuditableTroubleshootMixin,DeleteView):
	model = Troubleshoot
	form_class = TroubleshootForm
	success_url = reverse_lazy('it:index')
		
	def get_queryset(self):
		base_qs = super(TroubleshootDelete, self).get_queryset()
		return base_qs.filter(user=self.request.user)

def TroubleshootLanding(request,cid):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				category = Category.objects.get(pk=cid)
				context = { "profile" : profile,"category":category,"categorys":Category.objects.all(),"menuID":'troubleshoot'}
				return render(request,'IT_Dashboard/menu_content.html', context)
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')

def TroubleDetail(request,cid,tid):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				context = { "profile" : profile,"category":Category.objects.all()}
				return render(request,'IT_Dashboard/dashboard.html', context)
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')		

class SubTroubleshootCreate(AuditableSubtroubleshootMixin,CreateView):
	model = Subtroubleshoot
	form_class = SubtroubleshootForm
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
				if request.user.userdetail:
					return super(SubTroubleshootCreate , self).dispatch(request, *args, **kwargs)
			except Exception as e:
				return redirect('it:profile-add')
		else:
			return render(request,'IT_Dashboard/not_loggedIn.html')	
			
class SubTroubleshootUpdate(AuditableSubtroubleshootMixin,UpdateView):
	model = Subtroubleshoot
	form_class = SubtroubleshootForm
	def get_queryset(self):
		base_qs = super(SubTroubleshootUpdate, self).get_queryset()
		return base_qs.filter(user=self.request.user)

class SubTroubleshootDelete(AuditableSubtroubleshootMixin,DeleteView):
	model = Subtroubleshoot
	form_class = SubtroubleshootForm
	success_url = reverse_lazy('it:index')
		
	def get_queryset(self):
		base_qs = super(SubTroubleshootDelete, self).get_queryset()
		return base_qs.filter(user=self.request.user)
####################################################################################################################
class ContactListView(generic.ListView):
	template_name = 'IT_Dashboard/extras/contacts.html'
	context_object_name = 'users'
	def get_queryset(self):
		context = Userdetail.objects.all()
		return context
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
				if request.user.userdetail:
					return super(ContactListView , self).dispatch(request, *args, **kwargs)
			except Exception as e:
				return redirect('it:profile-add')
		else:
			return render(request,'IT_Dashboard/not_loggedIn.html')	

class ContactDetailView(generic.DetailView):
	model = Userdetail
	template_name = 'IT_Dashboard/extras/contacts_detail.html'
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
				if request.user.is_superuser or int(request.user.pk) == int(self.kwargs['pk']):
					return super(ContactDetailView , self).dispatch(request, *args, **kwargs)
				else:
					return render(request,'IT_Dashboard/requires_admin.html')
			except Exception as e:
				return redirect('it:profile-add')
		else:
			return render(request,'IT_Dashboard/not_loggedIn.html')		


def aidedMaps(request):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				context = { "profile" : profile,"category":Category.objects.all()}
				return render(request,'IT_Dashboard/extras/google_maps.html',context)	
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')

def aidedTimeline(request):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				context = { "profile" : profile,"category":Category.objects.all()}
				return render(request,'IT_Dashboard/extras/timeline.html',context)	
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')
		
def aidedTimeline2(request):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				context = { "profile" : profile,"category":Category.objects.all(),"users":Userdetail.objects.order_by('joined_tpac')}
				return render(request,'IT_Dashboard/extras/timeline_2.html',context)	
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')

def aidedTimeline(request):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				context = { "profile" : profile,"category":Category.objects.all()}
				return render(request,'IT_Dashboard/extras/timeline.html',context)	
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')				


def aidedGraphChart(request):
	profile = Userdetail.objects.get(pk=request.user.pk)
	context = { "profile" : profile,"category":Category.objects.all()}
	return render(request,'IT_Dashboard/extras/graph_chartjs.html')

def aidedGraphFlot(request):
	profile = Userdetail.objects.get(pk=request.user.pk)
	context = { "profile" : profile,"category":Category.objects.all()}
	return render(request,'IT_Dashboard/extras/graph_flot.html')

def aidedGraphMorris(request):
	profile = Userdetail.objects.get(pk=request.user.pk)
	context = { "profile" : profile,"category":Category.objects.all()}
	return render(request,'IT_Dashboard/extras/graph_morris.html')

def aidedGraphPeity(request):
	profile = Userdetail.objects.get(pk=request.user.pk)
	context = { "profile" : profile,"category":Category.objects.all()}
	return render(request,'IT_Dashboard/extras/graph_peity.html')

def aidedGraphRickshaw(request):
	profile = Userdetail.objects.get(pk=request.user.pk)
	context = { "profile" : profile,"category":Category.objects.all()}
	return render(request,'IT_Dashboard/extras/graph_rickshaw.html')

def aidedGraphSparkline(request):
	profile = Userdetail.objects.get(pk=request.user.pk)
	context = { "profile" : profile,"category":Category.objects.all()}
	return render(request,'IT_Dashboard/extras/graph_sparkline.html')

def ContentDetail(request):
	if request.user.is_authenticated():
		try:
			if request.user.userdetail:
				profile = Userdetail.objects.get(pk=request.user.pk)
				context = { "profile" : profile,"category":Category.objects.all()}
				return render(request,'IT_Dashboard/content_timeline.html', context)
		except Exception as e:
			return redirect('it:profile-add')
	else:
		return redirect('it:login')	

def getUserContent(request):
	profile = Userdetail.objects.all()
	return HttpResponse(serializers.serialize("json", profile), content_type='application/json')

def getIntroductionContent(request,cid):
	introduction_set = Category.objects.get(pk=cid).introduction_set.all()
	return HttpResponse(serializers.serialize("json", introduction_set), content_type='application/json')
def getTroubleshootContent(request,cid):
	troubleshoot_set = Category.objects.get(pk=cid).troubleshoot_set.all()
	return HttpResponse(serializers.serialize("json", troubleshoot_set), content_type='application/json')
def getTaskContent(request,cid):
	task_set = Category.objects.get(pk=cid).task_set.all()
	return HttpResponse(serializers.serialize("json", task_set), content_type='application/json')
def getUserById(request,uid):
	return HttpResponse(Userdetail.objects.get(pk=uid).fullname)

# class ProductDelete(DeleteView):
# 	model = Product
# 	fields = ['prodcuctName','price','quntity','prodcuct_describtion','best_before','product_logo','sellers','product_list']
# 	success_url = reverse_lazy('seller:index')
# 	