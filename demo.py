company = {
    "Engineering": {
        "Backend": ["Alice", "Bob", "Charlie"],
        "Frontend": ["David", "Eve"],
        "DevOps": ["Frank"]
    },
    "Sales": {
        "North": ["Grace", "Henry"],
        "South": ["Ivy"]
    }
}

def flattenDict(my_dict):
    flatDict = []
    for items in my_dict:
        if isinstance(my_dict[items], dict):
            flatDict.extend(flattenDict(my_dict[items]))

        elif isinstance(my_dict[items], list):
            flatDict.extend(my_dict[items])
            
        else :
           flatDict.append(my_dict[items])

    return flatDict


from collections import defaultdict
def countEmps(my_dict):
    count_dict = defaultdict(int)
    for dept in my_dict:
        if isinstance(my_dict[dept],dict):
            for key , value in my_dict[dept].items():
                count_dict[dept] += len(value)
    return count_dict

def findDept(emp , my_dict):
    for dept in my_dict:
        # if isinstance(my_dict[dept],dict):
            for key , value in my_dict[dept].items():
                if emp in value:
                    return key
    return f'{emp} not found in any team'

rev_dict = {emp : [dept , team] for dept in company for team , emps in company[dept].items() for emp in emps}

my_list = list(filter(lambda x : x < 1000 , map(lambda x: x**2 , [n for n in range(100) if (n%3==0) ^ (n%5==0)])))

print(my_list)

