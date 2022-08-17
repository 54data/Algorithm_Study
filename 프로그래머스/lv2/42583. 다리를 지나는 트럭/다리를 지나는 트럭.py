def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    
    while bridge:
        answer += 1
        bridge.pop(0)
        
        if truck_weights:
            if weight >= sum(bridge) + truck_weights[0]:
                x = truck_weights.pop(0)
                bridge.append(x)
            else:
                bridge.append(0)
                
    return answer