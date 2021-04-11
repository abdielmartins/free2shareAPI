from flask import Blueprint, request, current_app
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
        bio = body["body"]

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
                "nickname": nickname,
                "email": email,
                "phone": phone,
                "link_profile_picture": profile_pic_url,
                "bio": bio,
            }
        }

    except KeyError:
        return {"message": "Could not create new user! Verify your request body"}, HTTPStatus.BAD_REQUEST
