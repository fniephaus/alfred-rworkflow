# Alfred-RWorkflow

A [RPython][rpython]-compatible helper library for authors of workflows for [Alfred 2][alfred].

## What Is This?
Alfred can be extended with workflows written in different scripting languages such as [Python][python] or [Ruby][ruby].
These scripts need to be fast in order to keep Alfred's UI responsive. I wanted to play around with RPython which is a subset
of Python, so I decided to write a helper library similar to [Alfred-Workflow](alfred-workflow). With the RPython toolchain
it is possible to translate a RPython program into C which then can be compiled to produce an executable.

## Demo

![Demo](./demo.gif)

[Try it out yourself!][latest]

## Requirements
You need [pypy/pypy][pypy] for building your workflows.

## Building
```bash
[path to pypy repository]/rpython/bin/rpython demo.py
```

## Benchmarks
| Input       | CPython                                         | RPython                                       |                  
| -----------:|:-----------------------------------------------:|:---------------------------------------------:|
| 10          | 0.01s user 0.01s system 91% cpu 0.026 total     | 0.00s user 0.00s system 56% cpu 0.004 total   |
| 100         | 0.01s user 0.01s system 91% cpu 0.026 total     | 0.00s user 0.00s system 57% cpu 0.004 total   |
| 1000        | 0.02s user 0.01s system 92% cpu 0.028 total     | 0.00s user 0.00s system 59% cpu 0.004 total   |
| 10000       | 0.04s user 0.01s system 95% cpu 0.047 total     | 0.00s user 0.00s system 68% cpu 0.005 total   |
| 100000      | 0.35s user 0.01s system 98% cpu 0.368 total     | 0.03s user 0.00s system 93% cpu 0.037 total   |
| 1000000     | 6.85s user 0.06s system 99% cpu 6.929 total     | 0.67s user 0.01s system 99% cpu 0.685 total   |
| 10000000    | 161.77s user 1.12s system 99% cpu 2:43.36 total | 17.24s user 0.11s system 99% cpu 17.409 total |

[alfred]: http://www.alfredapp.com/
[alfred-workflow]: http://www.alfredapp.com/
[latest]: https://github.com/fniephaus/alfred-rworkflow/releases/latest/
[pypy]: https://bitbucket.org/pypy/pypy
[python]: https://www.python.org/
[rpython]: http://rpython.readthedocs.org/
[ruby]: https://www.ruby-lang.org/
