# AILab

AI Lab is a Python based back propagation image generation application.

## Installation

### Coming Soon
From source:

```bash
git clone https://github.com/Lonestar137/AILab ailab
cd ailab
make install
```

From pypi:

```bash
pip install ailab
```

## Executing

This application has a CLI interface that extends the Flask CLI.

Just run:

`python -m ailab run`

Go to:

- Website: http://localhost:5000
- Admin: http://localhost:5000/admin/
  - user: admin, senha: 1234
-API POST:
  - http://localhost:5000/api/v1/post/generate/image
- API GET:
  - http://localhost:5000/api/v1/post/
  - http://localhost:5000/api/v1/product/
  - http://localhost:5000/api/v1/product/1
  - http://localhost:5000/api/v1/product/2
  - http://localhost:5000/api/v1/product/3


> **Note**: You can also use `flask run` to run the application.
