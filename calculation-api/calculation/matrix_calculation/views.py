from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .scripts import sequential, list_comprehension, generator, multiprocessing_pool
import tracemalloc
import time

class SequentialAPI(APIView):

    def post(self, request):
        n = request.data["n"]
        m = request.data["m"]
        special_points = request.data["points"]
        
        result, current, peak, elapsed =  sequential.api(n, m, special_points)

        response_data= {
            "result": result,
            "time_in_s": elapsed,
            "max_memory_in_MB": peak / 10**6
        }

        return Response(response_data, status=200)

class ListComprehensionAPI(APIView):

    def post(self, request):
        n = request.data["n"]
        m = request.data["m"]
        special_points = request.data["points"]

        result, current, peak, elapsed =  list_comprehension.api(n, m, special_points)

        response_data= {
            "result": result,
            "time_in_s": elapsed,
            "max_memory_in_MB": peak / 10**6
        }

        return Response(response_data, status=200)

class GeneratorAPI(APIView):

    def post(self, request):
        n = request.data["n"]
        m = request.data["m"]
        special_points = request.data["points"]
       
        result, current, peak, elapsed =  generator.api(n, m, special_points)

        response_data= {
            "result": result,
            "time_in_s": elapsed,
            "max_memory_in_MB": peak / 10**6
        }
        return Response(response_data, status=200)

class MultiprocessingAPI(APIView):

    def post(self, request):
        n = request.data["n"]
        m = request.data["m"]
        special_points = request.data["points"]

        result, current, peak, elapsed =  multiprocessing_pool.api(n, m, special_points)

        response_data= {
            "result": result,
            "time_in_s": elapsed,
            "max_memory_in_MB": peak / 10**6
        }

        return Response(response_data, status=200)
