import os
import unittest
import json
import random
from flask_sqlalchemy import SQLAlchemy
from app import app
from model import setup_db, Actors, Movies

# SQLite database for local testing
database_filename = "testcastingAgency.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
TEST_DATABASE_URI = database_path


# Fill in JWTs
CASTING_ASSISTANT = os.getenv('CASTING_ASSISTANT')
CASTING_DIRECTOR = os.getenv('CASTING_DIRECTOR')
EXECUTIVE_PRODUCER = os.getenv('EXECUTIVE_PRODUCER')


class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.casting_assistant = CASTING_ASSISTANT
        self.casting_director = CASTING_DIRECTOR
        self.executive_producer = EXECUTIVE_PRODUCER
        setup_db(self.app, TEST_DATABASE_URI)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

    '''
    RBAC
    '''

# All post requests
# 1)
    def test_post_actors_by_executive_producer_with_auth_200(self):
        response = self.client().post('/actors',
                                      headers={
                                          "Authorization": "Bearer {}"
                                          .format(self.executive_producer)
                                      },
                                      json={
                                          "name": "Edward",
                                          "gender": "male",
                                          "age": 24
                                      })
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

# 2
    def test_post_actors_by_casting_assistant_without_auth_403(self):
        response = self.client().post('/actors',
                                      headers={
                                          "Authorization": "Bearer {}"
                                          .format(self.casting_assistant)
                                      },
                                      json={
                                          "name": "Edward",
                                          "gender": "male",
                                          "age": 24
                                      })
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 403)


# 3


    def test_post_movies_by_executive_producer_with_auth_200(self):
        response = self.client().post('/movies',
                                      headers={
                                          "Authorization": "Bearer {}"
                                          .format(self.executive_producer)
                                      },
                                      json={
                                          "title": "Iron Man",
                                          "releaseDate": "2020/01/01"

                                      })

        data = json.loads(response.data.decode('utf-8').decode('utf-8'))

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

# 4
    def test_post_movies_by_casting_assistant_without_auth_403(self):
        response = self.client().post('/movies',
                                      headers={
                                          "Authorization": "Bearer {}"
                                          .format(self.casting_assistant)
                                      },
                                      json={
                                          "title": "Iron Man",
                                          "releaseDate": "2015/01/01"
                                      })

        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 403)

# 5
    def test_post_movies_by_executive_producer_with_auth_200(self):
        response = self.client().post('/movies',
                                      headers={
                                          "Authorization": "Bearer {}"
                                          .format(self.executive_producer)
                                      },
                                      json={
                                          "title": "Iron Man",
                                          "releaseDate": "2015/01/01"
                                      })

        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

# 6
    def test_post_movies_by_casting_assistant_without_auth_403(self):
        response = self.client().post('/movies',
                                      headers={
                                          "Authorization": "Bearer {}"
                                          .format(self.casting_assistant)
                                      },
                                      json={
                                          "title": "Iron Man",
                                          "releaseDate": "2015/01/01"
                                      })

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 403)

# All get requests
# 1
    def test_get_actors_by_casting_assistant_with_auth_200(self):
        response = self.client().get('/actors',
                                     headers={
                                         "Authorization": "Bearer {}"
                                         .format(self.casting_assistant)
                                     })
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

# 2
    def test_get_actors_by_casting_assistant_without_auth_401(self):
        response = self.client().get('/actors')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')

# 3
    def test_get_movies_by_casting_assistant_with_auth_200(self):
        response = self.client().get('/movies',
                                     headers={
                                         "Authorization": "Bearer {}"
                                         .format(self.casting_assistant)
                                     })
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

# 4
    def test_get_movies_by_casting_assistant_without_auth_401(self):
        response = self.client().get('/movies')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')

# 5
    def test_get_actors_by_casting_assistant_with_auth_200(self):
        response = self.client().get('/actors',
                                     headers={
                                         "Authorization": "Bearer {}"
                                         .format(self.casting_assistant)
                                     })
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

# 6
    def test_get_actors_by_casting_assistant_without_auth_401(self):
        response = self.client().get('/actors')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')

# 7
    def test_get_movies_by_casting_assistant_with_auth_200(self):
        response = self.client().get('/movies',
                                     headers={
                                         "Authorization": "Bearer {}"
                                         .format(self.casting_assistant)
                                     })
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)
# 8

    def test_get_movies_by_casting_assistant_without_auth_401(self):
        response = self.client().get('/movies')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')


# All patch requests
# 1

    def test_patch_actors_by_casting_director_with_auth_200(self):
        random_id = random.choice([actor.id for actor in Actors.query.all()])
        response = self.client().patch('/actors/{}'.format(random_id),
                                       headers={
            "Authorization": "Bearer {}".format(self.casting_director)
        },
            json={
            "name": "David",
            "gender": "other"
        })

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

# 2
    def test_patch_actors_by_casting_assistant_without_auth_403(self):
        random_id = random.choice([actor.id for actor in Actors.query.all()])
        response = self.client().patch('/actors/{}'.format(random_id),
                                       headers={
            "Authorization": "Bearer {}".format(self.casting_assistant)
        },
            json={
            "name": "David",
            "gender": "other"
        })

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

