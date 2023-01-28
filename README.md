# example-components
An example of how to use Codecov's Components feature

The initial setup consists of 2 directories `calculator` and `smiles`. The `calculator` directory also consists of 2 sub-directories `simple` and `complex`.

```
.
├── calculator
│   ├── complex
│   │   ├── complex_calculator.py
│   │   └── test_complex_calculator.py
│   └── simple
│       ├── simple_calculator.py
│       └── test_simple_calculator.py
└── smiles
    ├── smiles.py
    └── test_smiles.py
```

As shown above, each file exists alongside its corresponding test file.

For this example, there will be **2 components**, `calculator` and `smiles` which correspond to the directories. You will need to edit the `codecov.yml` file as is done in this repository in order to see Components in your codebases. See [our documentation](https://docs.codecov.com/docs/components) for details.

## Components in the PR comment

To see an example of what components look like in the Codecov [PR comment](https://github.com/codecov/example-components/pull/2#issuecomment-1407490619), see this [pull request](https://github.com/codecov/example-components/pull/2). Note the section `Components` where you will see the increase in the `calculator` component.

## Components with multiple uploads

To see how Components deal with multiple uploads, see this [pull request](https://github.com/codecov/example-components/pull/3). The `calculator` Component is created as a union of the `complex` and `simple` coverage uploads.

Since Components are not correlated with uploads, you do not need to specify Components during upload time, only in the `codecov.yml` file. They will work with any number of uploads.

## Components with flags

Unlike Components, Flags are correlated with uploads. For larger codebases, you may find that you will need a Flag for internal services (e.g. `simple/` and `complex/`) of projects (e.g. `calculator/` and `smiles/`) in a monorepository.

See this [pull request](https://github.com/codecov/example-components/pull/4) with how to incorporate both into your systems.
