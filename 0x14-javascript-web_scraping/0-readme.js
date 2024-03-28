#!/usr/bin/node

const fs = requre('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
	if (err) {
		console.log(err);
	} else {
	console.log(data);
	}
});
