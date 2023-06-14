from django.contrib import admin

# 당신의 모델을 여기서 등록하세요.

from .models import UserInfo

admin.site.register(UserInfo)

# 여기서 등록해야 admin 페이지에서 웹으로 관리할 수 있다.

# 만약 settings.py 에서 INSTALLED_APPS에 등록되어 있지 않으면
# 정상적으로 처리되지 않는 것에 주의 !!

# python manage.py makkemigrations
# python manage.py migrate
# python manage.py runserver
