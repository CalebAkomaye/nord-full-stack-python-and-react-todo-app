from app import db
from sqlalchemy.sql import func

class Todo(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      title = db.Column(db.String(250), nullable=False)
      priority = db.Column(db.String(10), nullable=False, default="low")
      created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
      updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
      is_completed = db.Column(db.Boolean(), nullable=False)

      def to_json(self):
            return{
                  "id": self.id,
                  "title":self.title,
                  "priority":self.priority,
                  "isCompleted": self.is_completed,
                  "createdAt":self.created_at,
                  "updatedAt":self.updated_at,
            }
