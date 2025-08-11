import tensorcircuit as tc
import numpy as np

def calculate_readout_error(num_qubits, num_shots):
    """
    使用TensorCircuit计算读出误差
    
    参数:
        num_qubits: 量子比特数量
        num_shots: 测量次数
        
    返回:
        readout_error: 读出误差率
        results: 测量结果统计
    """
    # 创建量子电路，初始状态为全零态
    c = tc.Circuit(num_qubits)
    
    # 对所有量子比特进行测量
    # TensorCircuit中测量会返回测量结果和概率分布
    # 我们进行多次测量以获取统计结果
    results = {}
    total_errors = 0
    
    for _ in range(num_shots):
        # 测量所有量子比特，得到结果（以字符串形式表示）
        # 在实际硬件中，这里会包含读出误差
        # 在模拟器中，我们可以通过添加噪声模型来模拟
        # 这里我们使用带噪声的测量
        meas = c.measure(allow_state=True, with_prob=False, noisy=True)
        
        # 将测量结果转换为字符串
        result_str = ''.join(map(str, meas[::-1]))  # 注意量子比特顺序可能需要反转
        
        # 检查是否为全零态
        if result_str != '0' * num_qubits:
            total_errors += 1
        
        # 更新结果统计
        if result_str in results:
            results[result_str] += 1
        else:
            results[result_str] = 1
    
    # 计算读出误差率
    readout_error = total_errors / num_shots
    
    return readout_error, results

# 参数设置
num_qubits = 3       # 3个量子比特
num_shots = 10000    # 测量10000次

# 运行计算
readout_error, results = calculate_readout_error(num_qubits, num_shots)

# 输出结果
print(f"量子比特数量: {num_qubits}")
print(f"测量次数: {num_shots}")
print(f"读出误差率: {readout_error:.2%}")
print("\n测量结果分布:")
for state, count in sorted(results.items()):
    probability = count / num_shots
    print(f"状态 |{state}⟩: {count}次 ({probability:.2%})")