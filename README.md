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

## Tests

To run the tests, run `python3 tests.py`.
