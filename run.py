from flask import redirect, jsonify
from app import create_app, db
from models import Message

app = create_app()


@app.route('/')
def main():
    return redirect('/admin', 302)


@app.route('/api/messages/<message_name>')
def get_message(message_name):
    message = Message.query.filter_by(title=message_name).first()
    return jsonify(
        {
            "text": message.text
        }
    )


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(host='0.0.0.0', port=6571)
