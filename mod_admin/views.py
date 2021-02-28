from . import admin

@admin.route("/")
def admin_index():
    return "welcom to panel admin"