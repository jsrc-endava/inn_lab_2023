To run app:
```
flask --app noah_core run --port=4000 --host=0.0.0.0 --debug
```

To interact with Alembic:
```
flask --app noah_core db --help
flask --app noah_core db migrate -m "new revision" # After modyfing models
flask --app noah_core db upgrade
flask --app noah_core db downgrade
```

To interact with pytest:
```
pytest
pytest -s # to print to console
```

To run tasks:
```
invoke --list
invoke zilliz-schema.messages
```