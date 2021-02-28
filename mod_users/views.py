from . import user

@user.route("/")
def users_index():
    return "welcom to panel users"