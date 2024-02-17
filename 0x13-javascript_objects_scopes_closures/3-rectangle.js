#!/usr/bin/node

const Rectagle = class {
	constructor (w, h) {
		if (typeof w === 'integer' && w > 0 && typeof h === 'integer' && h > 0) {
			this.width = w;
			this.height = h;
		}
	};

	print () {
		for (let i = 0; i < this.height; i++) {
			let myNum = '';
			let y = 0;
			while (y < this.width) {
				myNum += 'X';
				y++;
			}

			console.log(myNum);
		}
	}
};
module.exports = Rectangle;
