// MongoDB initialization script for development environment
// This script runs when the MongoDB container starts for the first time

// Create the mainframe database
db = db.getSiblingDB('mainframe');

// Create a user for the mainframe database
db.createUser({
  user: 'mainframe_user',
  pwd: 'dev_password',
  roles: [
    {
      role: 'readWrite',
      db: 'mainframe'
    }
  ]
});

// Create some initial collections if needed
db.createCollection('users');
db.createCollection('projects');
db.createCollection('repositories');
db.createCollection('assessments');
db.createCollection('chats');

print('MongoDB initialization completed successfully');
