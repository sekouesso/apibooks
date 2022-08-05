from flask import Flask,request,jsonify,abort,render_template
from werkzeug.exceptions import HTTPException
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from flask_cors import CORS
from models import setup_db, Livre,Categorie
from dotenv import load_dotenv

import os

from flask_migrate import Migrate
from datetime import datetime
from auth import requires_auth


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    load_dotenv()


    """ motdepasse = os.getenv('motdepasse')
    motdepasse = quote_plus(motdepasse)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:{}@localhost:5432/apibooks_db".format(
        motdepasse)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') """


    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                                'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                                'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response

 
    @app.route('/livres')
    def list_livres():
        livres = Livre.query.all()
        return jsonify({
            'nombre_livre': len(livres),
            'livres':[livre.format() for livre in livres]
        })

    @app.route('/livres/<int:id>')
    def un_livre(id):
        livre = Livre.query.get(id)
        if not livre:
            abort(404)
        else:
            return jsonify({
                'id':id,
                'livre':livre.format()
            })

    @app.route('/livres',methods=['POST','GET'])
    def add_livre():
        body = request.get_json()
        new_isbn = body.get('isbn', None)
        new_titre = body.get('titre', None)
        new_dateparution = body.get('dateparution', None)
        new_editeur = body.get('editeur', None)
        new_version = body.get('version', None)
        new_categorie_id = body.get('categorie_id', None)
        if not new_isbn or not new_titre or not new_dateparution or not new_editeur or not new_version or not new_categorie_id:
            abort(404)
        else:
            livre = Livre(isbn=new_isbn, titre=new_titre,dateparution=new_dateparution, editeur=new_editeur, version=new_version,categorie_id=new_categorie_id)
            db.session.add(livre)
            db.session.commit()
            livres = Livre.query.all()
            return jsonify({
                'id':livre.id,
                'nombre_livre': len(livres),
                'livres':[livre.format() for livre in livres]
            })

    @app.route('/livres/<int:id>', methods=['GET','PATCH'])
    def update_livres(id):
        livre = Livre.query.get(id)
        body = request.get_json()
        new_isbn = body.get('isbn', None)
        new_titre = body.get('titre', None)
        new_dateparution = body.get('dateparution', None)
        new_editeur = body.get('editeur', None)
        new_version = body.get('version', None)
        new_categorie_id = body.get('categorie_id', None)
        if not livre:
            abort(404)
        if not new_isbn or not new_titre or not new_dateparution or not new_editeur or not new_version or not new_categorie_id:
            abort(404)
        else:
            livre.isbn = new_isbn
            livre.titre = new_titre
            livre.dateparution = new_dateparution
            livre.version = new_version
            livre.editeur = new_editeur
            livre.categori_id = new_categorie_id
            db.session.commit()
            return jsonify({
                "message":"Modification effectuée avec succès",
                'id': id,
                'livre':livre.format()
            })

    @app.route('/livres/<int:id>',methods=['DELETE','GET'])
    def delete_livre(id):
        livre = Livre.query.get(id)
        if not livre:
            abort(404)
        else:
            db.session.delete(livre)
            db.session.commit()
            livres = Livre.query.all()
            return jsonify({
                "message":"Suppression effectuée avec succès",
                'id': id,
                'livres':[livre.format() for livre in livres],
                'nombre_livre': len(livres)
                })

    @app.route('/categories')
    def list_categories():
        categories = Categorie.query.all()
        return jsonify({
            'nombre_categorie':len(categories),
            'categories':[categorie.format() for categorie in categories]
        })

    @app.route('/categories/<int:id>')
    def un_categorie(id):
        categorie = Categorie.query.get(id)
        if categorie is None:
            abort(404)
        else:
            return jsonify({
                'id':id,
                'categorie':categorie.format()
            })

    @app.route('/categories/<int:id>/livres')
    def get_livres_by_category(id):
        categorie = Categorie.query.get(id)
        if categorie is None:
            abort(404)
        else:
            livres = Livre.query.filter(Livre.categorie_id==id).all()
            return jsonify({
            'nombre_livre': len(livres),
            'livres':[livre.format() for livre in livres],
            'categorie_id': categorie.id
        })

    @app.route('/categories', methods=['GET','POST'])
    def add_category():
        body = request.get_json()
        new_libelle = body.get('libelle', None)
        new_description = body.get('description', None)
        if not new_libelle or not new_description:
            abort(404)
        else:
            categorie = Categorie(libelle=new_libelle, description=new_description)
            db.session.add(categorie)
            db.session.commit()
            categories = Categorie.query.all()
            return jsonify({
                'nombre_categorie':len(categories),
                'categories':[categorie.format() for categorie in categories]
            })

    @app.route('/categories/<int:id>',methods=['GET','PATCH'])
    def update_categorie(id):
        categorie = Categorie.query.get(id)
        if categorie is None:
            abort(404)
        body = request.get_json()
        new_libelle = body.get('libelle', None)
        new_description = body.get('description', None)
        if not new_libelle or not new_description:
            abort(404)
        else:
            categorie.libelle = new_libelle
            categorie.description = new_description
            db.session.commit()
            return jsonify({
                "message":"modification effectuée avec succès",
                'id':id,
                'categorie':categorie.format()
            })

    @app.route('/categories/<int:id>', methods=['GET','DELETE'])
    def delete_categorie(id):
        categorie = Categorie.query.get(id)
        if categorie is None:
            abort(404)
        else:
            db.session.delete(categorie)
            db.session.commit()
            categories = Categorie.query.all()
            return jsonify({
                "message":"Suppression effectuée avec succès",
                'nombre_categorie':len(categories),
                'categories':[categorie.format() for categorie in categories],
                'id':id
            })




    # les errorhandler permettent de capturer les erreurs
    @app.errorhandler(422)
    def unprocessable(error):
        return (jsonify({'success': False, 'error': 422,
                'message': 'Unprocessable'}), 422)

    @app.errorhandler(400)
    def bad_request(error):
        return (jsonify({'success': False, 'error': 400,
                'message': 'Bad request'}), 400)

    @app.errorhandler(401)
    def bad_request(error):
        return (jsonify({'success': False, 'error': 401,
                'message': 'Unauthorized'}), 401)

    @app.errorhandler(403)
    def bad_request(error):
        return (jsonify({'success': False, 'error': 403,
                'message': 'Forbidden'}), 403)

    @app.errorhandler(404)
    def ressource_not_found(error):
        return (jsonify({'success': False, 'error': 404,
                'message': 'Not found'}), 404)
        
    @app.errorhandler(500)
    def iternal_server_error(error):
        return (jsonify({'success': False, 'error': 500,
                'message': 'Internal server error'}), 500)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)#host='0.0.0.0', port=8080,

