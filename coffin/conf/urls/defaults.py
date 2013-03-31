from django.conf.urls import (handler403, handler404, handler500,
        include, patterns, url)

handler404 = 'coffin.views.defaults.page_not_found'
handler500 = 'coffin.views.defaults.server_error'
