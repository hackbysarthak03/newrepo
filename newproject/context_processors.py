from doctor.models import DoctorProfile
from patient.models import PatientProfile


def getDoctorDetails(request):
    current_user = request.user
    data = DoctorProfile.objects.filter(user__username = current_user.username).first()

    return {
        'doctorData':data
    }

def getPatientDetails(request):
    current_user = request.user
    data = PatientProfile.objects.filter(user__username = current_user.username).first()

    return {
        'patientData':data
    }



