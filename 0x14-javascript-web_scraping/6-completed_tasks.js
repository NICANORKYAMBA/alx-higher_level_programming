#!/usr/bin/node
const request = require('request');

// Make the API request and get the response
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  // Load the response data into a list of objects
  const tasks = JSON.parse(body);

  // Create a dictionary to hold the number of completed tasks for each user
  const completedTasksByUser = {};

  // Loop through the tasks and count the completed tasks for each user
  tasks.forEach(function (task) {
    if (task.completed) {
      const userId = task.userId;
      if (completedTasksByUser[userId]) {
        completedTasksByUser[userId]++;
      } else {
        completedTasksByUser[userId] = 1;
      }
    }
  });

  // Print out the completed tasks for each user
  console.log(completedTasksByUser);
});
