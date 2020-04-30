# Casting Agency

Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

## Motivation

This is my capstone project for the Udacity Full Stack Developer nanodegree.

## Dependencies

All dependencies are listed in the `requirements.txt` file.
They can be installed by running `pip3 install -r requirements.txt`.

## Authentication

The API has three registered users:

1. Assistant

2. Director

3. Producer

The Auth0 domain and api audience can be found in `setup.sh`.

## Demo Page  

https://casting-agency-webapp.herokuapp.com

Test each endpoint with the link above ,and different role's Jwts.
JWTs for different role can be accessed by login to the link with username and password provided as follows.
https://kprod.auth0.com/authorize?audience=castingAgency&response_type=token&client_id=WwlsQzNVr9q37zz71Crr6zTofItGU9ZI&redirect_uri=http://localhost:5432/login-results

```
- Casting Assistant
    - UserName: casting.assistant@whatever.com
    - Password: Password!
- Casting Director
    - UserName: casting.director@whatever.com
    - Password: Password!
- Executive Producer
    - UserName: executive.producer@whatever.com
    - Password: Password!
```

## Endpoints

### `GET /movies`

Gets all movies from the db.

Response:

```json5
{
  movies: [
    {
      id: 1,
      release_date: "2021-02-02",
      title: "Titanic II"
    },
    {
      id: 2,,
      release_date: "2008-01-01",
      title: "Dark Knight"
    }
  ],
  success: true
}
```

### `POST /movies`

Adds a new movie to the db.

Data:

```json5
{
  title: "2008-01-01",
  release_date: "Dark Knight"
}
```

Response:

```json5
{
  success: true,
  movie: [
    {
      id: 2,
      release_date: "2021-02-02",
      title: "Dark Knight"
    }
  ]
}
```

### `PATCH /movies/<int:id>`

Edit data on a movie in the db.

Data:

```json5
{
  title: "Dark Knight",
  release_date: "2021/02/02"
}
```

Response:

```json5
{
  success: true,
  movie: [
    {
      id: 2,
      release_date: "2021-02-02",
      title: "Dark Knight"
    }
  ]
}
```

### `DELETE /movies/<int:id>`

Delete a movie from the db.

Response:

```json5
{
  success: true
}
```

### `GET /actors`

Gets all actors from the db.

Response:

```json5
{
  actors: [
    {
      gender: "Male",
      id: 1,
      name: "C.Bale"
    },
    {
      gender: "Male",
      id: 2,
      name: "Robert Downey Jr"
    }
  ],
  success: true
}
```

### `POST /actors`

Adds a new actor to the db.

Data:

```json5
{
  name: "name",
  gender: "Female"
}
```

Response:

```json5
{
  success: true,
  actor: "name"
}
```

### `PATCH /actors/<int:id>`

Edit data on a actor in the db.

Data:

```json5
{
  name: "new name",
  gender: "M"
}
```

Response:

```json5
{
  success: true,
  actor: [
    {
      gender: "M",
      id: 1,
      name: "new name"
    }
  ]
}
```

### `DELETE /actors/<int:id>`

Delete a actor from the db.

Response:

```json5
{
  success: true
}
```
