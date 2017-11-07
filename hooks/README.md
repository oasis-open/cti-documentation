## Git Hooks

To take advantage of the `update-time.py` pre-push Git Hook issue the command below from the repository's root directory.

```
ln -s -f hooks/update-time.py .git/hooks/pre-push
```

That's it! The time should automatically be updated every time you push to the repository.
