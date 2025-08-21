import numpy as np

def project_simplex(v: np.ndarray) -> np.ndarray:
    n = len(v)
    u = np.sort(v)[::-1]  # 降序排列
    comsum = np.cumsum(u)
    j = np.arange(1, n + 1)
    cond = u - (comsum - 1) / j > 0
    if np.any(cond):
        rho = np.max(np.where(cond)[0])
        theta = (comsum[rho] - 1) / (rho + 1)
    else:
        theta = (comsum[-1] - 1) / n
    return np.maximum(v - theta, 0)

if __name__ == "__main__":
    v = np.array([-0.1, -0.2, 0.05, 0.6, 0.65])
    u = project_simplex(v)
    print("Project simplex:", u)