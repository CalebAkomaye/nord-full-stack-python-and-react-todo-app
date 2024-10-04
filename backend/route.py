from app import app, db
from flask import request, jsonify
from model import Todo

@app.route('/api/todos', methods=["GET"])
def get_todos():
      todos = Todo.query.all()
      if len(todos) == 0:
          return jsonify({"msg": ["Nothing Here"]})
      
      result = [todo.to_json() for todo in todos]
      return jsonify(result)


@app.route("/api/todos", methods=["POST"])
def create_todos():
     try:
      data = request.json
      
      required_fields = ["title", "priority", "isCompleted"]
      for field in required_fields:
          if field not in data:
              return jsonify({"err": f"missing required field: [{field}]"}), 400

      title = data.get('title')
      priority = data.get('priority')
      isCompleted = 1 if data.get('isCompleted').lower() == "true" else 0

      new_todo = Todo(title=title, priority=priority, is_completed=bool(isCompleted))
      db.session.add(new_todo)
      db.session.commit()

      return jsonify({'msg': 'successfully added a new task'}), 201
     except Exception as e:
         db.session.rollback()
         return jsonify({"error": str(e)}), 500

@app.route("/api/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    try:
        todo = Todo.query.get(id)
        if todo is None:
            return jsonify({"msg": "Todo Item Not Found"})
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"msg": "Item Deleted Successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": str(e)}), 500
    
@app.route("/api/todos/<int:id>", methods=["PATCH"])
def update_todo(id):
    try:
        todo = Todo.query.get(id)
        if todo is None:
            return jsonify({"msg": "Todo Item Not Found"})
        
        data = request.json
        todo.title = data.get('title', todo.title)
        todo.priority = data.get('priority', todo.priority)
        todo.is_completed = 1 if data.get('isCompleted', todo.is_completed) == 'true' else 0

        db.session.commit()
        return jsonify(todo.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": str(e)}), 500

