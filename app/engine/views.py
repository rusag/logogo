from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import *
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .models import SVG_POST, SVG_FILE
from .forms import SVGForm
from .build_svg import SVG_LOGOGO
from cairosvg import svg2png
from django.urls import reverse


import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def home(request): 

	# check if the request is post
	svg_url = ''
	if request.method =='POST': 

		# Pass the form data to the form class
		logger.error("start") 
		form = SVGForm(request.POST)

		# In the 'form' class the clean function 
		# is defined, if all the data is correct 
		# as per the clean function, it returns true 
		if form.is_valid(): 

			# Temporarily make an object to be add some 
			# logic into the data if there is such a need 
			# before writing to the database 
			post = form.save(commit = False) 

			# Finally write the changes into database 
			post.save()
			data = {	"brand":form['brand'].value(),
						"slogan":form['slogan'].value(),
                        "industry":form['industry'].value(),
                        "style":form['style'].value(),
                        "font_family":form['font'].value(),
                        "tag":form['tag'].value(),
                        "symbol":form['symbol'].value(),
                        "font_color":form['color'].value(),
                        "line_color":form['color'].value()}

			brand_name = form['brand'].value()
			# svg_url = 'app/engine/static/'+brand_name'+'.png'
			# logger.error(f'SVG FORM DATA : {brand_name},{svg_url}') 
			general_path = 'mediafiles/svg/'+ brand_name
			abc = SVG_LOGOGO(**data)
			# abc = SVG_LOGOGO(brand_name)

			# svg_code = abc.template1()

			svg_code = getattr(abc,form['template'].value())()

			svg_name = default_storage.save(general_path+'.svg', ContentFile(svg_code))
			svg_url = default_storage.url(svg_name)
			logger.error(f'{svg_url}||{svg_name}')
			logger.error(f'{type(svg_code)}')
			png_path = general_path +'.png'
			svg_url = general_path +'.svg'

			# pngData = svg2png(bytestring=svg_code)
			svg2png(bytestring=svg_code, write_to= png_path)
			logger.error(f'png_path:{png_path}||svg_url:{svg_url}')
			# aa = default_storage.open(svg_url)
			# logger.error(f'{aa}')
			# was inserted successfully 
			# return render(request, "style.html", context)
			return render(request, "home.html", {"png_url": png_path, "svg_url": 'mediafiles/'+svg_url })
			# return render(request, "home.html", {"svg_url": f"'{brand_name}'"}) 
			# return render(request, "home.html", {'graph':svg_fff}) 
		else: 
		
			# Redirect back to the same page if the data 
			# was invalid 
			return render(request, "home.html", {'form':form}) 
	else: 

		# If the request is a GET request then, 
		# create an empty form object and 
		# render it into the page 
		form = SVGForm(None) 
		return render(request, 'home.html', {'form':form, "svg_url": svg_url})