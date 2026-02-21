const express = require('express');
const todoRoutes = require('./routes/todos');

const app = express();
const PORT = 3001;

app.use(express.json());

app.use('/todos', todoRoutes);

app.listen(PORT, () => {
  console.log(`Todo API server running on port ${PORT}`);
});
