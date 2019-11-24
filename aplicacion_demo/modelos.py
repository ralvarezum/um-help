from . import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

automovil_persona = Table('association', Base.metadata,
                          Column('automovil_id', Integer, ForeignKey('automovil.id')),
                          Column('persona_id', Integer, ForeignKey('persona.id'))
                          )

class AutoPersona(db.Model):
    __tablename__ = 'autopersona'
    automovil_id = Column(Integer, ForeignKey('automovil.id'), primary_key=True)
    persona_id = Column(Integer, ForeignKey('persona.id'), primary_key=True)

class Automovil(db.Model):
    __tablename__ = 'automovil'
    id = db.Column(db.Integer,
                   primary_key=True)
    marca = db.Column(db.String(64),
                       index=False,
                       unique=False,
                       nullable=False)
    modelo = db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    creado = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    activo = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)
    personas = relationship("Persona", secondary='autopersona')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        automoviles = Automovil.query.all()
        return automoviles

    def __repr__(self):
        return '<Automovil {}, {}>'.format(self.marca, self.modelo)

class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer,
                   primary_key=True)
    nombre = db.Column(db.String(64),
                       index=False,
                       unique=False,
                       nullable=False)
    apellido = db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    creado = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    activo = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)
    automoviles = relationship("Automovil", secondary='autopersona')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        personas = Persona.query.all()
        return personas

    def __repr__(self):
        return '<Persona {}, {}>'.format(self.apellido, self.nombre)
