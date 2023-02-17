# AcceptReject.Py
This is code for PHSX815 - Spring 2023 for Accept/Reject sampling. It takes a predefined target function `f(x)`, defines a proposal function `g(x)`, then generates random samples based on user-defined criterion.

## Usage

`python3 AcceptReject.py -h` Help \
`python3 AcceptReject.py [-seed -size -reg (0 or 1)]` 

`-seed` Seed number \
`-size`  Sample Size \
`-reg` Selects the region beneath which is the "hit" or "miss" region. This is either `0` or `1` where `0` is below the target function and `1` is
between the target function and the proposal function.
