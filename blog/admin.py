from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for

from blog import models
from blog.app import db

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for('auth.login'))
        return super(MyAdminIndexView, self).index()


class CustomView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))


    def create_blueprint(self, admin):
        blueprint = super().create_blueprint(admin)
        blueprint.name = f'{blueprint.name}_admin'
        return blueprint

    def get_url(self, endpoint, **kwargs):
        if not (endpoint.startswith('.') or endpoint.startswith('admin.')):
            endpoint = endpoint.replace('.', '_admin.')
        return super().get_url(endpoint, **kwargs)

class TagAdminView(CustomView):
    column_searchable_list = ('name',)
    column_filters = ('name',)
    can_export = True
    export_types = ['csv', 'xlsx']
    create_modal = True
    edit_modal = True

class UserAdminView(CustomView):
    column_exclude_list = ('password',)
    column_details_exclude_list = ('password',)
    column_export_exclude_list = ('password',)
    column_searchable_list = ('first_name', 'last_name', 'is_staff', 'email')
    column_filters = ('first_name', 'last_name', 'is_staff', 'email')
    column_editable_list = ('first_name', 'last_name','is_staff')
    can_create = True
    can_edit = True
    can_delete = False

class AuthorAdminView(CustomView):
    #column_list = ('user.first_name','user.last_name','user.email',)
    #column_searchable_list = ('user.first_name', 'user.last_name','user.email',)
    can_create = True
    can_edit = False
    can_delete = False

admin = Admin(name="Blog Admin", index_view=MyAdminIndexView(), template_mode="bootstrap4")

admin.add_view(TagAdminView(models.Tag, db.session, category="Models"))
admin.add_view(CustomView(models.Article, db.session, category="Models"))
admin.add_view(AuthorAdminView(models.Author, db.session, category="Models"))
admin.add_view(UserAdminView(models.User, db.session, category="Models"))
