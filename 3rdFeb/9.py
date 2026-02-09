from flask import Flask, request, jsonify

app=Flask(__name__)

students_data={
    1:{"name":"raghu","dept":"ise","cgpa":9.47},
    2:{"name":"rahul","dept":"cse","cgpa":9.17},
    3:{"name":"rohan","dept":"ece","cgpa":8.76}
}

#get all students
@app.route('/', methods=['GET'])
def get_all():
    try:
        return jsonify(students_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        print("every student called")
        
#get student by id
@app.route('/<int:id>', methods=['GET'])
def get_student(id):
    try:
        student=students_data.get(id)
        if student:
            return jsonify(student)
        else:
            return jsonify({"error": "Student not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        print(f"student {id} called")
    
if __name__=='__main__':
    app.run(debug=True)