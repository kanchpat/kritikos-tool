// Application configuration
// In production, these would come from environment variables

const config = {
  JWT_SECRET: process.env.JWT_SECRET || 'my-super-secret-jwt-key-change-in-production',
  PORT: process.env.PORT || 5000,
  TOKEN_EXPIRY: '24h',
};

module.exports = config;
