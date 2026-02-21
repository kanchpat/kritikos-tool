const express = require('express');
const router = express.Router();
const Todo = require('../models/todo');

// List all todos
router.get('/', (req, res) => {
  res.json(Todo.getAll());
});

// Get a single todo
router.get('/:id', (req, res) => {
  const todo = Todo.getById(parseInt(req.params.id));
  if (!todo) {
    return res.status(404).json({ error: 'Todo not found' });
  }
  res.json(todo);
});

// Create a new todo
router.post('/', (req, res) => {
  if (!req.body.title) {
    return res.status(400).json({ error: 'Title is required' });
  }
  const todo = Todo.create({ title: req.body.title });
  res.status(201).json(todo);
});

// Update a todo
router.put('/:id', (req, res) => {
  const todo = Todo.update(parseInt(req.params.id), req.body);
  if (!todo) {
    return res.status(404).json({ error: 'Todo not found' });
  }
  res.json(todo);
});

// Delete a todo
router.delete('/:id', (req, res) => {
  const todo = Todo.remove(parseInt(req.params.id));
  if (!todo) {
    return res.status(404).json({ error: 'Todo not found' });
  }
  res.json(todo);
});

module.exports = router;
