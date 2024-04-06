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
        
        return 
        max_weight_supported,
        items_count,
        items_weights,
        items_values,
        items_available_quantity
            
