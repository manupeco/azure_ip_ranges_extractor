# Azure API Management Filter Policy Creator
 A Python script that allows to create the XML snippet to allow API Management to accept request only from IP ranges of a specific service

# How to use it

## Retrive the IP address ranges for all Azure services
Visit the page https://learn.microsoft.com/en-us/rest/api/virtualnetwork/service-tags/list?tabs=HTTP and click on the red button “Try it” above the endpoint. Choose your Azure account to sign in and continue. Enter a region in location field (“West Europe”) and choose the subscription.

Now click the “Run” button and get the result. Take the big JSON returned as result and save it in a file.

## Create the policy snippet

Run the script with the command:

```
python ip_extractor.py <path_previous_saved_json_file> <path_of_output_xml_file_with_policy_snippet> <azure_service_name>
```

The value for <azure_service_name> can be found in the json file in the name attribute of the different json block inside the input file.
If we use for example "AzureFrontDoor.Backend" as name we'll get a result file like the following:

```
<ip-filter action="allow">
	<address-range from="4.232.98.120" to="4.232.98.127" />
	<address-range from="13.73.248.16" to="13.73.248.23" />
	<address-range from="20.21.37.40" to="20.21.37.47" />
	<address-range from="20.36.120.104" to="20.36.120.111" />
	<address-range from="20.37.64.104" to="20.37.64.111" />
	<address-range from="20.37.156.120" to="20.37.156.127" />
	<address-range from="20.37.195.0" to="20.37.195.7" />
	<address-range from="20.37.224.104" to="20.37.224.111" />
	<address-range from="20.38.84.72" to="20.38.84.79" />
	<address-range from="20.38.136.104" to="20.38.136.111" />
	<address-range from="20.39.11.8" to="20.39.11.15" />
	<address-range from="20.41.4.88" to="20.41.4.95" />
	<address-range from="20.41.64.120" to="20.41.64.127" />
	<address-range from="20.41.192.104" to="20.41.192.111" />
	<address-range from="20.42.4.120" to="20.42.4.127" />
	<address-range from="20.42.129.152" to="20.42.129.159" />
	<address-range from="20.42.224.104" to="20.42.224.111" />
	<address-range from="20.43.41.136" to="20.43.41.143" />
	<address-range from="20.43.65.128" to="20.43.65.135" />
	<address-range from="20.43.130.80" to="20.43.130.87" />
	<address-range from="20.45.112.104" to="20.45.112.111" />
	<address-range from="20.45.192.104" to="20.45.192.111" />
	<address-range from="20.59.103.64" to="20.59.103.71" />
	<address-range from="20.72.18.248" to="20.72.18.255" />
	<address-range from="20.79.107.152" to="20.79.107.159" />
	<address-range from="20.88.157.176" to="20.88.157.183" />
	<address-range from="20.90.132.152" to="20.90.132.159" />
	<address-range from="20.115.247.64" to="20.115.247.71" />
	<address-range from="20.118.195.128" to="20.118.195.135" />
	<address-range from="20.119.155.128" to="20.119.155.135" />
	<address-range from="20.150.160.96" to="20.150.160.103" />
	<address-range from="20.189.106.112" to="20.189.106.119" />
	<address-range from="20.192.161.104" to="20.192.161.111" />
	<address-range from="20.192.225.48" to="20.192.225.55" />
	<address-range from="20.210.70.64" to="20.210.70.67" />
	<address-range from="20.215.4.240" to="20.215.4.247" />
	<address-range from="20.217.44.240" to="20.217.44.247" />
	<address-range from="40.67.48.104" to="40.67.48.111" />
	<address-range from="40.74.30.72" to="40.74.30.79" />
	<address-range from="40.80.56.104" to="40.80.56.111" />
	<address-range from="40.80.168.104" to="40.80.168.111" />
	<address-range from="40.80.184.120" to="40.80.184.127" />
	<address-range from="40.82.248.248" to="40.82.248.255" />
	<address-range from="40.89.16.104" to="40.89.16.111" />
	<address-range from="51.12.41.8" to="51.12.41.15" />
	<address-range from="51.12.193.8" to="51.12.193.15" />
	<address-range from="51.53.30.144" to="51.53.30.151" />
	<address-range from="51.104.25.128" to="51.104.25.135" />
	<address-range from="51.105.80.104" to="51.105.80.111" />
	<address-range from="51.105.88.104" to="51.105.88.111" />
	<address-range from="51.107.48.104" to="51.107.48.111" />
	<address-range from="51.107.144.104" to="51.107.144.111" />
	<address-range from="51.120.40.104" to="51.120.40.111" />
	<address-range from="51.120.224.104" to="51.120.224.111" />
	<address-range from="51.137.160.112" to="51.137.160.119" />
	<address-range from="51.143.192.104" to="51.143.192.111" />
	<address-range from="52.136.48.104" to="52.136.48.111" />
	<address-range from="52.140.104.104" to="52.140.104.111" />
	<address-range from="52.150.136.120" to="52.150.136.127" />
	<address-range from="52.159.71.160" to="52.159.71.167" />
	<address-range from="52.228.80.120" to="52.228.80.127" />
	<address-range from="68.221.93.128" to="68.221.93.135" />
	<address-range from="102.133.56.88" to="102.133.56.95" />
	<address-range from="102.133.216.88" to="102.133.216.95" />
	<address-range from="147.243.0.0" to="147.243.255.255" />
	<address-range from="158.23.108.56" to="158.23.108.63" />
	<address-range from="191.233.9.120" to="191.233.9.127" />
	<address-range from="191.235.225.128" to="191.235.225.135" />
	<address-range from="2603:1000:4::600" to="2603:1000:4::61f" />
	<address-range from="2603:1000:104::e0" to="2603:1000:104::ff" />
	<address-range from="2603:1000:104::300" to="2603:1000:104::31f" />
	<address-range from="2603:1000:104:1::5c0" to="2603:1000:104:1::5df" />
	<address-range from="2603:1000:104:1::7e0" to="2603:1000:104:1::7ff" />
	<address-range from="2603:1010:6:1::5c0" to="2603:1010:6:1::5df" />
	<address-range from="2603:1010:6:1::7e0" to="2603:1010:6:1::7ff" />
	<address-range from="2603:1010:101::600" to="2603:1010:101::61f" />
	<address-range from="2603:1010:304::600" to="2603:1010:304::61f" />
	<address-range from="2603:1010:404::600" to="2603:1010:404::61f" />
	<address-range from="2603:1020:5:1::5c0" to="2603:1020:5:1::5df" />
	<address-range from="2603:1020:5:1::7e0" to="2603:1020:5:1::7ff" />
	<address-range from="2603:1020:206:1::5c0" to="2603:1020:206:1::5df" />
	<address-range from="2603:1020:206:1::7e0" to="2603:1020:206:1::7ff" />
	<address-range from="2603:1020:305::600" to="2603:1020:305::61f" />
	<address-range from="2603:1020:405::600" to="2603:1020:405::61f" />
	<address-range from="2603:1020:605::600" to="2603:1020:605::61f" />
	<address-range from="2603:1020:705:1::5c0" to="2603:1020:705:1::5df" />
	<address-range from="2603:1020:705:1::7e0" to="2603:1020:705:1::7ff" />
	<address-range from="2603:1020:805:1::5c0" to="2603:1020:805:1::5df" />
	<address-range from="2603:1020:805:1::7e0" to="2603:1020:805:1::7ff" />
	<address-range from="2603:1020:905::600" to="2603:1020:905::61f" />
	<address-range from="2603:1020:a04:1::5c0" to="2603:1020:a04:1::5df" />
	<address-range from="2603:1020:a04:1::7e0" to="2603:1020:a04:1::7ff" />
	<address-range from="2603:1020:b04::600" to="2603:1020:b04::61f" />
	<address-range from="2603:1020:c04:1::5c0" to="2603:1020:c04:1::5df" />
	<address-range from="2603:1020:c04:1::7e0" to="2603:1020:c04:1::7ff" />
	<address-range from="2603:1020:d04::600" to="2603:1020:d04::61f" />
	<address-range from="2603:1020:e04:1::5c0" to="2603:1020:e04:1::5df" />
	<address-range from="2603:1020:e04:1::7e0" to="2603:1020:e04:1::7ff" />
	<address-range from="2603:1020:f04::600" to="2603:1020:f04::61f" />
	<address-range from="2603:1020:1004::5c0" to="2603:1020:1004::5df" />
	<address-range from="2603:1020:1004::7e0" to="2603:1020:1004::7ff" />
	<address-range from="2603:1020:1104::680" to="2603:1020:1104::69f" />
	<address-range from="2603:1020:1204:2::e0" to="2603:1020:1204:2::ff" />
	<address-range from="2603:1020:1302:1::1c0" to="2603:1020:1302:1::1df" />
	<address-range from="2603:1020:1403:2::140" to="2603:1020:1403:2::15f" />
	<address-range from="2603:1030:f:1::600" to="2603:1030:f:1::61f" />
	<address-range from="2603:1030:10:1::5c0" to="2603:1030:10:1::5df" />
	<address-range from="2603:1030:10:1::7e0" to="2603:1030:10:1::7ff" />
	<address-range from="2603:1030:104:1::5c0" to="2603:1030:104:1::5df" />
	<address-range from="2603:1030:104:1::7e0" to="2603:1030:104:1::7ff" />
	<address-range from="2603:1030:107::6a0" to="2603:1030:107::6bf" />
	<address-range from="2603:1030:210:1::5c0" to="2603:1030:210:1::5df" />
	<address-range from="2603:1030:210:1::7e0" to="2603:1030:210:1::7ff" />
	<address-range from="2603:1030:40b:1::5c0" to="2603:1030:40b:1::5df" />
	<address-range from="2603:1030:40c:1::5c0" to="2603:1030:40c:1::5df" />
	<address-range from="2603:1030:40c:1::7e0" to="2603:1030:40c:1::7ff" />
	<address-range from="2603:1030:504:1::5c0" to="2603:1030:504:1::5df" />
	<address-range from="2603:1030:504:1::7e0" to="2603:1030:504:1::7ff" />
	<address-range from="2603:1030:608::600" to="2603:1030:608::61f" />
	<address-range from="2603:1030:702:2::140" to="2603:1030:702:2::15f" />
	<address-range from="2603:1030:807:1::5c0" to="2603:1030:807:1::5df" />
	<address-range from="2603:1030:807:1::7e0" to="2603:1030:807:1::7ff" />
	<address-range from="2603:1030:a07::600" to="2603:1030:a07::61f" />
	<address-range from="2603:1030:b04::600" to="2603:1030:b04::61f" />
	<address-range from="2603:1030:c06:1::5c0" to="2603:1030:c06:1::5df" />
	<address-range from="2603:1030:f05:1::5c0" to="2603:1030:f05:1::5df" />
	<address-range from="2603:1030:f05:1::7e0" to="2603:1030:f05:1::7ff" />
	<address-range from="2603:1030:1005::600" to="2603:1030:1005::61f" />
	<address-range from="2603:1040:5::e0" to="2603:1040:5::ff" />
	<address-range from="2603:1040:5:1::5c0" to="2603:1040:5:1::5df" />
	<address-range from="2603:1040:5:1::7e0" to="2603:1040:5:1::7ff" />
	<address-range from="2603:1040:207::600" to="2603:1040:207::61f" />
	<address-range from="2603:1040:407:1::5c0" to="2603:1040:407:1::5df" />
	<address-range from="2603:1040:407:1::7e0" to="2603:1040:407:1::7ff" />
	<address-range from="2603:1040:606::600" to="2603:1040:606::61f" />
	<address-range from="2603:1040:806::600" to="2603:1040:806::61f" />
	<address-range from="2603:1040:904:1::5c0" to="2603:1040:904:1::5df" />
	<address-range from="2603:1040:904:1::7e0" to="2603:1040:904:1::7ff" />
	<address-range from="2603:1040:a06::e0" to="2603:1040:a06::ff" />
	<address-range from="2603:1040:a06:1::5c0" to="2603:1040:a06:1::5df" />
	<address-range from="2603:1040:a06:1::7e0" to="2603:1040:a06:1::7ff" />
	<address-range from="2603:1040:b04::600" to="2603:1040:b04::61f" />
	<address-range from="2603:1040:c06::600" to="2603:1040:c06::61f" />
	<address-range from="2603:1040:d04::5c0" to="2603:1040:d04::5df" />
	<address-range from="2603:1040:d04::7e0" to="2603:1040:d04::7ff" />
	<address-range from="2603:1040:f05:1::5c0" to="2603:1040:f05:1::5df" />
	<address-range from="2603:1040:f05:1::7e0" to="2603:1040:f05:1::7ff" />
	<address-range from="2603:1040:1002:1::1e0" to="2603:1040:1002:1::1ff" />
	<address-range from="2603:1040:1104::680" to="2603:1040:1104::69f" />
	<address-range from="2603:1040:1302:1::4e0" to="2603:1040:1302:1::4ff" />
	<address-range from="2603:1040:1402:1::1c0" to="2603:1040:1402:1::1df" />
	<address-range from="2603:1050:6:1::5c0" to="2603:1050:6:1::5df" />
	<address-range from="2603:1050:6:1::7e0" to="2603:1050:6:1::7ff" />
	<address-range from="2603:1050:403::5c0" to="2603:1050:403::5df" />
	<address-range from="2a01:111:20a::" to="2a01:111:20a:ffff:ffff:ffff:ffff:ffff" />
	<address-range from="2a01:111:2050::" to="2a01:111:205f:ffff:ffff:ffff:ffff:ffff" />
</ip-filter>
```

Use the snippet in the output file in the API Management service policy as described at https://learn.microsoft.com/en-us/azure/api-management/api-management-access-restriction-policies#RestrictCallerIPs
