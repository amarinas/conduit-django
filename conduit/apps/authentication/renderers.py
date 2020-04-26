import json

#from rest_framework.renderers import JSONRenderer
from conduit.apps.core.renderers import ConduitJSONRenderer

class UserJSONRenderer(ConduitJSONRenderer):
    object_label = 'user'
    pagination_object_label ='user'
    pagination_count_label ='usersCount'

    def render(self, data, media_type=None, renderer_context=None):

        #decode token before rendering
        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):
            #if token is bytes then it will decode
            data['token'] = token.decode('utf-8')


        return super(UserJSONRenderer, self).render(data)
