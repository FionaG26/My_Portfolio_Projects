const { ethers } = require('ethers');
const fs = require('fs');
require('dotenv').config();

const contractABI = JSON.parse(fs.readFileSync('path/to/compiledABI.json')); // Replace with the actual path to the compiled ABI file
const contractAddress = 'CONTRACT_ADDRESS'; // Replace with the deployed contract address
const privateKey = process.env.PRIVATE_KEY;
const provider = new ethers.providers.JsonRpcProvider('https://ropsten.infura.io/v3/YOUR_INFURA_PROJECT_ID'); // Replace with your Infura Project ID

const wallet = new ethers.Wallet(privateKey, provider);
const contract = new ethers.Contract(contractAddress, contractABI, wallet);

async function voteForCandidate(candidateId) {
    try {
        const tx = await contract.vote(candidateId);
        console.log('Transaction Hash:', tx.hash);
        await tx.wait();
        console.log('Vote successful!');
    } catch (err) {
        console.error('Error:', err);
    }
}

async function getCandidateVotes(candidateId) {
    try {
        const votes = await contract.candidates(candidateId);
        console.log(`Candidate ${votes.name} has ${votes.voteCount} votes.`);
    } catch (err) {
        console.error('Error:', err);
    }
}

// Call the functions here to interact with the smart contract
