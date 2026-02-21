import React, { useState, useEffect } from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { getDashboard } from '../services/api';

function Dashboard() {
  const { user, logout } = useAuth();
  const [dashboardData, setDashboardData] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    getDashboard()
      .then((data) => setDashboardData(data))
      .catch((err) => setError(err.message));
  }, []);

  // Redirect if not authenticated (safety check beyond ProtectedRoute)
  if (!user) {
    return <Navigate to="/login" replace />;
  }

  return (
    <div className="dashboard-page">
      <header className="dashboard-header">
        <h1>Dashboard</h1>
        <div className="user-info">
          <span>Welcome, {user.name}</span>
          <button onClick={logout}>Sign Out</button>
        </div>
      </header>

      {error && <div className="error-message">{error}</div>}

      {dashboardData ? (
        <div className="dashboard-content">
          <div className="stats-grid">
            <div className="stat-card">
              <h3>Projects</h3>
              <p>{dashboardData.stats.projectsCount}</p>
            </div>
            <div className="stat-card">
              <h3>Completed</h3>
              <p>{dashboardData.stats.tasksCompleted}</p>
            </div>
            <div className="stat-card">
              <h3>In Progress</h3>
              <p>{dashboardData.stats.tasksInProgress}</p>
            </div>
            <div className="stat-card">
              <h3>Notifications</h3>
              <p>{dashboardData.stats.notifications}</p>
            </div>
          </div>

          <div className="recent-activity">
            <h2>Recent Activity</h2>
            <ul>
              {dashboardData.recentActivity.map((item) => (
                <li key={item.id}>
                  <span>{item.action}</span>
                  <time>{new Date(item.timestamp).toLocaleDateString()}</time>
                </li>
              ))}
            </ul>
          </div>
        </div>
      ) : (
        !error && <p className="loading">Loading dashboard...</p>
      )}
    </div>
  );
}

export default Dashboard;
