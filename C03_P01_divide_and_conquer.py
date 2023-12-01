import csv

class System:
    def __init__(self):
        self.sensors_list = list()
        self.sensor_mapping_list = list()
        self.master_node_list = list()
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.DictReader(data_file)
        for row in reader:
            node_id = row['Node ID']
            type = row['Type']
            master_node_id = row['Master Node ID']
            
            if type == 'Master':
                self.master_node_list.append(int(master_node_id))
            elif type == "Sensor":
                self.sensors_list.append(int(node_id))
                self.sensor_mapping_list.append(int(master_node_id))
                
        
    def SensorAssignedCount(self, mapping_list, l, r, OverloadSensor):
        count = 0
        for i in range(l, r+1):
            if (mapping_list[i] == OverloadSensor): 
                count +=  1
        return count
    
    def OverloadNodeHelper(self,l, r):
        if l == r:
            return self.sensor_mapping_list[l]
        mid = (l + r)//2
        left_overload = self.OverloadNodeHelper(l, mid)
        right_overload = self.OverloadNodeHelper(mid+1, r)
    
        left_count = self.SensorAssignedCount(self.sensor_mapping_list, l, mid, left_overload)
        right_count = self.SensorAssignedCount(self.sensor_mapping_list, mid+1, r, right_overload)
    
        if left_count > (mid - l + 1)//2 and right_count > (r - mid)//2:
            return min(left_overload, right_overload)
        elif left_count > (mid - l + 1)//2:
            return left_overload
        else:
           return right_overload
        
        #pass
        
    def getOverloadedNode(self):
        
        return self.OverloadNodeHelper(0, len(self.sensor_mapping_list)-1)
    
    def getPotentialOverloadNode(self):
        potential_overload_nodes = []
        n = len(self.sensor_mapping_list)
        for master_node in self.master_node_list:
            assigned_sensors = self.SensorAssignedCount(self.sensor_mapping_list, 0, n - 1, master_node)
            if assigned_sensors > n // 2:
                return master_node
            elif assigned_sensors == n // 2:
                potential_overload_nodes.append(master_node)
        return potential_overload_nodes
            #pass
    
if __name__ == "__main__":
    test_system1 = System()
    
    test_system1.config_system('app_data1.csv')
    
    print("Overloded Master Node : ", test_system1.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system1.getPotentialOverloadNode())

    test_system2 = System()
    
    test_system2.config_system('app_data2.csv')
    
    print("Overloded Master Node : ", test_system2.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system2.getPotentialOverloadNode())

    test_system3 = System()

    test_system3.config_system('app_data3.csv')
    
    print("Overloded Master Node : ", test_system3.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system3.getPotentialOverloadNode())

    test_system4 = System()

    test_system4.config_system('app_data4.csv')
    
    print("Overloded Master Node : ", test_system4.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system4.getPotentialOverloadNode())
