from flask_restful import Resource
from flask import request
from app.posts.models import Post

class Index(Resource):

    def get(self):
        user_id = request.args.get('user_id')
        offset = int(request.args.get('offset', 0))
        limit = int(request.args.get('limit', 20))
        (sw_lat, sw_lng) = [float(s) for s in request.args.get('sw', '0, 0').split(',')]
        (ne_lat, ne_lng) = [float(s) for s in request.args.get('ne', '0, 0').split(',')]

        param = {}
        if user_id:
            param['user_id'] = user_id

        try:
            query = Post.query
            query = query.filter_by(**param)
            query = query.filter(
                Post.geo_lat <= ne_lat,
                Post.geo_lat >= sw_lat
            )
            if sw_lng <= ne_lng:
                query = query.filter(
                    Post.geo_lng <= ne_lng,
                    Post.geo_lng >= sw_lng
                )
            else:
                query = query.filter(
                    (Post.geo_lng <= ne_lng) |
                    (Post.geo_lng >= sw_lng)
                )
            posts = query. \
                order_by(Post.datetime.desc()). \
                limit(limit). \
                offset(offset*limit)

            responseObject = {
                'status' : 'success',
                'message' : 'Successfully got post(s)',
                'posts' : [post.get_id_title for post in posts]
            }
            return responseObject, 200
        
        except Exception as e:
            responseObject = {
                'status' : 'fail',
                'message' : 'Try again.'
            }
            return responseObject, 500
