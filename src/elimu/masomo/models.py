from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#we extend the django profiles class to hold more information
class Profiles(models.Model):
	info = models.TextField("Information", max_length=200)
	user = models.ForeignKey(User, unique=True)
 	def get_absolute_url(self):
        	return ('profiles_profile_detail', (), { 'username': self.user.username })
    	get_absolute_url = models.permalink(get_absolute_url)

class County(models.Model):
	name = models.CharField("County", max_length=45)
class School(models.Model):
	name = models.CharField("School", max_length=45)
        address = models.CharField("Address", max_length=100)
	county = models.ForeignKey(County)
        latitude = models.CharField("Latitude", max_length=25)
        longitude = models.CharField("Longitude", max_length=25)
class Radius(models.Model):
	radius = models.CharField("Radius", max_length=25)
class Device(models.Model):
	deviceidentifier = models.CharField("Device ID", max_length=45)
        school = models.ForeignKey(School)
        apikey = models.CharField("API Key", max_length=25)
        radius = models.ForeignKey(Radius)
        status = models.BooleanField(default=True)
	def natural_key(self):
        	return (self.deviceidentifier, self.school)
	class Meta:
		verbose_name_plural = "Devices"
		db_table = 'elimu_device'
#have to add subject here because of the import
class Subject(models.Model):
	name = models.CharField("Subject", max_length=45)
        description = models.TextField("Description", max_length=255)
        def __unicode__(self):
		return self.name
# we now link the entities to the profiles
class Curriculumdev(Profiles):
        surname = models.CharField("Surname", max_length=25)
        firstname = models.CharField("Lastname", max_length=25)
class QATutor(Profiles):
        surname = models.CharField("Surname", max_length=25)
        firstname = models.CharField("Lastname", max_length=25)
        tutorid = models.CharField("Tutor ID", max_length=25)
        subjects = models.ManyToManyField(Subject)
class Teacher(Profiles):
        school = models.ForeignKey(School)
        surname = models.CharField("Surname", max_length=25)
        lastname = models.CharField("Lastname", max_length=25)
        emplcode = models.CharField("Code", max_length=25)
        techerid = models.CharField("Teacher ID", max_length=25)
class Student(Profiles):
        school = models.ForeignKey(School)
        surname = models.CharField("Surname", max_length=25)
        lastname = models.CharField("Lastname", max_length=25)
        prefname = models.CharField("Pref Name", max_length=25)
        kcpeno = models.CharField("KCPE Identifier", max_length=20)
#lets deal with the contents here
class Chapter(models.Model):
	subject = models.ForeignKey(Subject)
	title = models.CharField("Title", max_length=45)
        description = models.TextField("Description", max_length=255)
        def __unicode__(self):
		return self.title
class Constraint(models.Model):
	value = models.TextField("Value", max_length=255)
        def __unicode__(self):
		return self.value
class Topic(models.Model):
	chapter = models.ForeignKey(Chapter)
        title = models.CharField("title", max_length=25)
        def __unicode__(self):
		return self.chapter
class Page(models.Model):
        topic = models.ForeignKey(Topic)
        pagelabel = models.CharField("Label", max_length=25)
class ContentType(models.Model):
	name = models.CharField("Content Type", max_length=45)
        description = models.TextField("Description", max_length=255)
	constraint = models.ManyToManyField(Constraint)
        def __unicode__(self):
		return self.name
class Content(models.Model):
	title = models.CharField("Title", max_length=45)
	description = models.TextField("Description", max_length=255)
	value = models.TextField("Value", max_length=255)
        resource = models.FileField(upload_to='resources')
        page = models.ForeignKey(Page)
        def __unicode__(self):
		return self.title
class Quiz(models.Model):
	quizname = models.CharField("Quiz", max_length=45)
        subject = models.ForeignKey(Subject)
class Score(models.Model):
        score = models.IntegerField("Score")
class Question(models.Model):
	question = models.CharField("Question", max_length=200)
        quiz = models.ForeignKey(Quiz)
        score = models.ForeignKey(Score)
class QuesChoice(models.Model):
	answer = models.CharField("Choices", max_length=45)
        question = models.ForeignKey(Question)
        correct = models.BooleanField(default=0)
        explanation = models.TextField("Explanation")
class QuestionResults(models.Model):
	user = models.ForeignKey(User)
        choice = models.ForeignKey(QuesChoice)
	question = models.ForeignKey(Question)
        device = models.ForeignKey(Device)
class Advert(models.Model):
	advert = models.FileField(upload_to='adverts')
        page = models.ForeignKey(Page)
        datepub = models.DateTimeField("Published Date")
        expiryend = models.DateTimeField("End Date")
        sponsor = models.CharField("Website", max_length=25)
class StudentQuestions(models.Model):
	student = models.ForeignKey(Student)
        question = models.TextField("Question", max_length=25)
        subject = models.ForeignKey(Subject)
        identifier = models.CharField("Unique ID", max_length=25)
