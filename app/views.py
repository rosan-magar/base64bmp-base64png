import json
from json.encoder import JSONEncoder
from django.http.response import JsonResponse
from rest_framework.views import APIView
from PIL import Image
import base64
from io import BytesIO
import os


class UploadImage(APIView):         

    def post(self, request, format=None):
        # print("request data: " , request.data['base64_bmp'])
        # print(bas)
        bmp_signatures = request.data['base64_bmp_signatures']
        png_signatures = []
        for signature in bmp_signatures:
            temp = signature.replace('data:image/bmp;base64,', '')
            updated_signature =  self.convert_bmp_to_png(temp)
            updated_png_signature =  updated_signature.decode("utf-8")
            png_signatures.append('data:image/png;base64,' + updated_png_signature)
        return JsonResponse({"message":"Hello, this is from get codechecker", "png_signatures" : png_signatures})


    def convert_bmp_to_png(self, signature):
        im = Image.open(BytesIO(base64.b64decode(signature)))
        im.convert("RGB")
        im.save("test.png")
        encoded_base64_png = base64.b64encode(open("test.png", "rb").read()) 
        os.remove("test.png")
        return encoded_base64_png