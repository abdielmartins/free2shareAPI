from flask import Blueprint, request, current_app
from flask.globals import session
from free_2_share.models.user_model import UserModel
from http import HTTPStatus

bp_user = Blueprint("user_view", __name__, url_prefix="/api/users")


@bp_user.route("/create", methods=["POST"])
def create_user():
    try:
        session = current_app.db.session

        body = request.get_json()

        name = body["name"]
        nickname = body["nickname"]
        email = body["email"]
        password = body["password"]
        phone = body["phone"]
        profile_pic_url = body["link_profile_picture"]
        bio = body["bio"]

        new_user = UserModel(
            name=name,
            nickname=nickname,
            email=email,
            phone=phone,
            link_profile_picture=profile_pic_url,
            bio=bio,
        )

        new_user.password = password

        session.add(new_user)
        session.commit()

        return {
            "user": {
                "id": new_user.id,
                "name": new_user.name,
                "nickname": new_user.nickname,
                "email": new_user.email,
                "phone": new_user.phone,
                "link_profile_picture": new_user.link_profile_picture,
                "bio": new_user.bio,
                "favorites": new_user.favorites_list,
            }
        }, HTTPStatus.CREATED

    except KeyError:
        return {"message": "Could not create new user! Verify your request body"}, HTTPStatus.BAD_REQUEST


@bp_user.route("/get", methods=["GET"])
def list_all_users():
    name_filter = request.args.get("name")

    if name_filter:
        list_of_users: UserModel = (
            UserModel.query.filter(UserModel.name.like(f"%{name_filter}%")).order_by(UserModel.name).all()
        )
    else:
        list_of_users: UserModel = UserModel.query.all()

    return {
        "users": [
            {
                "name": user.name,
                "nickname": user.nickname,
                "email": user.email,
                "phone": user.phone,
                "bio": user.bio,
                "favorites": user.favorites_list,
            }
            for user in list_of_users
        ]
    }, HTTPStatus.OK


@bp_user.route("/update/<int:user_id>", methods=["PATCH", "PUT"])
def update_user(user_id):
    KEYS_LIST = ("name", "nickname", "email", "password", "phone", "profile_pic_url", "bio")

    session = current_app.db.session

    body = request.get_json()

    values_to_update = {}

    for key in KEYS_LIST:
        if body.get(key):
            values_to_update[key] = body.get(key)

    print(values_to_update)

    return HTTPStatus.OK