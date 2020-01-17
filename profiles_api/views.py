from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as function(get, post, path, put, delete)",
            "Is similar to a traditional Django View",
            "Gives the most control over your application logic",
            "Is mapped manually to URLs"
        ]
        return Response({"message": "Hello", "an_apiview": an_apiview})
