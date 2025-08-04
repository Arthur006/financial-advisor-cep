#!/bin/bash

python puml-generator.py -o docs/images/context.svg puml/context.puml
python puml-generator.py -o docs/images/container.svg puml/container.puml
python puml-generator.py -o docs/images/login-sequence.svg puml/login-sequence.puml
python puml-generator.py -o docs/images/client-sequence.svg puml/client-sequence.puml
python puml-generator.py -o docs/images/advisor-sequence.svg puml/advisor-sequence.puml
