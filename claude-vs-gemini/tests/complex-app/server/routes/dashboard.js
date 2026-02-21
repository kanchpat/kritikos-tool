const express = require('express');
const authenticate = require('../middleware/auth');

const router = express.Router();

// GET /api/dashboard - Protected route returning dashboard data
router.get('/dashboard', authenticate, (req, res) => {
  // In a real app, these stats would come from a database
  const dashboardData = {
    user: {
      id: req.user.id,
      name: req.user.name,
      email: req.user.email,
    },
    stats: {
      projectsCount: 12,
      tasksCompleted: 47,
      tasksInProgress: 8,
      notifications: 3,
    },
    recentActivity: [
      { id: 1, action: 'Completed task "Update landing page"', timestamp: '2024-01-15T10:30:00Z' },
      { id: 2, action: 'Created project "Mobile App v2"', timestamp: '2024-01-14T16:45:00Z' },
      { id: 3, action: 'Commented on "API redesign"', timestamp: '2024-01-14T09:15:00Z' },
    ],
  };

  res.json(dashboardData);
});

module.exports = router;
