# -*- coding: utf-8 -*-
import time,uuid

from transwarp.db import next_id
from transwarp.orm import Model,StringField,BooleanField,FloatField,TextField

class Contact(Model):
    __table__ = 'contact'

    id = StringField(primary_key=True,updatable=False,default=next_id,dll='varchar(50)')
    name = StringField(ddl='varchar(50)')
    tel = StringField(ddl='varchar(50)')
    work_tel = StringField(ddl='varchar(50)')
    sex = StringField(ddl='varchar(50)')
    college = StringField(ddl='varchar(50)')
    headman = BooleanField()
    groupid = StringField(ddl='varchar(50)')
    year = StringField(ddl='varchar(50)')

