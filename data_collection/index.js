const express = require('express')
const bodyParser = require('body-parser')
const fs = require('fs')
const app = express()
const port = 7788

const jokes = JSON.parse(fs.readFileSync('jokes-1213.json', {encoding:'utf8'}))
const njokes = jokes.length

app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());
app.use(express.static('images'));

app.get('/', function(req, res){
	res.sendFile(__dirname + '/index.html');
});

app.get('/joke', (req, res) => {
	var current = parseInt(req.query.current, 10) || 0
	var next = (current + 1) % njokes;
	res.json({
		id: next,
		joke: jokes[next],
		njokes: njokes
	})
})

app.post('/label', function (req, res) {
	console.log(req.body)
	const joke_id = req.body.joke_id;
	const label = req.body.label;
	const participant = req.body.participant;
	const date = new Date()

	fs.appendFileSync(
		'user_labels', 
		`[${date.toLocaleString()}][${Math.floor(date.getTime()/1000)}] ${joke_id}: ${label}, ${participant}\n`, 
		{encoding:'utf8'}
	)
  	res.send('1')
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))