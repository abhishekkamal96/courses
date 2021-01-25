# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contact_name = {}
    name_contact = {}
    count = 1
    for cur_query in queries:
        if cur_query.type == 'add':
            cur_num = cur_query.number
            cur_name = cur_query.name
            if cur_num in contact_name:
                if cur_name == contact_name.get(cur_num):
                    continue
                else:
                    exist_name = contact_name.get(cur_num)
                    if exist_name in name_contact:
                        if len(name_contact[exist_name]) > 1:
                            ind = name_contact[exist_name].index(cur_num)
                            name_contact[exist_name].pop(ind)
                        else:
                            del name_contact[exist_name]

                    if cur_name in name_contact:
                        name_contact[cur_name].append(cur_num)
                    else:
                        name_contact[cur_name] = [cur_num]
                contact_name[cur_num] = cur_name
            elif cur_name in name_contact:
                contact_name[cur_num] = cur_name
                name_contact[cur_name].append(cur_num)
            else:
                name_contact[cur_name] = [cur_num]
                contact_name[cur_num] = cur_name

        elif cur_query.type == 'del':
            cur_num = cur_query.number
            cur_name = contact_name.get(cur_num)
            if cur_num in contact_name:
                del contact_name[cur_num]
            if cur_name in name_contact:
                if len(name_contact[cur_name])>1:
                    ind = name_contact[cur_name].index(cur_num)
                    name_contact[cur_name].pop(ind)
                else:
                    del name_contact[cur_name]

        else:
            res = 'not found'
            cur_num = cur_query.number
            if cur_num in contact_name:
                res = contact_name.get(cur_num)
            result.append(res)

        # print(count)
        # print("contact_name ", count, contact_name)
        # print("name_contact ", count, name_contact)
        # count += 1

    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

