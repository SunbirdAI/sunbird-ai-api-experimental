# Sunbird AI API (Experimental) Design document
## Introduction
This project recreates some of the functionality of the Sunbird AI API, with some experimental features added on top. Some of the experimental features are:
- Language Identification
- Translation of longer text documents of multiple formats (.txt, .pdf etc)

In addition to the functional features above, this project will also explore some DevOps concepts like:
- Use of linters like flake8 to ensure code quality.
- Usage of pre-commit hooks to run tests and flake8 before a commit is made.
- CI/CD (automated testing and deployment).
- Project management:
  - Usage of GitHub Projects to keep track of tasks/issues.
  - Usage of a design doc to drive progress.

The reason for separating this from the main API repo is mainly due to the complexity of setting up the codebase. 
We're currently facing an issue where our GCP account doesn't work so that codebase would require some non-trivial changes to get it to work with HuggingFace models. 
This is also mainly an intern project, so it's educational value comes from recreating some of the functionality already in the API.

Checkout the [design doc for the main API](https://github.com/SunbirdAI/sunbird-docs/blob/main/06-design-docs/language/API_Framework.md) if interested.

## Requirements
1. Translation endpoint (text input).
   1. This endpoint receives text and translates to the given target language.
   2. If the source language is not specified, run the text through a language ID model and use the result as the source language.
   3. If the text > 200 characters long, split the text into batches of <= 200 characters, translate each batch, and combine the results into the final output.
   4. The response should include the translated text and the identified language.
   5. The translation models to use are
      1. English-to-Multiple: https://huggingface.co/Sunbird/sunbird-en-mul
      2. Multiple-to-English: https://huggingface.co/Sunbird/mbart-mul-en
      3. Local-to-Local: Chain the above
2. Translation endpoint (file input)
   1. This endpoint receives a text file in either .pdf or .txt format, translates it and returns a file containing the translation.
   2. Acceptable file size is <= 2MB
3. Frontend
   1. Create a basic frontend similar to `translate.sunbird.ai` (or `translate.google.com`) that takes in text and returns the translation.
   2. It should also support file upload for translation.
4. DevOps
   1. Use flake8 for linting code.
   2. Use a pre-commit hook to run linting before a commit is made.
   3. Use github actions to run tests automatically.
   4. Use github actions to automatically deploy when code is merged into the main branch. (Deployment options are [fly.io](https://fly.io/), [heroku](https://www.heroku.com/) or [google cloud run](https://cloud.google.com/run).
   5. Each task is an issue in this [project](https://github.com/orgs/SunbirdAI/projects/7). For each task, create a branch for the task, raise a PR, attach the PR to an issue, mark off the tasklist as tasks are completed, then receive review from 2 people before it can be merged.


## Endpoint structure
#### Text Translate
`POST /api/translate`
**Request**:
```
{
  (optional) "source-language": "",
  "target-language": "",
  "text": "",
}
```

**Response**:
```
{
  "text": "",
  (optional) "detected-language": ""
}
```

#### File translate
`POST /api/file-translate`
**Request**:
```
Form-data with the following fields:

text_file:
(optional) source_language:
```

**Response**
```
JSON response with an S3 (or GCS) link to the translate file:
{
  "translated-file": "https://s3.amazonaws.com/file.txt" 
}
```

## Tech stack
- API Framework: [FastAPI](https://fastapi.tiangolo.com/)
- Models: [HuggingFace Inference API](https://huggingface.co/Sunbird).
- Frontend: Jinja templates + Tailwind.
- Deployment: Fly.io, Heroku or CloudRun (still deciding)
