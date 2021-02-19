from rest_framework.views import APIView
from .models import ProductCategory
from .serializers import ProductCategorySerializer
from rest_framework import permissions, status
from apps.ecauth.authentications import JWTAuthentication
from rest_framework.response import Response


# Create your views here.
class ProductCategoryView(APIView):

    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get(self, request, parent_category_id=None):
        queryset = ProductCategory.objects.filter(parent_id=parent_category_id)
        serializer = ProductCategorySerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)