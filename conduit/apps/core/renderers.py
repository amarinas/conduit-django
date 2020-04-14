import json

from rest_framework import JSONRenderer

class ConduitJSONRenderer(JSONRenderer):
    charset ='utf-8'
    object-label = 'object'

    def render(self, data, media_type=None, render_context=None):
        error = data.get('errors', None)

        if error is not None:
            return super(ConduitJSONRenderer, self).render(data)


        return json.dumps({
            self.object_label: data
        })
