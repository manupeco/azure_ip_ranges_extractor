import json
import sys
import ipaddress

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]
service_to_extract = sys.argv[3]

f = open(input_file_path)

json_data = json.load(f)


output_dict = [x for x in json_data["values"] if x["name"] == service_to_extract]

with open(output_file_path, 'w') as writer:    
    writer.write('<ip-filter action="allow">')

    for ip_ranges in output_dict:
        ip_list = ip_ranges["properties"]["addressPrefixes"]
        for cidr in ip_list:
            lowest_and_max_ip = ipaddress.ip_network(cidr)
            lowest_ip = lowest_and_max_ip[0]
            max_ip = lowest_and_max_ip[-1]
            range_for_policy = f'\n\t<address-range from="{lowest_ip}" to="{max_ip}" />'
            writer.write(range_for_policy)

    writer.write("\n</ip-filter>")


f.close()