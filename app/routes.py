from flask import url_for, redirect
from flask_admin import expose, BaseView, AdminIndexView
from sqlalchemy import desc

from models import Message


class MyMainView(AdminIndexView):
    @expose
    def admin_main(self):
        messages = Message.query.order_by(desc(Message.id)).all()
        return self.render('admin/index.html', messages=messages)

