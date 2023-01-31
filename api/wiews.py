from flask import jsonify, Blueprint

from dao.dao import PostsDAO


api_blueprint = Blueprint('api_blueprint', __name__)
posts = PostsDAO('./data/posts.json', './data/comments.json')


@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    return jsonify(posts.load_posts_json())


@api_blueprint.route('/api/posts/<int:postid>', methods=['GET'])
def get_post_by_id(postid):
    return jsonify(posts.get_post_by_pk_json(postid))
