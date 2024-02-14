#!/usr/bin/node

const fs = require('fs');

const contentA = fs.readFileSync(process.argv[2]).toString() + '\n';
const contentB = fs.readFileSync(process.argv[3]).toString() + '\n';
const filePath = process.argv[4];
fs.writeFileSync(filePath, contentA + contentB);
