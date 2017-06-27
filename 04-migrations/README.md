# Migrations

Using flask_migrate. Also trying a join-table.

An example of a query I can use with this setup.
```
Channel.query.first().subscribers.first().name
```
