from django.db import models
from django.core.exceptions import ValidationError
import random, string


LENGTH_STUDENT_UID = 20


def unique_rand():
    """Randomize student id

    This function will give out random string as a unique student id.

    Args: 
        None

    Returns:
        Random string
    """
    while True:
        studentid = ''.join(random.choices(string.ascii_uppercase + string.digits, k = LENGTH_STUDENT_UID))
        if not Student.objects.filter(studentid=studentid).exists():
            return str(studentid)


def is_not_reach_max_students(school_obj):
    """Validator to check number of max students

    This function will validate and return if reaching max number of students in particular school. The function will raise error if so.

    Args: 
        - school_id: school that validate against

    Returns:
        None
    """
    school_id = school_obj.pk
    max_students = school_obj.max_students
    #max_students = School.objects.filter(pk=school_id).first().max_students
    if Student.objects.filter(school=school_id).count() is max_students:
        raise ValidationError("maximum number of student reached")


class School(models.Model):
    """Represent school that can contain students

    Fields:
    - name: school name with 20 char max
    - max_students: maximum number of students
    - created: date/time of created record

	"""
    name = models.CharField(max_length=20)
    max_students = models.PositiveSmallIntegerField(default=1)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
    	return self.name


class Student(models.Model):
    """Represent student in a particular school

    Fields:
    - name: school name with 20 char max
    - max_students: maximum number of students
    - created: date/time of created record

	"""
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    studentid=models.CharField(primary_key=True, max_length=20, unique=True, default=unique_rand, editable=False)
    created = models.DateField(auto_now_add=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, validators=[is_not_reach_max_students])
    age = models.PositiveSmallIntegerField(default=0)
    nationality = models.CharField(default="Thai", max_length=20)
    
    def __str__(self):
        return self.firstname+" "+self.lastname