# 3
    def test_patch_movies_by_casting_director_with_auth_200(self):
        random_id = random.choice([movie.id for movie in Movies.query.all()])
        response = self.client().patch('/movies/{}'.format(random_id),
                                       headers={
            "Authorization": "Bearer {}".format(self.casting_director)
        },
            json={
            "title": "Joker",
            "releaseDate": "2019/10/1"
        })

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status_message'], 'OK')

# 4
    def test_patch_movies_by_casting_assistant_without_auth_403(self):
        random_id = random.choice([movie.id for movie in Movies.query.all()])
        response = self.client().patch('/movies/{}'.format(random_id),
                                       headers={
            "Authorization": "Bearer {}".format(self.casting_assistant)
        },
            json={
            "title": "Joker",
            "releaseDate": "2019/10/1"
        })

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

# 5
    def test_patch_actors_by_casting_director_with_auth_200(self):
        random_id = random.choice([actor.id for actor in Actors.query.all()])
        response = self.client().patch('/actors/{}'.format(random_id),
                                       headers={
            "Authorization": "Bearer {}".format(self.casting_director)
        },
            json={
            "name": "David",
            "gender": "other"
        })

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

# 6
    def test_patch_actors_by_casting_assistant_without_auth_403(self):
        random_id = random.choice([actor.id for actor in Actors.query.all()])
        response = self.client().patch('/actors/{}'.format(random_id),
                                       headers={
            "Authorization": "Bearer {}".format(self.casting_assistant)
        },
            json={
            "name": "David",
            "gender": "other",
            "age": 10
        })

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 403)

# 7
    def test_patch_movies_by_casting_director_with_auth_200(self):
        random_id = random.choice([movie.id for movie in Movies.query.all()])
        response = self.client().patch('/movies/{}'.format(random_id),
                                       headers={
            "Authorization": "Bearer {}".format(self.casting_director)
        },
            json={
            "title": "Joker",
            "releaseDate": "2019/10/1"
        })

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

# 8
    def test_patch_movies_by_casting_assistant_without_auth_403(self):
        random_id = random.choice([movie.id for movie in Movies.query.all()])
        response = self.client().patch('/movies/{}'.format(random_id),
                                       headers={
            "Authorization": "Bearer {}".format(self.casting_assistant)
        },
            json={
            "title": "Joker",
            "releaseDate": "2019/10/1"
        })

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 403)


# All delete requests
# 1


    def test_delete_actors_by_executive_producer_with_auth_200(self):
        random_id = random.choice([actor.id for actor in Actors.query.all()])
        response = self.client().delete('actors/{}'.format(random_id),
                                        headers={
                                            "Authorization": "Bearer {}"
                                            .format(self.executive_producer)
        }
        )
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status_message'], 'OK')

# 2
    def test_delete_actors_by_casting_assistant_without_auth_403(self):
        random_id = random.choice([actor.id for actor in Actors.query.all()])
        response = self.client().delete('actors/{}'.format(random_id),
                                        headers={
                                            "Authorization": "Bearer {}"
                                            .format(self.casting_assistant)
        }
        )
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

# 3
    def test_delete_movies_by_executive_producer_with_auth_200(self):
        random_id = random.choice([movie.id for movie in Movies.query.all()])
        response = self.client().delete('movies/{}'.format(random_id),
                                        headers={
                                            "Authorization": "Bearer {}"
                                            .format(self.executive_producer)
        }
        )
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status_message'], 'OK')

# 4
    def test_delete_movies_by_casting_assistant_without_auth_403(self):
        random_id = random.choice([movie.id for movie in Movies.query.all()])
        response = self.client().delete('movies/{}'.format(random_id),
                                        headers={
                                            "Authorization": "Bearer {}"
                                            .format(self.casting_assistant)
        }
        )
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 403)

# 5
    def test_delete_actors_by_executive_producer_with_auth_200(self):
        random_id = random.choice([actor.id for actor in Actors.query.all()])
        response = self.client().delete('actors/{}'.format(random_id),
                                        headers={
                                            "Authorization": "Bearer {}"
                                            .format(self.executive_producer)
        }
        )
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)
# 6

    def test_delete_actors_by_casting_assistant_without_auth_403(self):
        random_id = random.choice([actor.id for actor in Actors.query.all()])
        response = self.client().delete('actors/{}'.format(random_id),
                                        headers={
                                            "Authorization": "Bearer {}"
                                            .format(self.casting_assistant)
        }
        )
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

# 7
    def test_delete_movies_by_executive_producer_with_auth_200(self):
        random_id = random.choice([movie.id for movie in Movies.query.all()])
        response = self.client().delete('movies/{}'.format(random_id),
                                        headers={
                                            "Authorization": "Bearer {}"
                                            .format(self.executive_producer)
        }
        )
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)
# 8

    def test_delete_movies_by_casting_assistant_without_auth_403(self):
        random_id = random.choice([movie.id for movie in Movies.query.all()])
        response = self.client().delete('movies/{}'.format(random_id),
                                        headers={
                                            "Authorization": "Bearer {}"
                                            .format(self.casting_assistant)
        }
        )
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 403)


if __name__ == '__main__':
    unittest.main()
