from django.views.generic import TemplateView


class WebUiView(TemplateView):

    template_name="webui/index.html"
