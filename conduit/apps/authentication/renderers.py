import json

from rest_framework.renderers import JSONRenderer

class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)
        #decode token before rendering
        token = data.get('token', None)

        if errors is not None:
            return super(UserJSONRenderer, self).render(data)

        if token is not None and isinstance(token, bytes):
            #if token is bytes then it will decode
            data['token'] = token.decode('utf-8')

            return json.dumps({
                'user': data
            })
