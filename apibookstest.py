import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from werkzeug.exceptions import HTTPException
from models import setup_db, Livre,Categorie
from config import myTokens

access_token_auth_header = {'Authorization': myTokens['access_token']}


class BooksapitestCase(unittest.TestCase):
    """This class represents the apibookstest test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "apibooks_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
    'postgres', 'esso', 'localhost:5432', self.database_name)


        setup_db(self.app, self.database_path)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        self.new_categorie = {
            'libelle': 'categorie',
            'description':'Description de la categorie'
        }
        self.new_update_categorie = {
            'libelle': 'categorie update',
            'description':'Description de la categorie update'
        }
        self.new_livre = {
            "categorie_id": 1,
            "dateparution": "Thu, 05 Feb 1998 00:00:00 GMT",
            "editeur": "editeur1",
            "isbn": "isbn1",
            "titre": "titre1",
            "version": "version1"
        }
        self.new_update_livre = {
            "categorie_id": 1,
            "dateparution": "Thu, 05 Feb 1998 00:00:00 GMT",
            "editeur": "editeur update",
            "isbn": "isbn update",
            "titre": "titre update",
            "version": "version update"
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_all_categories(self):
        res = self.client().get('/categories',headers=access_token_auth_header)
        # ici on récupère les données provenant de la Response
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['categories']))

    def test_get_all_livres(self):
        res = self.client().get('/livres',headers=access_token_auth_header)
        # ici on récupère les données provenant de la Response
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['livres'])
        self.assertTrue(len(data['livres']))
    
    def test_create_new_categorie(self):
        res=self.client().post('/categories', json = self.new_categorie,headers=access_token_auth_header)
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['categories']))

    def test_create_new_livre(self):
        res=self.client().post('/livres', json = self.new_livre,headers=access_token_auth_header)
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['livres'])
        self.assertTrue(len(data['livres']))
    """ 
    def test_delete_categorie(self):
        res=self.client().delete('/categories/16', headers=access_token_auth_header)
        data=json.loads(res.data)
        #categorie=Categorie.query.filter(Categorie.id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], "Suppression effectuée avec succès")
        self.assertEqual(data['id'], 16)
        self.assertTrue(data['categories'])
        self.assertTrue(data['nombre_categorie'])

    def test_delete_livre(self):
        res=self.client().delete('/livres/2', headers=access_token_auth_header)
        data=json.loads(res.data)
        #categorie=Categorie.query.filter(Categorie.id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], "Suppression effectuée avec succès")
        self.assertEqual(data['id'], 2)
        self.assertTrue(data['livre'])
        self.assertTrue(data['nombre_livre']) 
    """
    
    def test_get_categorie(self):
        res=self.client().get('/categories/1', headers=access_token_auth_header)
        data=json.loads(res.data)
        #categorie=Categorie.query.filter(Categorie.id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['id'], 1)
        self.assertTrue(data['categorie'])

    def test_get_categorie_livres(self):
        res=self.client().get('/categories/1/livres', headers=access_token_auth_header)
        data=json.loads(res.data)
        #categorie=Categorie.query.filter(Categorie.id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['categorie_id'], 1)
        self.assertTrue(data['livres'])
        self.assertTrue(data['nombre_livre'])
    
    def test_get_livree(self):
        res=self.client().get('/livres/1', headers=access_token_auth_header)
        data=json.loads(res.data)
        #categorie=Categorie.query.filter(Categorie.id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['id'], 1)
        self.assertTrue(data['livre'])
    
    def test_categorie_which_does_not_exist(self):
        res=self.client().delete('/categories/1000',headers=access_token_auth_header)
        data=json.loads(res.data)
        categorie=Categorie.query.filter(Categorie.id == 1000).one_or_none()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    

    def test_update_categorie(self):
        res = self.client().patch('/categories/1', json=self.new_update_categorie,
                                  headers=access_token_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'],"modification effectuée avec succès")
        self.assertEqual(data['id'], 1)
        self.assertTrue(data['categorie'])

    def test_update_livre(self):
        res = self.client().patch('/livres/1', json=self.new_update_livre,
                                  headers=access_token_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'],"Modification effectuée avec succès")
        self.assertEqual(data['id'], 1)
        self.assertTrue(data['livre'])



# # Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()