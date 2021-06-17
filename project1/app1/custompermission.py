from rest_framework.permissions import BasePermission
from rest_framework import serializers
from app1.seriallizers import *

# according to our choice to give permission of get, post etc.
class mypermission(BasePermission):
    def has_permission(self, request, view):
        if request.method=='GET':
            return True
        '''
        if request.method=='POST':
            name=request.data.get('name')

            return True
        '''  



        return False