from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from datetime import datetime
import uuid

app = Flask(__name__)

# You can add your mongo db configuration url below (I have added my local MongoDB Compass url)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/logisticsData'
mongo = PyMongo(app)

# API endpoint for creating a new document
@app.route('/api/data', methods=['POST'])
def create_data():
    data = request.json
    data['timestamp'] = datetime.utcnow()
    # Generate a UUID and add it to the data as a unique identifier
    data['uuid'] = str(uuid.uuid4())
    collection = mongo.db.logisticsData
    result = collection.insert_one(data)
    return jsonify({'message': 'Data created successfully', 'id': data['uuid']}), 201

# API endpoint for retrieving all documents
@app.route('/api/data', methods=['GET'])
def get_all_data():
    collection = mongo.db.logisticsData
    data = list(collection.find())
    # Convert ObjectId to string for JSON serialization
    for item in data:
        item['_id'] = str(item['_id'])

    return jsonify(data), 200

# API endpoint for retrieving a specific document by UUID
@app.route('/api/data/<string:data_uuid>', methods=['GET'])
def get_data_by_uuid(data_uuid):
    collection = mongo.db.logisticsData
    data = collection.find_one({'uuid': data_uuid})
    if data:
        # Convert ObjectId to string for JSON serialization
        data['_id'] = str(data['_id'])
        return jsonify(data), 200
    else:
        return jsonify({'message': 'Data not found'}), 404

# API endpoint for deleting a specific document by UUID
@app.route('/api/data/<string:data_uuid>', methods=['DELETE'])
def delete_data(data_uuid):
    collection = mongo.db.logisticsData
    result = collection.delete_one({'uuid': data_uuid})
    if result.deleted_count > 0:
        return jsonify({'message': 'Data deleted successfully'}), 200
    else:
        return jsonify({'message': 'Data does not exist in database'}), 404

if __name__ == '__main__':
    app.run(debug=True)
