# Puppy Writer Lambda

This mini-project provides an AWS Lambda that:
1. Reads a JSON document from an S3 bucket
2. Checks a MongoDB Atlas collection to see if it's already in it
3. If not, it is added to the db.  
		a. And if it meets a criteria, send me a text message via Twilio

## Prerequisites

- This project was developed with Python 3.7+

## Getting Started

- git clone & cd into it
- Make the virtual environment:
  - `mkvirtualenv -p /usr/local/bin/python3.8 -r requirements.txt`

### Tests

- coming eventually
- In the meantime, lint with `flake8`

## Configuration

* Define AWS credentials in either `config.yaml` or in the [default] section of `~/.aws/credentials`. To use another profile, append something like `--profile user1`.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the AWS credentials to version control.

## Invocation

	lambda invoke -v
 
## Deploy
    
To deploy:

	lambda deploy --requirements requirements.txt
