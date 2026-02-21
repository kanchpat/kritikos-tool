# Bugfix App

A simple Express.js REST API for managing users. This app contains **3 intentional bugs** that need to be found and fixed.

## Setup

```bash
npm install
npm start
```

The server runs on `http://localhost:3000`.

## Endpoints

- `GET /users?page=1&limit=5` - Returns a paginated list of users
- `POST /users` - Creates a new user (expects JSON body with `name` and `email`)
- `GET /users/:id` - Returns a single user by ID

## Known Bugs

### Bug 1: Off-by-one error in pagination (`GET /users`)

The pagination logic in `routes/users.js` calculates the wrong slice indices. Requesting page 1 skips the first set of results entirely and returns what should be page 2. The `start` and `end` values use `page * limit` and `(page + 1) * limit` instead of the correct `(page - 1) * limit` and `page * limit`.

### Bug 2: Missing null check causes crash (`POST /users`)

Sending a POST request to `/users` with an empty body or without a `name` field causes the server to crash with a `TypeError: Cannot read properties of undefined`. The code calls `req.body.name.trim()` without first checking whether `req.body` or `req.body.name` exists.

### Bug 3: Wrong status code for missing user (`GET /users/:id`)

When a user is not found by ID, the endpoint returns HTTP status `200` with `{ "message": "User not found" }` instead of the correct `404` status code. This makes it impossible for clients to distinguish between a successful response and a not-found error.
