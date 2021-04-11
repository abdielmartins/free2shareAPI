from flask import Flask


def init_app(app: Flask):

    from free_2_share.views.user_view import bp_user

    app.register_blueprint(bp_user)
