from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View


class StartPage(View):
    def get(self, request):
        return JsonResponse({"status": "Ok"}, status=200)