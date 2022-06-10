from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
import App.models as models
import App.ser as ser


class Index(APIView):
    def get(self, request):
        queryset = models.Group.objects.all()
        ser_data = ser.GroupSer(instance=queryset, many=True)
        # ser_data.is_valid(raise_exception=True)
        # print(ser_data.data)
        for i in queryset.get(id=1).rule_id.all():
            print(i)
        rules = models.Rule.objects.first().group
        print('rules', rules.all())

        return Response(ser_data.data)
