from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator, qs_exists


class UniqueMailLowerValidator(UniqueValidator):
    def __call__(self, value, serializer_field):
        # Determine the existing instance, if this is an update operation.
        instance = getattr(serializer_field.parent, "instance", None)

        queryset = self.queryset.filter(email__iexact=value)
        queryset = self.exclude_current_instance(queryset, instance)
        if qs_exists(queryset):
            raise ValidationError(self.message, code="unique")
