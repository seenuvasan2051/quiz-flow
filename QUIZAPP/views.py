from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from QUIZAPP.models import *

# Create your views here.
def indexview(request):
 return render(request,'index.html')

def adminloginview(request):
 return render(request,'adminlogin.html')

def userloginview(request):
 return render(request,'userlogin.html')

def adminverificationview(request):
 contact = request.POST['contact']
 password = request.POST['password']
 if contact== '9845123684' and password== "admin":
  return render(request,'adminhome.html')
 else:
   return render(request,'adminlogin.html')
 
def newuserview(request):
 return render(request,'newuser.html')
  
 
def savenewuserview(request):
 name= request.POST['name']
 address = request.POST['address']
 email = request.POST['email']
 phonenumber = request.POST['phonenumber']
 password = request.POST['password']
 
 newuser = user(name = name, address = address, email = email, phonenumber = phonenumber, password = password)
 newuser.save()
 return render( request,'userlogin.html')

def processuserloginview(request):
    contactno = request.POST["contact"]
    pwd = request.POST["password"]

    userdata = user.objects.filter(phonenumber = contactno)
    for userinfo in userdata:
       if userinfo.password == pwd : 
           request.session['userid'] = userinfo.id   
           return render(request,'userhome.html')
       
    return render(request,'userlogin.html')

def mathquizview(request):
    quizzes = Quiz.objects.filter(quiz_type="maths")
    return render(request, 'mathquiz.html', {'quiz_questions': quizzes})

def englishquizview(request):
  quizzes = Quiz.objects.filter(quiz_type="english")
  return render(request,'englishquiz.html',{'quiz_questions': quizzes})

def gkquizview(request):
  quizzes = Quiz.objects.filter(quiz_type="gk")
  return render(request,'gkquiz.html',{'quiz_questions': quizzes})
  
def submitview(request):
  return render(request,'userhome.html')

def create_quiz_view(request):
    if request.method == 'POST':
        quiz_type = request.POST.get('quiz_type') 
        question_text = request.POST.get('question_text')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correct_option = request.POST.get('correct_option')

        # Create a new quiz object
        new_quiz = Quiz(
            quiz_type=quiz_type,
            question_text=question_text,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            correct_option=correct_option
        )

        # Save the new quiz to the database
        new_quiz.save()

        success_message = "Quiz created successfully"
        return JsonResponse({'status': 'success', 'message': success_message})

def submit_quiz(request):
    if request.method == 'POST':
        submitted_answers = {}
        for key, value in request.POST.items():
            if key.startswith('question'):
                question_id = key.replace('question', '')
                submitted_answers[question_id] = value

        # Filter only that particular quiz 
        quiz_type = request.POST.get('quiz_type') 
        quiz = Quiz.objects.filter(quiz_type=quiz_type)
        correct_answers = {str(question.id): question.correct_option for question in quiz}

        score = sum(1 for question_id, submitted_answer in submitted_answers.items()
                    if correct_answers.get(question_id) == submitted_answer)

        total_questions = len(correct_answers)

        return JsonResponse({'status': 'success', 'message': 'Quiz submitted successfully',
                             'score': score, 'totalQuestions': total_questions})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

