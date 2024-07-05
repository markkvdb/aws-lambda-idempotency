# aws-lambda-idempotency

This project showcases how to introduce idempotency to AWS lambda handlers by using a DynamoDB table. Most of the hard work is done by [Powertools for AWS Lambda](https://docs.powertools.aws.dev/lambda/python/latest/) and [Serverless](https://www.serverless.com/).


## Quick-start

Make sure that NPM and Poetry are installed on your system. Next, clone this repository and install the necessary node packages via `npm install`.

Deploy this project using Serverless with

```bash
sls deploy
```


## Notes

- The TableName property of the defined DynamoDB table needs to match the one referenced in `app.py`. This could be improved by introducing an environment variable taken from the serverless file.
