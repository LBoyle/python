# Migrations

Using flask_migrate. Also trying a join-table.

An example of a query I can use with this setup.
```
Channel.query.first().subscribers.first().name
```

#### Progress

Now I've begun splitting it up into separate files, I'm running into problems I didn't predict. For instance, the controllers are doing a lot of work.

I'm also going to need a settings file.
