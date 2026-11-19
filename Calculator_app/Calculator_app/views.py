from django.http import HttpResponse
from django.template import loader 
# Defining a function which
# will receive request and
# perform task depending 
# upon function definition
def hello_geeks (request) :
 
    # This will return Hello welcome
    # string as HttpResponse
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())