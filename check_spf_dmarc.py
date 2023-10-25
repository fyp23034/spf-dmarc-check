import dns.resolver
import checkdmarc

# will be passed from the backend when calling classfication API, this is an example
senderAddress = "account-security-noreply@accountprotection.microsoft.com"  

domain = checkdmarc.get_base_domain(senderAddress)  # get the base email server domain from the sender address

# source: https://www.thierolf.org/blog/2021/small-python-script-to-quick-test-dmarc-dkim-and-spf-records/
try:
    test_dmarc = dns.resolver.resolve('_dmarc.' + domain , 'TXT')
    for dns_data in test_dmarc:
        if 'DMARC1' in str(dns_data):
            print("  [PASS] DMARC record found!")
            # print out the DMARC record if you want to see it
            # print(dns_data)
except:
    print("  [FAIL] DMARC record not found.")

try:
    test_spf = dns.resolver.resolve(domain , 'TXT')
    for dns_data in test_spf:
        if 'spf1' in str(dns_data):
            print ("  [PASS] SPF record found!")
            # print out the SPF record if you want to see it
            # print(dns_data)
except:
    print ("  [FAIL] SPF record not found.")