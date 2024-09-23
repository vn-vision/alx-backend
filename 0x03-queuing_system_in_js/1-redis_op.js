#!/usr/bin/yarn dev
import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
	console.log('Redis client not connected to the server: ', err.toString());
});
client.on('connect', () => {
	console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value, print){
	client.set(schoolName, value);
}

function displaySchoolValue(schoolName){
	client.get(schoolName, (_err, reply) =>{
		console.log(reply);
	});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
