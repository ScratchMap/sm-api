from flask_restful import Resource
from flask import request
from app.posts.models import Post
from app.utils import db
from app.auth.views import authenticate

class Posts(Resource):

    def get(self, post_id=None, user_id=None):
        
        if post_id:
            posts = Post.query.filter_by(id=post_id).all()
        elif user_id:
            posts = Post.query.filter_by(user_id=user_id).all()
        else:
            posts = Post.query.all()

        responseObject = {
            'status' : 'success',
            'message' : 'Successfully got post(s)',
            'posts' : [post.get_all_data for post in posts]
        }
        return responseObject, 200

class User_Posts(Resource):

    @authenticate
    def get(self, resp, post_id=None):
        if post_id:
            return Posts.get(self=self, post_id=post_id)
        else:
            return Posts.get(self=self, user_id=resp)

    @authenticate
    def post(self, resp):
        post_data = request.get_json()

        try:
            post_post_data = post_data['post']

            post = Post(
                title=post_post_data['data']['title'],
                description=post_post_data['data']['body'],
                geo_lat=post_post_data['geo']['lat'],
                geo_lng=post_post_data['geo']['lng'],
                user_id=resp
            )
            db.session.add(post)
            db.session.commit()

            responseObject = {
                'status' : 'success',
                'message' : 'Successfully added post.',
                'post' : post.get_id_title
            }
            return responseObject, 201

        except Exception as e:
            db.session.rollback()
            
            responseObject = {
                'status' : 'fail',
                'message' : 'Try again.'
            }
            return responseObject, 500

    @authenticate
    def delete(self, resp, post_id):
        try:
            post = Post.query.filter_by(id=post_id, user_id=resp).first()
            if post:
                db.session.delete(post)
                db.session.commit()

                responseObject = {
                    'status' : 'success',
                    'message' : 'Successfully deleted post.',
                    'post' : post.get_id_title
                }
                return responseObject, 202
            else:
                responseObject = {
                    'status' : 'fail',
                    'message' : 'Post does not exits.'
                }
                return responseObject, 404

        except Exception as e:
            db.session.rollback()
            
            responseObject = {
                'status' : 'fail',
                'message' : 'Try again.'
            }
            return responseObject, 500

    @authenticate
    def patch(self, resp, post_id):
        post_data = request.get_json()

        try:
            post = Post.query.filter_by(id=post_id, user_id=resp).first()
            if post:
                post_post_data = post_data['post']
                if post.title != post_post_data['data']['title']:
                    post.title = post_post_data['data']['title']
                if post.description != post_post_data['data']['body']:
                    post.description = post_post_data['data']['body']

                db.session.commit()

                responseObject = {
                    'status' : 'success',
                    'message' : 'Successfully update post.',
                    'post' : post.get_id_title
                }
                return responseObject, 202
            
            else:
                responseObject = {
                    'status' : 'fail',
                    'message' : 'Post does not exits.'
                }
                return responseObject, 404


        except Exception as e:
            db.session.rollback()
            
            responseObject = {
                'status' : 'fail',
                'message' : 'Try again.'
            }
            return responseObject, 500
