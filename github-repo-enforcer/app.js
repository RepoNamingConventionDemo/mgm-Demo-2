const express = require('express');
const axios = require('axios');
const crypto = require('crypto');
const app = express();

// Use environment variables to store sensitive information
const GITHUB_TOKEN = process.env.GIT_TOKEN;  // Get from GitHub Secrets
const SECRET = process.env.WEBHOOK_SECRET;  // Get from GitHub Secrets

app.use(express.json());

// Function to verify the webhook signature
function verifySignature(req) {
  const payload = JSON.stringify(req.body);
  const signature = req.headers['x-hub-signature-256'];
  const hmac = crypto.createHmac('sha256', SECRET);
  const digest = 'sha256=' + hmac.update(payload).digest('hex');
  return crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(digest));
}

app.post('/webhook', async (req, res) => {
  if (!verifySignature(req)) {
    return res.status(403).send('Invalid signature');
  }

  const repoName = req.body.repository.name;
  const owner = req.body.repository.owner.login;

  // Define your naming convention (repository name must start with 'mgm-')
  const isValid = /^mgm-[a-z0-9-]+$/.test(repoName);

  // If the repository name is invalid, delete the repository
  if (!isValid) {
    try {
      await axios.delete(`https://api.github.com/repos/${owner}/${repoName}`, {
        headers: {
          'Authorization': `token ${GITHUB_TOKEN}`,
          'Content-Type': 'application/json',
        },
      });
      console.log(`Repository ${repoName} deleted for violating naming convention.`);
      res.status(200).send(`Repository ${repoName} deleted.`);
    } catch (error) {
      console.error('Error deleting repository:', error.response?.data || error.message);
      res.status(500).send('Failed to delete repository');
    }
  } else {
    res.status(200).send('Repository name is valid');
  }
});

app.listen(3000, () => {
  console.log('Webhook listener running on port 3000');
});

