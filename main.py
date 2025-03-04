from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from drive_utils import upload_note, list_notes, get_note_content

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    note_title = data.get("title")
    note_content = data.get("content")
    if not note_title or not note_content:
        return jsonify({"error": "Title and content required"}), 400

    file_id = upload_note(note_content, note_title)
    return jsonify({"message": "Note uploaded successfully", "file_id": file_id})


@app.route("/notes", methods=["GET"])
def get_notes():
    notes = list_notes()
    return jsonify(notes)


@app.route("/note/<file_id>", methods=["GET"])
def get_note(file_id):
    content = get_note_content(file_id)
    return jsonify({"content": content})


if __name__ == "__main__":
    app.run(debug=True)
