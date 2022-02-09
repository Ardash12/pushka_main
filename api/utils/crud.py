import json

def get_recommendations_by_id(db, id: str, type: str):
    connect = db.space(type)
    recommendations = dict(connect.select(id))
    return recommendations[id]

def get_recommendations_by_phone(db, phone: str, type: str):
    connect = db.space(type)
    recommendations = dict(connect.select(phone))
    return recommendations[phone]