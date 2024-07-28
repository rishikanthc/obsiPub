import falcon
from obsipub import funcs as F
import json


class Posts:
    def on_get(self, req, resp):
        _titles = F.list_posts()
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(_titles)


app = application = falcon.App()
posts = Posts()
app.add_route("/posts", posts)
