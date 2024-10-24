const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

const GITHUB_TOKEN = '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';
const ORGANIZATION_NAME = 'RepoNamingConventionDemo';

app.post('/webhook', async (req, res) => {
    const action = req.body.action;
    const repositoryName = req.body.repository.name;

    if (action === 'created') {
        if (!repositoryName.startsWith('mgm-')) {
            try {
                await axios.delete(`https://api.github.com/repos/${ORGANIZATION_NAME}/${repositoryName}`, {
                    headers: {
                        Authorization: `token ${GITHUB_TOKEN}`,
                        Accept: 'application/vnd.github.v3+json'
                    }
                });
                console.log(`Repository ${repositoryName} deleted for not following naming convention.`);
            } catch (error) {
                console.error(`Error deleting repository: ${error.message}`);
            }
        } else {
            console.log(`Repository ${repositoryName} follows naming convention.`);
        }
    }

    res.status(200).send('Webhook received');
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

