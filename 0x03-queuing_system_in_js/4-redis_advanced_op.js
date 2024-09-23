#!/usr/bin/env node
import { createClient, print } from 'redis';

// Create the Redis client
const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
  
  // Store hash values using hset
  client.hset('HolbertonSchools', 'Portland', 50, print);
  client.hset('HolbertonSchools', 'Seattle', 80, print);
  client.hset('HolbertonSchools', 'New York', 20, print);
  client.hset('HolbertonSchools', 'Bogota', 20, print);
  client.hset('HolbertonSchools', 'Cali', 40, print);
  client.hset('HolbertonSchools', 'Paris', 2, print);

  // Retrieve and display the entire hash
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.log('Error fetching data:', err);
    } else {
      console.log(reply);
    }

    // Close the Redis connection after the operations
    client.quit();
  });
});
