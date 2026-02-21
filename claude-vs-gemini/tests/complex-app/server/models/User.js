const bcrypt = require('bcryptjs');

// In-memory user store
// In production, this would be a database (e.g. MongoDB, PostgreSQL)
const users = [];
let nextId = 1;

// Seed a demo user
const SALT_ROUNDS = 10;
const demoPasswordHash = bcrypt.hashSync('password123', SALT_ROUNDS);
users.push({
  id: nextId++,
  name: 'Demo User',
  email: 'demo@example.com',
  password: demoPasswordHash,
  createdAt: new Date().toISOString(),
});

function findByEmail(email) {
  return users.find((u) => u.email === email) || null;
}

function findById(id) {
  return users.find((u) => u.id === id) || null;
}

async function create({ name, email, password }) {
  const existing = findByEmail(email);
  if (existing) {
    throw new Error('User with this email already exists');
  }

  const hashedPassword = await bcrypt.hash(password, SALT_ROUNDS);
  const user = {
    id: nextId++,
    name,
    email,
    password: hashedPassword,
    createdAt: new Date().toISOString(),
  };

  users.push(user);
  return user;
}

async function validatePassword(plainPassword, hashedPassword) {
  return bcrypt.compare(plainPassword, hashedPassword);
}

module.exports = { findByEmail, findById, create, validatePassword };
