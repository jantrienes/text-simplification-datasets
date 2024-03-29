# Text Simplification Datasets

A collection of text simplification datasets with a focus on sentence/paragraph/document-level simplification. All [contributions](#Contributing) are welcome!

For browsing/sorting the datasets, you can use the [interactive table](https://jantrienes.github.io/text-simplification-datasets/).

## Datasets

Notes on the table columns:

- **Kind** refers to the way simplification instances were obtained. For _parallel_, this is usually through manual simplification according to specific guidelines. For _comparable_, this is by automatically mining pairs of complex/simple sentences with similar meaning from a large text corpus.
- **Level** can be lexical (lex), sentence (sent), paragraph (para) or document (doc).
- **Refs** refers to the number of references per instance (i.e., gold simplifications).

{{datasets}}

## Contributing

New entries can be added to [`data.yml`](./data.yml). Afterwards, run `python render.py` and submit a PR with the changes.

## Acknowledgements

This list has greatly benefitted from the survey of [Alva-Manchego et al. (2020)](https://doi.org/10.1162/COLI_a_00370) and [Štajner (2021)](https://doi.org/10.18653/v1/2021.findings-acl.233), as well as notes by [Laura Vásquez-Rodríguez](https://lmvasque.github.io/). Thanks! Also thanks to [@tollefj](https://github.com/tollefj) for adding the interactive table.
