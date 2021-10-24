from django.urls import include, path
from rest_framework_nested import routers
from justapp.views import StudentViewSet, SchoolViewSet, StudentSchoolViewSet

# create router for schools and students endpoint
router = routers.SimpleRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'students', StudentViewSet)

# register nested student-school endpoint
schools_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
schools_router.register(r'students', StudentSchoolViewSet, basename='student-school ')

# assign url pattern from the routers
urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(schools_router.urls)),
]