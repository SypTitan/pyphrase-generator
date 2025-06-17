<div align="center">
<h1>Passphrase Generator</h1>
</div>
<div align="center">
<img src="https://imgs.xkcd.com/comics/password_strength.png" width="60%" height="-1" alt="xkcd #936: Password Strength">
</div>
</lb>
<div align="center">
A simple CLI that generates (somewhat secure) passphrases, inspired by <a href="https://xkcd.com/936/">xkcd #936</a>, creating phrases by picking words from a list of 100 adjectives and 100 nouns.
</div>

## Installation

This project uses [uv](https://docs.astral.sh/uv/) as project manager.

To use the project, install uv, clone the repo, and run `uv sync`.

## Usage

```
uv run generate [-l|--lowercase] [-f|--free] [-s sep|--separator sep] [length]
uv run gen [-l|--lowercase] [-f|--free] [-s sep|--separator sep] [length]
```

## Examples

```
uv run generate                 # Lazy Slow Card Hope
uv run generate 2               # Fancy Gate
uv run generate -l              # dry dream grass sheep
uv run generate -l 6            # slow warm high wise bridge moon
uv run generate -s "-"          # Purple-Paper-Door-Town
uv run generate -l -s "_" 3     # gray_bold_sword
```
---

<details>
	<summary><h2 style="display:inline-block">Adjectives used in generation</h2></summary>

	red
	blue
	green
	yellow
	pink
	orange
	black
	white
	gray
	brown
	violet
	gold
	silver
	steel
	copper
	lead
	plastic
	paper
	hard
	soft
	rough
	smooth
	sharp
	dull
	clean
	dirty
	dry
	wet
	new
	old
	young
	light
	heavy
	strong
	weak
	brave
	correct
	wrong
	full
	empty
	loud
	quiet
	fast
	slow
	hot
	cool
	bright
	dark
	sweet
	sour
	bitter
	spicy
	flat
	round
	square
	deep
	shallow
	high
	long
	short
	quick
	slow
	busy
	lazy
	proud
	wise
	funny
	mean
	fancy
	poor
	rich
	common
	rare
	pure
	clear
	murky
	sick
	healthy
	tidy
	messy
	safe
	warned
	real
	fake
	striped
	spotted
	rugged
	torn
	raw
	cooked
	ripe
	bland
	vast
	tiny
	smoky
	sunny
	cloudy
	stormy
	foggy
	wild
	icy
	fiery
	frozen
	molten
	creamy
	crispy
	crunchy
	fluffy
	juicy
	soggy
	sticky
</details>

<details>
	<summary><h2 style="display:inline-block">Nouns used in generation</h2></summary>

	time
	door
	tree
	bird
	fish
	book
	hand
	star
	ring
	king
	queen
	heart
	fire
	rain
	snow
	wind
	moon
	ship
	road
	path
	house
	chair
	table
	wall
	floor
	roof
	food
	bread
	milk
	meat
	fruit
	apple
	stone
	sand
	lake
	river
	hill
	cloud
	storm
	light
	sound
	voice
	child
	horse
	sheep
	plant
	grass
	leaf
	wood
	metal
	glass
	gold
	paper
	clock
	wheel
	train
	plane
	sword
	shield
	crown
	bridge
	tower
	gate
	cave
	farm
	field
	coast
	beach
	world
	earth
	water
	ocean
	game
	song
	film
	story
	money
	work
	room
	card
	tooth
	hair
	face
	head
	foot
	nose
	mind
	gift
	shop
	town
	city
	park
	dream
	life
	hope
	friend
	baby
	bird
	dog
	cat
</details>

