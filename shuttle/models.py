from django.db import models

class Node(models.Model):
	name = models.CharField(max_length=255)
	image = models.ImageField(upload_to='nodes')
	# geo_loc = "2222,4444" 
	# first:latitude second:longitude
	geo_loc = models.CharField(max_length=255)

class Route(models.Model):
	start = models.ForeignKey(Node, related_name='start')
	destination = models.ForeignKey(Node, related_name='destination')

class Time(models.Model):
	route= models.ForeignKey(Route, related_name='time')
	time = models.TimeField()
