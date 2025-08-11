import tensorcircuit as tc
import numpy as np
from noise_sim_tc import noise_sim
from tensorcircuit.channels import amplitudedampingchannel

def cz_expectation(observable, n_cz, isNoisy=True):
    """
    observable: list, e.g. [0,3]，0,1,2,3分别代表I,X,Y,Z，顺序对应比特0和1
    n_cz: int, CZ门数量
    返回有噪声电路的期望值
    """
    # 泡利算符映射
    pauli_keys = ['i', 'x', 'y', 'z']
    obs_dict = {pauli_keys[observable[0]]: [0], pauli_keys[observable[1]]: [1]}

    # 生成泡利算符列表
    pauli_dict = {
        'i': np.array([[1, 0], [0, 1]]),
        'x': np.array([[0, 1], [1, 0]]),
        'y': np.array([[0, -1j], [1j, 0]]),
        'z': np.array([[1, 0], [0, -1]])
    }
    # 构造特征向量
    def get_eigenvector(idx):
        if idx == 0:
            return np.array([1, 0])  # I本征态任意，取|0>
        elif idx == 1:
            return np.array([1, 1]) / np.sqrt(2)  # X本征态
        elif idx == 2:
            return np.array([1, 1j]) / np.sqrt(2)  # Y本征态
        elif idx == 3:
            return np.array([1, 0])  # Z本征态
    state_list = [get_eigenvector(observable[0]), get_eigenvector(observable[1])]
    init_state = np.kron(state_list[0], state_list[1])

        # 构造电路
    circuit = tc.Circuit(2, inputs=init_state)
    for _ in range(n_cz):
        circuit.cz(0, 1)
    circuit_noise = noise_sim(circuit)

    # 计算期望值
    pn_noisy = circuit_noise.expectation_ps(**obs_dict)
    pn_noiseless = circuit.expectation_ps(**obs_dict)
    if isNoisy:
        return pn_noisy
    return pn_noiseless