from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import datetime
from .models import User

class CustomLoginRequiredMixin():
    def dispatch(self,request,*args,**kwargs):
        if 'Authorization' not in request.headers:
            response=Response({'error':'Please set Auth-Token'},status=status.HTTP_404_NOT_FOUND)
            response.accepted_renderer=JSONRenderer()
            response.accepted_media_type='application/json'
            response.rendered_context={}
            return response 
        
        token=request.headers['Authorization']
        now=datetime.datetime.now()
        login_user=User.objects.filter(token=token, token_expired__gt=now)

        if len(login_user)==0:
            response=Response({'error': 'The Token is Expired or Invalid'}, status=status.HTTP_404_NOT_FOUND)
            response.accepted_renderer=JSONRenderer()
            response.accepted_media_type='application/json'
            response.rendered_context={}
            return response 
        
        request.login_user=login_user[0]
        return super().dispatch(request,*args,**kwargs)