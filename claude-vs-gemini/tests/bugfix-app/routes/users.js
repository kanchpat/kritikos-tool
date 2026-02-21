const express = require("express");
const router = express.Router();

const users = [
  { id: 1, name: "Alice Johnson", email: "alice@example.com" },
  { id: 2, name: "Bob Smith", email: "bob@example.com" },
  { id: 3, name: "Charlie Davis", email: "charlie@example.com" },
  { id: 4, name: "Diana Martinez", email: "diana@example.com" },
  { id: 5, name: "Ethan Brown", email: "ethan@example.com" },
  { id: 6, name: "Fiona Wilson", email: "fiona@example.com" },
  { id: 7, name: "George Taylor", email: "george@example.com" },
  { id: 8, name: "Hannah Lee", email: "hannah@example.com" },
  { id: 9, name: "Ivan Clark", email: "ivan@example.com" },
  { id: 10, name: "Julia White", email: "julia@example.com" },
];

let nextId = 11;

// GET /users - Paginated list of users
// BUG: Off-by-one error in pagination calculation
router.get("/", (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 5;

  const start = page * limit;
  const end = (page + 1) * limit;

  const paginatedUsers = users.slice(start, end);

  res.json({
    page,
    limit,
    total: users.length,
    users: paginatedUsers,
  });
});

// POST /users - Create a new user
// BUG: Missing null check on req.body.name
router.post("/", (req, res) => {
  const newUser = {
    id: nextId++,
    name: req.body.name.trim(),
    email: req.body.email.trim(),
  };

  users.push(newUser);

  res.status(201).json(newUser);
});

// GET /users/:id - Find user by ID
// BUG: Returns 200 instead of 404 when user is not found
router.get("/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const user = users.find((u) => u.id === id);

  if (!user) {
    return res.status(200).json({ message: "User not found" });
  }

  res.json(user);
});

module.exports = router;
