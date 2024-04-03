<div align="center">
<h1>🎤 AI-Karaoke-Backend</h1>

An API built for the AI-Karaoke event

For instructions on how to use the API refer to `📁 doc/routes.md`

Current version : 1.0

</div>

---

## Development

After cloning the repository, run the following command in your `venv`:

```bash
pip install -r requirements.txt
```

Switch to the `karaoke_backend` project:

```bash
cd karaoke_backend
```

and start the server:

```bash
python ./manage.py runserver 0.0.0.0:8000
```

## Build

To build the project for deployment, containerize the app using the Dockerfile

```bash
docker buildx build -t ai-karaoke .
```

and then run the image

```bash
docker run -it -p 8000:8000 ai-karaoke
```
