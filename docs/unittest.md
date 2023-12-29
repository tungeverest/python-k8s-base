
# Run all tests

```bash
sh ./devspace/scripts/run_test.sh tests/
```

OR

```bash
make unittest
```

Run one test

```bash
sh ./devspace/scripts/run_test.sh tests/test_account.py::TestAccount::test_get
```

**NOTE**: Some tests may fail on first try and need to re-run._
