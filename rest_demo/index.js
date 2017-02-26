// index.js
var faker = require('faker');

module.exports = function() {
	var data = {
		greetings: [],
	}

	// seed init data
	for (var i = 0; i < 20; i++) {
	data.greetings.push({
		id: i,
		first_name: faker.fake("{{name.lastName}}"),
		middle_name: faker.fake("{{name.firstName}}"),
		last_name: faker.fake("{{name.firstName}}"),
		create_date: faker.fake("{{date.past}}"),
		})
	}

  return data
}
