from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Your existing logic for the home page here
    doctor_list = [
    {"name": "Dr. Smith", "doctor_id": 1001, "expertise": "Cardiology"},
    {"name": "Dr. Johnson", "doctor_id": 1002, "expertise": "Pediatrics"},
    {"name": "Dr. Davis", "doctor_id": 1003, "expertise": "Orthopedics"},
    {"name": "Dr. Miller", "doctor_id": 1004, "expertise": "Oncology"},
    {"name": "Dr. Wilson", "doctor_id": 1005, "expertise": "Neurology"}
                  ]
    context={
    doctor_list:doctor_list
   } 
    return render(request, 'appointment.html', context)

def appointment_form(request):
    if request.method == 'POST':
        # Process the submitted form data here and save it to the model
        # Example: Creating an Appointment object and saving it to the database
        appointment_id = request.POST.get('appointment_id')
        doctor_id = request.POST.get('doctor_id')
        patient_id = request.POST.get('patient_id')
        appointment_time = request.POST.get('appointment_time')
        appointment_date = request.POST.get('appointment_date')
        purpose = request.POST.get('purpose')
        sick_information = request.POST.get('sick_information')
        created_at = request.POST.get('created_at')
        updated_at = request.POST.get('updated_at')
        # ... (create Appointment model instance and save)

        return HttpResponse("Appointment created successfully")  # Replace with appropriate response
    doctor_list = [
    {"name": "Dr. Smith", "doctor_id": 1001, "expertise": "Cardiology"},
    {"name": "Dr. Johnson", "doctor_id": 1002, "expertise": "Pediatrics"},
    {"name": "Dr. Davis", "doctor_id": 1003, "expertise": "Orthopedics"},
    {"name": "Dr. Miller", "doctor_id": 1004, "expertise": "Oncology"},
    {"name": "Dr. Wilson", "doctor_id": 1005, "expertise": "Neurology"}
                  ]
    context={
    doctor_list:doctor_list
   } 
    return render(request, 'appointment_form.html',context)

def doctor_view(request):
    return render(request, 'doctorviews.html', {})

def patient_view(request):
    return render(request, 'patientviews.html', {})
def my_view(request):
    # Make a GET request to an external API
    api_url = 'http://127.0.0.1:8000/api/appointments/'  # Replace this with your API endpoint
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract data from the response
        data = response.json()

        # Process the data as needed
        # For example, pass the data to a template for rendering
        return render(request, 'patientfulldetails.html', {'data': data})
    else:
        # Handle other status codes, e.g., 404, 500, etc.
        return HttpResponse("Failed to fetch data from the API", status=response.status_code)