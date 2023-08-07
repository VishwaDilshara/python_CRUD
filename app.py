# from flask import Flask, render_template, request, redirect
# from models import db, StudentModel
#
# app = Flask(__name__)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)
#
# # Create the table before the first request
# # @app._got_first_request
# # def create_table():
# #     db.create_all()
#
# @app.route('/create', methods = ['GET', 'POST'])
# def create():
#     if request.method == 'GET':
#         return render_template('create.html')
#
#     if request.method == 'POST':
#         hobby = request.form.getlist('hobbies')
#         hobbies = ",".join(map(str, hobby))
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         email = request.form['email']
#         password = request.form['password']
#         gender = request.form['gender']
#         hobbies = hobbies
#         country = request.form['country']
#
#         students = StudentModel(
#             first_name = first_name,
#             last_name = last_name,
#             email = email,
#             password = password,
#             gender = gender,
#             hobbies = hobbies,
#             country = country
#         )
#         db.session.add(students)
#         db.session.commit()
#         return redirect('/')
#
# @app.route('/', methods = ['GET'])
# def RetrieveList():
#     students = StudentModel.query.all()
#     return render_template('index.html', students = students)
#
# @app.route('/<int:id>/delete', methods=['GET', 'POST'])
#
# def delete(id):
#     students = StudentModel.query.filter_by(id=id).first()
#     if request.method == 'POST':
#         if students:
#             db.session.delete(students)
#             db.session.commit()
#             return redirect('/')
#             abort(404)
#         return render_template('delete.html')
#
#
# app.run(host='localhost', port=8080)

# -------------------------------------------------------------------------------
from flask import Flask, render_template, request, redirect
from models import db, StudentModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create the table before the first request
created_table = False

@app.before_request
def create_table():
    global created_table
    if not created_table:
        db.create_all()
        created_table = True

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    
    if request.method == 'POST':
        hobby = request.form.getlist('hobbies')
        hobbies = ",".join(map(str, hobby))
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        hobbies = hobbies
        country = request.form['country']

        students = StudentModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            gender=gender,
            hobbies=hobbies,
            country=country
        )
        db.session.add(students)
        db.session.commit()
        return redirect('/')
    
@app.route('/', methods=['GET'])
def RetrieveList():
    students = StudentModel.query.all()
    return render_template('index.html', students=students)
#
# @app.route('/<int:student_id>/delete', methods=['GET'])
# def delete(student_id):
#     student = StudentModel.query.get_or_404(student_id)
#     db.session.delete(student)
#     db.session.commit()
#     return redirect('/')
#     abort(404)
#
#
#
# def delete(id):
#     students = StudentModel.query.filter_by(id=id).first()
#     if request.method == 'POST':
#         if students:
#             db.session.delete(students)
#             db.session.commit()
#             return redirect('/')
#             abort(404)
#         return render_template('delete.html')
@app.route('/<int:student_id>/delete', methods=['GET'])
def delete(student_id):
    student = StudentModel.query.get_or_404(student_id)

    if request.method == 'POST':
        if students:
            db.session.delete(student)
            db.session.commit()
            return redirect('/')
            abort(404)
        return render_template('delete.html', student=student)

if __name__ == "__main__":
    app.run(host='localhost', port=8080)


