from django.forms import ModelForm 
from django import forms 
from engine.models import SVG_POST
# from formValidationApp.models import *

# define the class of a form 
class SVGForm(ModelForm): 
	class Meta: 
		# write the name of models for which the form is made 
		model = SVG_POST		 

		# Custom fields 
		fields =["brand","slogan", "industry", "style", "font", "tag", "symbol", "color", "template"] 

	# this function will be used for the validation 
	def clean(self): 

		# data from the form is fetched using super function 
		super(SVGForm, self).clean() 
		
		# extract the username and text field from the data 
		brand = self.cleaned_data.get('brand') 
		tag = self.cleaned_data.get('tag') 

		# conditions to be met for the username length 
		if len(brand) < 3: 
			self._errors['brand'] = self.error_class([ 
				'Maximum 5 characters required']) 
		if len(tag) >100: 
			self._errors['tag'] = self.error_class([ 
				'Tag Should Contain a maximum of 100 characters']) 

		# return any errors if found 
		return self.cleaned_data 
