# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Lessonlist(models.Model):
    id = models.IntegerField(primary_key=True)
    yk_clicks = models.IntegerField(db_column='yk_Clicks', blank=True, null=True)  # Field name made lowercase.
    yk_ageclass = models.IntegerField(db_column='yk_AgeClass', blank=True, null=True)  # Field name made lowercase.
    yk_secondclassid = models.IntegerField(db_column='yk_SecondClassID', blank=True, null=True)  # Field name made lowercase.
    yk_lessonlistname = models.CharField(db_column='yk_LessonListName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lessonlist'
