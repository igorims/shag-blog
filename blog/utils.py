from .models import Category

class DataMixin:
    def get_user_context(self, **kwargs) -> dict:
        context = kwargs
        context['cats'] = Category.objects.all()

        if self.request.user.is_authenticated:
            context['is_authenticated'] = True
        else:
            context['is_authenticated'] = False
        return context
