# tests/test_L002.py
import numpy as np

def E_capped(p, M):
    q = 1 - p
    return (1 - (M + 1) * q**M + M * q**(M + 1)) / (p * (1 - q**M))

def test_simulation_matches_closed_form():
    rng = np.random.default_rng(314159265358979323846 % 2**63)
    p, M, T = 0.3, 6, 200000
    g = rng.geometric(p, T)
    succ = g <= M
    assert abs(succ.mean() - (1 - (1 - p)**M)) < 0.01
    assert abs(g[succ].mean() - E_capped(p, M)) < 0.05

def test_limit_to_1_over_p():
    assert abs(E_capped(0.3, 500) - 1 / 0.3) < 1e-6

if __name__ == "__main__":
    test_simulation_matches_closed_form()
    test_limit_to_1_over_p()
    print("L-002: all tests green")