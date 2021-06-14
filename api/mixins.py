from django.utils import timezone
from rest_framework.response import Response


class UpdatePostModelMixin:
    def update(self, req, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        if req.data.updated:
            instance.updated = timezone.now()
        serializer = self.get_serializer(instance, data=req.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)
