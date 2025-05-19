<h1 align="center">
    <br>
    Pied Piper
</h1>

<h3 align="center">
    An Agent-Based Model Framework for simulating society resilience
</h3>

<div align="center">

![Python Version](https://img.shields.io/badge/python-≥3.10-blue)
[![PyPI Version](https://img.shields.io/pypi/v/piperabm.svg)](https://pypi.org/project/piperabm/)
[![GitHub](https://img.shields.io/badge/github-30363f?logo=github&logoColor=white)](https://github.com/cmudrc/pied-piper)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

<h3 align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Pied_Piper2.jpg/593px-Pied_Piper2.jpg" alt="KeePied Piper of HamelinpDelta" width="500">
</h3>

## Introduction

Whenever environments condition change for species, the living entities start to react to the new new condition. This projects aims at modeling the Alaskan communities that are heavily affected by the global warming.

## Installation

Install the package using pip:
```sh
pip install piperabm
```

## Usage

Once a `Model` instance is created, it automatically includes interconnected `infrastructure` and `society` components. The simulation is designed to explore how changes in one domain, such as agent behavior or infrastructure layout, affect the other over time. This interdependence forms the core of agent-based modeling within `PiperABM`.

```python
import piperabm as pa

model = pa.Model()
model.infrastructure.add_street(pos_1=[0, 0], pos_2=[-60, 40], name='road')
model.infrastructure.add_home(pos=[5, 0], id=1, name='home 1')
model.infrastructure.add_home(pos=[-60, 40], id=1, name='home 2')
model.infrastructure.bake()
model.society.generate(num=2, gini_index=0.4, average_balance=1000)
model.run(n=100, step_size=60)
```

For more usage examples, refer to the [`examples`](https://github.com/cmudrc/pied-piper/tree/main/examples) folder in the project repository.

## Supported Python Versions

It has been tested and verified to work with Python versions **3.10** to **3.13**. While it is expected to work with older versions of Python (given compatible dependency versions), these environments have not been tested and are not officially supported.

## Contributing

Contributions are welcome! Feel free to:
* Report issues.
* Submit feature requests.
* Create pull requests.

## License

Distributed under the MIT License. See [`LICENSE.txt`](https://github.com/cmudrc/pied-piper/blob/main/LICENSE) for more information.