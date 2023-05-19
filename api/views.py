from django.shortcuts import render

from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.decorators import action
from django.db.models import BooleanField, Case, When


class UserViewSet(DjoserUserViewSet):
    @action(["get"], detail=False)
    def me(self, request, *args, **kwargs):
        return super().me(request, *args, **kwargs)


    def get_queryset(self):
        request_user = self.request.user
        queryset = super().get_queryset()
        if request_user.is_authenticated:
            queryset = (
                super()
                .get_queryset()
                .annotate(
                    is_subscribed=Case(
                        When(
                            author_subscriptions__subscriber=request_user,
                            then=True,
                        ),
                        default=False,
                        output_field=BooleanField(),
                    )
                )
            )
        return queryset