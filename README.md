# weekend-app02

Internal JSON API for the `weekend-lab` cluster.

## Test and run

```sh
python3 -m unittest discover -s tests -v
hadolint Dockerfile
podman build -t weekend-app02:dev .
podman run --rm -p 8080:8080 weekend-app02:dev
curl --fail http://localhost:8080/healthz
```

Commits to `main` publish `ghcr.io/phelun/weekend-app02:<full-git-sha>`. Pull requests test, lint, build, and scan without publishing.
