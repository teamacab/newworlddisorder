from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *
from sqlalchemy.pool import StaticPool

import clr
clr.AddReference("IronPython.SQLite")
Base = declarative_base()
"""
class Singleton(object):
 
    '''
 
    Singelton class
 
    '''
 
    def __init__(self, decorated):
 
        self._decorated = decorated
 
    def instance(self, *args, **kwargs):
 
        try:
 
            return self._instance
 
        except AttributeError:
 
            self._instance = self._decorated(*args, **kwargs)
 
            return self._instance
 
    def __call__(self, *args, **kwargs):
 
        raise TypeError('Singletons must be accessed through the `Instance` method.')
 
@Singleton
"""
engine = create_engine('mysql://root@localhost/ex?charset=utf8&use_unicode=0', echo=True)
DBSession = scoped_session(
	sessionmaker(
		autoflush=False,
		expire_on_commit=False,
		autocommit=True,
		bind=engine
	)
)
session = DBSession()
session.expire_on_commit=False
session.autoflush=False
session.autocommit=True

def getSession():
	return session

def getEngine():
	return engine
"""
def getSession():
	if session is None:
		initDB()
	return session
"""

	

class Model():
 
    '''
 
    This is a baseclass with delivers all basic database operations
 
    '''
 
    def save(self):
		from ex.database import getSession 
		sess = getSession()
		sess.begin(subtransactions=True)
		try:
			sess.add(self)
			sess.flush()
			sess.commit()
		except:
			sess.rollback()
			sess.begin(subtransactions=True)
			try:
				sess.add(self)
				sess.flush()
				sess.commit()
			except:
				sess.rollback()
				raise
				

		return True
		

    def saveMultiple(self,objects = []):
 		from ex.database import getSession 
		sess = getSession()
		sess.begin(subtransactions=True)
		try:
			sess.add_all(objects)
			sess.flush()
			sess.commit()
		except:
			sess.rollback()
			sess.begin(subtransactions=True)
			try:
				sess.add_all(objects)
				sess.flush()
				sess.commit()
			except:
				sess.rollback()
				raise
				

		return True
    def update(self):
		from ex.database import getSession 
		sess = getSession()
		sess.begin(subtransactions=True)
		sess.commit()
		sess.flush()
		
    def delete(self):
 		from ex.database import getSession 
		sess = getSession()
		try:
			
			sess.delete(self)
			sess.commit()
		except:
			sess.rollback()
			raise
		
		return self
 
    def queryObject(self):
		from ex.database import getSession
		return getSession().query(self.__class__)



class Unit(Model,Base):
	__tablename__ = 'units'
	
	
	id = Column(Integer, primary_key=True)
	netid = Column(String(255))
	clazz = Column(String(255))
	posATL = Column(String(255))
	posASL = Column(String(255))
	animation = Column(String(255))
	damage = Column(String(255))
	alive = Column(String(255))
	weapons = Column(String(255))
	magazines = Column(String(255))
	items = Column(String(255))
	headgear = Column(String(255))
	uniform = Column(String(255))
	vest = Column(String(255))
	backpack = Column(String(255))
	backpackCargo = Column(String(255))
	uniformItems = Column(String(255))
	vestItems = Column(String(255))
	vehicle = Column(String(255))
	vehiclePos = Column(String(255))
	variables = relationship("Variable")
	rank = Column(String(255))
	skill = Column(String(255))
	name = Column(String(255))
	varname = Column(String(255))
	
class Player(Model,Base):
	__tablename__ = 'player'
	id = Column(Integer, primary_key=True)
	uid = Column(String(255))
	netid = Column(String(255))
	clazz = Column(String(255))
	posATL = Column(String(255))
	posASL = Column(String(255))
	animation = Column(String(255))
	damage = Column(String(255))
	alive = Column(String(255))
	weapons = Column(String(255))
	magazines = Column(String(255))
	items = Column(String(255))
	headgear = Column(String(255))
	uniform = Column(String(255))
	vest = Column(String(255))
	backpack = Column(String(255))
	backpackCargo = Column(String(255))
	uniformItems = Column(String(255))
	vestItems = Column(String(255))
	vehicle = Column(String(255))
	vehiclePos = Column(String(255))
	variables = relationship("Variable")
	rank = Column(String(255))
	skill = Column(String(255))
	name = Column(String(255))
	varname = Column(String(255))
	
	
class Variable(Model,Base):
	__tablename__ = 'variables'
	id = Column(Integer, primary_key=True)
	key = Column(String(255))
	value = Column(String(255))
	unit_id = Column(Integer, ForeignKey('units.id'))
	player_id = Column(Integer, ForeignKey('player.id'))
	
## Create all Tables 
Base.metadata.create_all(engine)
