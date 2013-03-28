from coffin import template
from django.contrib.staticfiles.storage import staticfiles_storage
from coffin.templatetags.static import StaticExtension as CoffinStaticExtension


register = template.Library()


class StaticExtension(CoffinStaticExtension):
    """Implements the {% static %} tag as provided by the ``staticfiles``
    contrib module.

    Returns the URL to a file using staticfiles' storage backend.

    Usage::

        {% static path [as varname] %}

    Examples::

        {% static "myapp/css/base.css" %}
        {% static variable_with_path %}
        {% static "myapp/css/base.css" as admin_base_css %}
        {% static variable_with_path as varname %}

    """

    @classmethod
    def get_static_url(cls, path):
        return super(StaticExtension, cls).get_static_url(
            staticfiles_storage.url(path))


register.tag(StaticExtension)


def static(path):
    return StaticExtension.get_static_url(path)
