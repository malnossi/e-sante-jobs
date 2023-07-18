from rest_framework import routers

# Accounts routes
from accounts import api as accounts_api

# Posts routes
from posts import api as posts_api

router = routers.DefaultRouter()

router.register(prefix="accounts", viewset=accounts_api.StudentProfilViewSet, basename="student")
router.register(prefix="posts", viewset=posts_api.PostViewSet, basename="post")