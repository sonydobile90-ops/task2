const fetch = require('node-fetch'); // npm install node-fetch

// Function to fetch and display a random joke
async function getRandomJoke() {
  try {
    const response = await fetch('https://official-joke-api.appspot.com/random_joke');
    const joke = await response.json();
    
    console.log('\n🎭 Here\'s a random joke for you:\n');
    console.log(`${joke.setup}`);
    console.log(`${joke.punchline}\n`);
    
    return joke;
  } catch (error) {
    console.error('Error fetching joke:', error);
  }
}

// Generate multiple jokes
async function getMultipleJokes(count = 5) {
  console.log(`\n📝 Getting ${count} random jokes...\n`);
  for (let i = 1; i <= count; i++) {
    const joke = await getRandomJoke();
    console.log(`---`);
  }
}

// Run the joke generator
getRandomJoke();
// Uncomment to get multiple jokes:
// getMultipleJokes(3);
