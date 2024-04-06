from collections import namedtuple

def read_file_data(): 
    with open('dados.txt') as file: 
        max_weight_supported = int(file.readline())
        items_count = int(file.readline())
        
        items_weights = []
        items_values = []
        items_available_quantity = []
        
        for _ in range(items_count):
            item_infos = file.readline().split()
            items_weights.append(float(item_infos[0]))
            items_values.append(float(item_infos[1]))
            items_available_quantity.append(int(item_infos[2]))
        
        forbidden_pairs = []
        
        for line in file:
            raw = line.split()
            forbidden_pairs.append((int(raw[0]), int(raw[1])))
        
        Data = namedtuple(
            'Data', [
                'max_weight_supported',
                'items_count',
                'items_weights',
                'items_values',
                'items_available_quantity',
                'forbidden_pairs'
            ]
        )
        
        return Data(
            max_weight_supported,
            items_count,
            items_weights,
            items_values,
            items_available_quantity,
            forbidden_pairs)
            
