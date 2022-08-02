import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
   
 ###################################################################################################################
#
#                                       HERE I HAVE MAKE M CONNECTION STRING
#
###################################################################################################################
database_name = "apibooks_db"
database_path = "postgresql://{}:{}@{}/{}".format(
    'postgres', 'esso', 'localhost:5432', database_name)
db = SQLAlchemy() 
ENV = "prod" 

'''
setup_db(app)
'''
###################################################################################################################
#
#
#                                        SET UP MY APPLICATION BY CONNEXION STRING AND MIGRATION
#
###################################################################################################################
#postgres://wcwkgcuuvhrftu:0c54c19e290e32c8d1f0b6a490117f05c7ec854d8a2ce28228d83a8489d48ce8@ec2-44-206-197-71.compute-1.amazonaws.com:5432/d54h518j7q2f07

def setup_db(app, db_path=database_path):
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = \
                'postgres://wcwkgcuuvhrftu:0c54c19e290e32c8d1f0b6a490117f05c7ec854d8a2ce28228d83a8489d48ce8@ec2-44-206-197-71.compute-1.amazonaws.com:5432/d54h518j7q2f07'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    #db.create_all()  #Cette ligne est décommentée si on souhaite créer automatiquement la base de données au lancement
    # de l'appplication
    migrate = Migrate(app, db)

class Categorie(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    livres = db.relationship(
        'Livre', backref=db.backref('categories', lazy=True))
    
    def __init__(self,libelle,description):
        self.libelle = libelle
        self.description = description
    
    def format(self):
        return {
            'id': self.id,
            'libelle': self.libelle,
            'description': self.description
        }



class Livre(db.Model):
    __tablename__='livres'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(50), nullable=False)
    titre = db.Column(db.String(50), nullable=False)
    dateparution = db.Column(db.DateTime(), nullable=False,default=datetime.utcnow)
    editeur = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categories.id'),
                        nullable=False)
    

    def __init__(self,isbn,titre,dateparution,editeur,version,categorie_id):
        self.isbn = isbn
        self.titre = titre
        self.dateparution = dateparution
        self.editeur = editeur
        self.version = version
        self.categorie_id = categorie_id
    
    def format(self):
        return {
            'id': self.id,
            'isbn': self.isbn,
            'titre': self.titre,
            'dateparution': self.dateparution,
            'version': self.version,
            'editeur': self.editeur,
            'categorie_id': self.categorie_id
        }
