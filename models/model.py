from dataclasses import fields
from datetime import datetime, timezone
import uuid
from marshmallow import Schema, fields
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Blacklist(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(), nullable=False)
    app_uuid = db.Column(db.String(), nullable=False)
    blocked_reason = db.Column(db.String(), nullable=True)
    request_ip = db.Column(db.String(), nullable=True)
    createdAt = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updatedAt = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'app_uuid': self.app_uuid,
            'blocked_reason': self.blocked_reason,
            'request_ip':self.request_ip,
            'createdAt': self.createdAt.isoformat(),
            'updatedAt': self.updatedAt.isoformat()
        }
class BlacklistJsonSchema(Schema):
    id = fields.Str()
    email = fields.Str()
    app_uuid = fields.Str()
    blocked_reason = fields.Str()
    request_ip = fields.Str()
    createdAt = fields.DateTime()
    updatedAt = fields.DateTime()
    def get_size(self, obj):
        return obj.size.name if obj.size else None