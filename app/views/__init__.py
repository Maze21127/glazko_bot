from flask_admin.contrib.sqla import ModelView
from wtforms import TextAreaField


class MessageView(ModelView):
    column_display_pk = True
    column_labels = {
        "id": "ID",
        "title": "Название",
        "text": "Сообщение"
    }
    column_default_sort = ('id', True)

    can_create = False
    can_edit = True
    can_delete = False
    can_export = True
    create_modal = True
    edit_modal = True

    form_overrides = {
        'text': TextAreaField,
    }

    column_searchable_list = ("id", "title", "text")
    export_max_rows = 500
    export_types = ['csv']

    #  Поля, которые нужно показывать
    #  column_list = ['id', 'title', 'text']