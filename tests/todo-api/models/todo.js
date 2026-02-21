let todos = [
  { id: 1, title: 'Buy groceries', completed: false },
  { id: 2, title: 'Walk the dog', completed: true },
  { id: 3, title: 'Read a book', completed: false },
];

let nextId = 4;

function getAll() {
  return todos;
}

function getById(id) {
  return todos.find((todo) => todo.id === id);
}

function create(todo) {
  const newTodo = {
    id: nextId++,
    title: todo.title,
    completed: false,
  };
  todos.push(newTodo);
  return newTodo;
}

function update(id, data) {
  const todo = todos.find((t) => t.id === id);
  if (!todo) return null;
  if (data.title !== undefined) todo.title = data.title;
  if (data.completed !== undefined) todo.completed = data.completed;
  return todo;
}

function remove(id) {
  const index = todos.findIndex((t) => t.id === id);
  if (index === -1) return null;
  return todos.splice(index, 1)[0];
}

module.exports = { getAll, getById, create, update, remove };
