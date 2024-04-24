#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(body);
    const completedTasksByUser = {};

    tasks.forEach(function (task) {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  }
});
